"""Shared pytest fixtures and test configuration.

Environment variables consumed
------------------------------
BTCPAY_HOST       Default https://testnet.demo.btcpayserver.org
BTCPAY_API_KEY    Greenfield API key (required for authed tests)
BTCPAY_STORE_ID   Store ID (required for store-scoped authed tests)
"""

from __future__ import annotations

import os
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

# Make the examples/ module importable so tests can reuse examples/config.py
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

DEFAULT_HOST = "https://testnet.demo.btcpayserver.org"


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "network: test makes real HTTP calls")


@pytest.fixture
def btcpay_host() -> str:
    return os.environ.get("BTCPAY_HOST", DEFAULT_HOST)


@pytest.fixture
def unauth_client(btcpay_host: str):
    """Anonymous Client — only works for endpoints that allow no auth."""
    from btcpay_greenfield_py import Client

    return Client(base_url=btcpay_host)


@pytest.fixture
def authed_client(btcpay_host: str):
    """Authenticated client (API key). Skips the test if BTCPAY_API_KEY is unset."""
    api_key = os.environ.get("BTCPAY_API_KEY")
    if not api_key:
        pytest.skip("BTCPAY_API_KEY not set — set it to run authed smoke tests")
    from btcpay_greenfield_py import AuthenticatedClient

    return AuthenticatedClient(base_url=btcpay_host, token=api_key, prefix="token")


@pytest.fixture
def store_id() -> str:
    sid = os.environ.get("BTCPAY_STORE_ID")
    if not sid:
        pytest.skip("BTCPAY_STORE_ID not set — required for store-scoped tests")
    return sid


@pytest.fixture(autouse=True)
def _skip_network_offline(request, btcpay_host: str) -> Iterator[None]:
    """Auto-skip tests marked 'network' if we can't reach the host.

    Run with `pytest -m "not network"` to skip all real-network tests.
    """
    if request.node.get_closest_marker("network"):
        import httpx

        try:
            # Cheap reachability check
            with httpx.Client(timeout=5.0) as c:
                c.get(f"{btcpay_host}/api/v1/health")
        except httpx.HTTPError as exc:
            pytest.skip(f"cannot reach {btcpay_host}: {exc}")
    yield
