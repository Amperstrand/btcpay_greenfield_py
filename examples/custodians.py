"""Custodian operations example.

Lists supported custodians (exchange integrations) on the BTCPay Server
instance. Custodians allow stores to deposit, withdraw, and trade assets
on supported exchanges.

This endpoint requires authentication but should work against any BTCPay
Server instance (it lists what's available, not account-specific data).

Required env vars:
    BTCPAY_API_KEY   any valid API key
"""

from __future__ import annotations

import sys

from config import get_client

from btcpay_greenfield_py.api.custodians.custodians_get_supported_custodians import (
    sync_detailed as get_supported_custodians,
)


def main() -> None:
    client = get_client()

    with client as c:
        result = get_supported_custodians(client=c)

        if result.status_code.value != 200:
            body = result.content.decode("utf-8", errors="replace")
            print(f"failed: HTTP {result.status_code}\n{body}", file=sys.stderr)
            return

        custodians = result.parsed
        if not isinstance(custodians, list):
            print("unexpected response type", file=sys.stderr)
            return

        print(f"supported custodians ({len(custodians)}):")
        for item in custodians:
            code = getattr(item, "code", "?")
            name = getattr(item, "name", "?")
            print(f"  {code}: {name}")


if __name__ == "__main__":
    main()
