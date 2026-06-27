"""Production middleware for the BTCPay Greenfield Python client.

Wraps the generated ``Client`` / ``AuthenticatedClient`` with:

- **Retry** on 5xx and transient connection errors, with exponential backoff
- **Timeouts** — sensible defaults (the generated client defaults to no timeout, which is dangerous)
- **Structured logging** via stdlib ``logging`` — request method + URL + status + duration.
  Auth headers are NEVER logged.
- **Metrics hooks** — optional callbacks for request count and latency (plug into Prometheus, Datadog, etc.)

Usage::

    from btcpay_greenfield_py import AuthenticatedClient
    from btcpay_greenfield_extras.middleware import configure_production_client

    client = AuthenticatedClient(base_url="https://btcpay.example.com", token="...", prefix="token")
    configure_production_client(client, max_retries=3, timeout=30.0)
    # client now has retry, timeouts, and logging configured
"""

from __future__ import annotations

import logging
import time
from typing import Any, Protocol, runtime_checkable

import httpx

DEFAULT_TIMEOUT = httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=5.0)
DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 0.5

_LOGGER = logging.getLogger("btcpay_greenfield")


@runtime_checkable
class MetricsCallback(Protocol):
    def __call__(
        self,
        *,
        method: str,
        url: str,
        status: int | None,
        duration_s: float,
        retried: bool,
        error: str | None,
    ) -> None: ...


