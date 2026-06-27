"""Create a test invoice against the BTCPay Greenfield API.

Required env vars:
    BTCPAY_API_KEY   API key with btcpay.store.cancreateinvoice permission
    BTCPAY_STORE_ID  the store to create the invoice under

Optional:
    BTCPAY_HOST      defaults to https://testnet.demo.btcpayserver.org

Usage:
    BTCPAY_API_KEY=... BTCPAY_STORE_ID=... python examples/create_invoice.py

Note: On testnet.demo.btcpayserver.org, freshly-registered stores have no
wallet linked, so invoice creation returns HTTP 400. This script reports
the server's error message instead of crashing in that case.
"""

from __future__ import annotations

import sys
from pprint import pprint

from config import get_client, get_store_id

from btcpay_greenfield_py.api.invoices.invoices_create_invoice import sync_detailed as create_invoice
from btcpay_greenfield_py.models.create_invoice_request import CreateInvoiceRequest


def main() -> None:
    client = get_client()
    store_id = get_store_id()

    with client as c:
        response = create_invoice(
            store_id=store_id,
            client=c,
            body=CreateInvoiceRequest(
                amount="1.50",
                currency="USD",
            ),
        )

    print(f"HTTP {response.status_code.value}")

    if response.status_code.value != 200:
        body = response.content.decode("utf-8", errors="replace")
        print(f"server declined invoice creation: {body}", file=sys.stderr)
        return

    invoice = response.parsed
    if invoice is None:
        print("200 OK but empty body — unexpected", file=sys.stderr)
        return

    print(f"created invoice {invoice.id}")
    print(f"  status:        {invoice.status}")
    print(f"  amount:        {invoice.amount} {invoice.currency}")
    print(f"  checkout link: {invoice.checkout_link}")
    print()
    pprint(invoice.to_dict())


if __name__ == "__main__":
    main()
