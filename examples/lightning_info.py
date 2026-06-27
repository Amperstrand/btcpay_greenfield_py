"""Lightning node info example.

Retrieves information about the Lightning node associated with a store.
Requires the store to have a Lightning payment method configured and the
``btcpay.store.canviewlightninginvoice`` permission.

This will likely fail against testnet.demo.btcpayserver.org unless your
auto-registered store has Lightning configured.

Required env vars:
    BTCPAY_API_KEY   API key with btcpay.store.canuselightningnode
    BTCPAY_STORE_ID  the store with Lightning configured
"""

from __future__ import annotations

import sys

from config import get_client, get_store_id

from btcpay_greenfield_py.api.lightning_store.store_lightning_node_api_get_info import (
    sync_detailed as get_ln_info,
)


def main() -> None:
    client = get_client()
    store_id = get_store_id()

    with client as c:
        info = get_ln_info(store_id=store_id, crypto_code="BTC", client=c)

        if info.status_code.value != 200:
            body = info.content.decode("utf-8", errors="replace")
            print(f"failed (likely no Lightning node configured): HTTP {info.status_code}\n{body}", file=sys.stderr)
            return

        node = info.parsed
        if node is None:
            print("200 OK but empty body", file=sys.stderr)
            return

        print(f"node alias:     {getattr(node, 'alias', '?')}")
        print(f"public key:     {getattr(node, 'node_info', None)}")
        bh = getattr(node, "block_height", "?")
        peers = getattr(node, "peers", []) or []
        print(f"block height:   {bh}")
        print(f"peers:          {len(peers)}")
        chains = getattr(node, 'chains', [])
        if chains:
            print(f"chains:         {chains}")


if __name__ == "__main__":
    main()