class RetryTransport(httpx.BaseTransport):
    """Wraps an httpx transport with automatic retry on 5xx + transient errors."""

    def __init__(
        self,
        wrapped: httpx.BaseTransport,
        *,
        max_retries: int = DEFAULT_MAX_RETRIES,
        backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
        logger: logging.Logger | None = None,
        metrics: MetricsCallback | None = None,
    ) -> None:
        self._wrapped = wrapped
        self._max_retries = max_retries
        self._backoff_factor = backoff_factor
        self._logger = logger or _LOGGER
        self._metrics = metrics

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        last_exc: Exception | None = None
        start = time.monotonic()
        retried = False

        for attempt in range(self._max_retries + 1):
            try:
                response = self._wrapped.handle_request(request)
                duration = time.monotonic() - start
                if response.status_code < 500:
                    self._emit(method=request.method, url=str(request.url),
                               status=response.status_code, duration=duration,
                               retried=retried, error=None)
                    return response
                last_exc = None
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout,
                    httpx.PoolTimeout) as exc:
                last_exc = exc
                duration = time.monotonic() - start

            if attempt >= self._max_retries:
                break

            retried = True
            delay = self._backoff_factor * (2 ** attempt)
            self._logger.warning(
                "retrying %s %s (attempt %d/%d) after %.1fs — %s",
                request.method, request.url, attempt + 2, self._max_retries + 1,
                delay, last_exc or f"HTTP {response.status_code}",
            )
            time.sleep(delay)

        duration = time.monotonic() - start
        status: int | None = None
        error_msg: str | None = None

        if last_exc is not None:
            error_msg = type(last_exc).__name__
            self._emit(method=request.method, url=str(request.url), status=None,
                       duration=duration, retried=retried, error=error_msg)
            raise last_exc

        status = response.status_code
        self._emit(method=request.method, url=str(request.url), status=status,
                   duration=duration, retried=retried, error=None)
        return response

    def _emit(self, **kwargs: Any) -> None:
        if self._metrics:
            try:
                self._metrics(**kwargs)
            except Exception:
                pass


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async version of RetryTransport."""

    def __init__(
        self,
        wrapped: httpx.AsyncBaseTransport,
        *,
        max_retries: int = DEFAULT_MAX_RETRIES,
        backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
        logger: logging.Logger | None = None,
        metrics: MetricsCallback | None = None,
    ) -> None:
        self._wrapped = wrapped
        self._max_retries = max_retries
        self._backoff_factor = backoff_factor
        self._logger = logger or _LOGGER
        self._metrics = metrics

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        import asyncio

        last_exc: Exception | None = None
        start = time.monotonic()
        retried = False

        for attempt in range(self._max_retries + 1):
            try:
                response = await self._wrapped.handle_async_request(request)
                duration = time.monotonic() - start
                if response.status_code < 500:
                    self._emit(method=request.method, url=str(request.url),
                               status=response.status_code, duration=duration,
                               retried=retried, error=None)
                    return response
                last_exc = None
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout,
                    httpx.PoolTimeout) as exc:
                last_exc = exc
                duration = time.monotonic() - start

            if attempt >= self._max_retries:
                break

            retried = True
            delay = self._backoff_factor * (2 ** attempt)
            self._logger.warning(
                "retrying %s %s (attempt %d/%d) after %.1fs",
                request.method, request.url, attempt + 2, self._max_retries + 1, delay,
            )
            await asyncio.sleep(delay)

        duration = time.monotonic() - start
        if last_exc is not None:
            self._emit(method=request.method, url=str(request.url), status=None,
                       duration=duration, retried=retried, error=type(last_exc).__name__)
            raise last_exc

        self._emit(method=request.method, url=str(request.url),
                   status=response.status_code, duration=duration,
                   retried=retried, error=None)
        return response

    def _emit(self, **kwargs: Any) -> None:
        if self._metrics:
            try:
                self._metrics(**kwargs)
            except Exception:
                pass


def create_logging_hooks(logger: logging.Logger | None = None) -> dict[str, list[Any]]:
    """Return httpx event hooks for structured request/response logging.

    Logs ``method + URL + status_code`` only. NEVER logs headers, body, or auth tokens.
    """
    log = logger or _LOGGER

    def _req(request: httpx.Request) -> None:
        log.info("→ %s %s", request.method, request.url)

    def _resp(response: httpx.Response) -> None:
        request = response.request
        log.info("← %s %s [%d]", request.method, request.url, response.status_code)

    return {"request": [_req], "response": [_resp]}


def configure_production_client(
    client: httpx.Client | Any,
    *,
    max_retries: int = DEFAULT_MAX_RETRIES,
    timeout: httpx.Timeout | float | None = DEFAULT_TIMEOUT,
    backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
    logging_enabled: bool = True,
    logger: logging.Logger | None = None,
    metrics: MetricsCallback | None = None,
) -> Any:
    """Configure a generated Client/AuthenticatedClient with production defaults.

    Applies retry transport, sensible timeout, structured logging, and optional
    metrics callbacks. Must be called AFTER entering the client context (or
    after manually calling ``client.get_httpx_client()``).

    Returns the same client for chaining.
    """
    sync_client = client.get_httpx_client()
    _apply_to_httpx(sync_client, max_retries, timeout, backoff_factor,
                    logging_enabled, logger, metrics)

    try:
        async_client = client.get_async_httpx_client()
        _apply_to_async_httpx(async_client, max_retries, timeout, backoff_factor,
                              logging_enabled, logger, metrics)
    except Exception:
        pass

    return client


def _apply_to_httpx(
    httpx_client: httpx.Client,
    max_retries: int,
    timeout: httpx.Timeout | float | None,
    backoff_factor: float,
    logging_enabled: bool,
    logger: logging.Logger | None,
    metrics: MetricsCallback | None,
) -> None:
    if timeout is not None:
        httpx_client.timeout = timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)

    original_transport = httpx_client._transport
    if original_transport is not None:
        httpx_client._transport = RetryTransport(
            original_transport,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            logger=logger,
            metrics=metrics,
        )

    if logging_enabled:
        hooks = create_logging_hooks(logger)
        for event, fns in hooks.items():
            existing = httpx_client.event_hooks.get(event, [])
            httpx_client.event_hooks[event] = list(existing) + fns


def _apply_to_async_httpx(
    httpx_client: httpx.AsyncClient,
    max_retries: int,
    timeout: httpx.Timeout | float | None,
    backoff_factor: float,
    logging_enabled: bool,
    logger: logging.Logger | None,
    metrics: MetricsCallback | None,
) -> None:
    if timeout is not None:
        httpx_client.timeout = timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)

    original_transport = httpx_client._transport
    if original_transport is not None:
        httpx_client._transport = AsyncRetryTransport(
            original_transport,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            logger=logger,
            metrics=metrics,
        )

    if logging_enabled:
        hooks = create_logging_hooks(logger)
        for event, fns in hooks.items():
            existing = httpx_client.event_hooks.get(event, [])
            httpx_client.event_hooks[event] = list(existing) + fns
