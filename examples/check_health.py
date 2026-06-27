"""Health check — no auth required.

Demonstrates the simplest possible call against the BTCPay Greenfield API:
GET /api/v1/health. Works against any public BTCPay Server instance.

Usage:
    python examples/check_health.py
    BTCPAY_HOST=https://mainnet.demo.btcpayserver.org python examples/check_health.py
"""

from __future__ import annotations

import sys

import httpx
from config import get_unauth_client

from btcpay_greenfield_py.api.health.health_get_health import sync_detailed as get_health_detailed


def main() -> None:
    # /api/v1/health is anonymous on every BTCPay Server instance.
    client = get_unauth_client()

    try:
        with client as client:
            response = get_health_detailed(client=client)
    except httpx.HTTPError as exc:
        print(f"transport error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"HTTP {response.status_code.value}")

    if response.parsed is None:
        # The generated _parse_response blindly tries to JSON-parse error bodies,
        # which can raise if the server returns an empty body. Fall back to raw bytes.
        print(f"raw body: {response.content!r}")
        return

    # ApplicationHealthData has a single field: `synchronized`
    print(f"synchronized: {response.parsed.synchronized}")


if __name__ == "__main__":
    main()
