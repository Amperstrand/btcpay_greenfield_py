"""Tests for btcpay_greenfield_extras.middleware — retry, logging, metrics."""

from __future__ import annotations

import logging

import httpx
import pytest

from btcpay_greenfield_extras.middleware import (
    DEFAULT_TIMEOUT,
    AsyncRetryTransport,
    RetryTransport,
    configure_production_client,
    create_logging_hooks,
)

# --- RetryTransport (sync) ---

class TestRetryTransport:
    def test_no_retry_on_2xx(self) -> None:
        calls: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(1)
            return httpx.Response(200, content=b"ok", request=request)

        transport = httpx.MockTransport(handler)
        retry = RetryTransport(transport, max_retries=3, backoff_factor=0)
        client = httpx.Client(transport=retry)

        response = client.get("https://example.com/test")
        assert response.status_code == 200
        assert len(calls) == 1

    def test_retries_on_500(self) -> None:
        attempts: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            attempts.append(1)
            if len(attempts) < 3:
                return httpx.Response(500, content=b"err", request=request)
            return httpx.Response(200, content=b"ok", request=request)

        transport = httpx.MockTransport(handler)
        retry = RetryTransport(transport, max_retries=3, backoff_factor=0)
        client = httpx.Client(transport=retry)

        response = client.get("https://example.com/test")
        assert response.status_code == 200
        assert len(attempts) == 3

    def test_gives_up_after_max_retries(self) -> None:
        attempts: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            attempts.append(1)
            return httpx.Response(503, content=b"down", request=request)

        transport = httpx.MockTransport(handler)
        retry = RetryTransport(transport, max_retries=2, backoff_factor=0)
        client = httpx.Client(transport=retry)

        response = client.get("https://example.com/test")
        assert response.status_code == 503
        assert len(attempts) == 3

    def test_retries_on_connect_error(self) -> None:
        attempts: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            attempts.append(1)
            if len(attempts) < 2:
                raise httpx.ConnectError("conn refused")
            return httpx.Response(200, content=b"ok", request=request)

        transport = httpx.MockTransport(handler)
        retry = RetryTransport(transport, max_retries=3, backoff_factor=0)
        client = httpx.Client(transport=retry)

        response = client.get("https://example.com/test")
        assert response.status_code == 200
        assert len(attempts) == 2

    def test_no_retry_on_4xx(self) -> None:
        calls: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(1)
            return httpx.Response(404, content=b"not found", request=request)

        transport = httpx.MockTransport(handler)
        retry = RetryTransport(transport, max_retries=3, backoff_factor=0)
        client = httpx.Client(transport=retry)

        response = client.get("https://example.com/test")
        assert response.status_code == 404
        assert len(calls) == 1

    def test_metrics_callback_fires(self) -> None:
        recorded: list[dict] = []

        def metrics(**kwargs: object) -> None:
            recorded.append(kwargs)

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(200, content=b"ok", request=request)

        transport = httpx.MockTransport(handler)
        retry = RetryTransport(transport, max_retries=3, backoff_factor=0, metrics=metrics)
        client = httpx.Client(transport=retry)

        client.get("https://example.com/test")
        assert len(recorded) == 1
        assert recorded[0]["method"] == "GET"
        assert recorded[0]["status"] == 200
        assert recorded[0]["retried"] is False


# --- AsyncRetryTransport ---

class TestAsyncRetryTransport:
    @pytest.mark.asyncio
    async def test_retries_on_500_async(self) -> None:
        attempts: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            attempts.append(1)
            if len(attempts) < 2:
                return httpx.Response(500, content=b"err", request=request)
            return httpx.Response(200, content=b"ok", request=request)

        transport = httpx.MockTransport(handler)
        retry = AsyncRetryTransport(transport, max_retries=3, backoff_factor=0)
        async with httpx.AsyncClient(transport=retry) as client:
            response = await client.get("https://example.com/test")
            assert response.status_code == 200
            assert len(attempts) == 2


# --- Logging hooks ---

class TestLoggingHooks:
    def test_logs_request_and_response(self, caplog) -> None:
        hooks = create_logging_hooks()
        client = httpx.Client(
            transport=httpx.MockTransport(
                lambda req: httpx.Response(200, content=b"ok", request=req)
            ),
            event_hooks=hooks,
            base_url="https://example.com",
        )

        with caplog.at_level(logging.INFO, logger="btcpay_greenfield"):
            client.get("/test")

        messages = [r.message for r in caplog.records]
        assert any("→ GET" in m for m in messages)
        assert any("← GET" in m and "[200]" in m for m in messages)

    def test_never_logs_auth_headers(self, caplog) -> None:
        hooks = create_logging_hooks()
        client = httpx.Client(
            transport=httpx.MockTransport(
                lambda req: httpx.Response(200, content=b"ok", request=req)
            ),
            event_hooks=hooks,
            headers={"Authorization": "token super-secret-key"},
            base_url="https://example.com",
        )

        with caplog.at_level(logging.DEBUG):
            client.get("/test")

        full_log = "\n".join(r.message for r in caplog.records)
        assert "super-secret-key" not in full_log
        assert "Authorization" not in full_log


# --- configure_production_client ---

class TestConfigureProductionClient:
    def test_sets_timeout(self) -> None:
        from btcpay_greenfield_py import Client

        client = Client(base_url="https://example.com")
        client.get_httpx_client()
        configure_production_client(client, timeout=httpx.Timeout(5.0))

        assert client.get_httpx_client().timeout.connect == 5.0

    def test_wraps_transport(self) -> None:
        from btcpay_greenfield_py import Client

        client = Client(base_url="https://example.com")
        client.get_httpx_client()
        configure_production_client(client, max_retries=5)

        wrapped = client.get_httpx_client()._transport
        assert isinstance(wrapped, RetryTransport)
        assert wrapped._max_retries == 5

    def test_default_timeout_is_set(self) -> None:
        from btcpay_greenfield_py import Client

        client = Client(base_url="https://example.com")
        client.get_httpx_client()
        configure_production_client(client)

        timeout = client.get_httpx_client().timeout
        assert timeout is not None
        assert timeout.read == DEFAULT_TIMEOUT.read
