"""Shared client configuration for the examples.

Picks up the BTCPay target host and API key from environment variables so we
never hard-code secrets into the repo.

Required env vars
-----------------
BTCPAY_HOST      e.g. https://testnet.demo.btcpayserver.org
BTCPAY_API_KEY   a Greenfield API key with the permissions your script needs

Optional
--------
BTCPAY_STORE_ID  store ID, required for any store-scoped call (invoices, etc.)
"""

from __future__ import annotations

import os

from btcpay_greenfield_py import AuthenticatedClient, Client

DEFAULT_HOST = "https://testnet.demo.btcpayserver.org"


def get_client() -> AuthenticatedClient:
    """Authenticated client using an API key (Authorization: token <key>)."""
    return AuthenticatedClient(
        base_url=os.environ.get("BTCPAY_HOST", DEFAULT_HOST),
        token=os.environ["BTCPAY_API_KEY"],
        prefix="token",  # BTCPay's expected Authorization scheme
    )


def get_unauth_client() -> Client:
    """Anonymous client — only works for endpoints that allow no auth (e.g. /health)."""
    return Client(base_url=os.environ.get("BTCPAY_HOST", DEFAULT_HOST))


def get_store_id() -> str:
    return os.environ["BTCPAY_STORE_ID"]


if __name__ == "__main__":
    # Smoke check: print resolved config without leaking the key.
    host = os.environ.get("BTCPAY_HOST", DEFAULT_HOST)
    key_set = bool(os.environ.get("BTCPAY_API_KEY"))
    store_set = bool(os.environ.get("BTCPAY_STORE_ID"))
    print(f"host:      {host}")
    print(f"api key:   {'set' if key_set else 'MISSING'}")
    print(f"store id:  {'set' if store_set else 'MISSING'}")
