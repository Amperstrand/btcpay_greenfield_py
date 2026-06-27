"""Payment request example: create and list payment requests.

Payment requests are reusable links for specific amounts. Unlike invoices
(which expire), payment requests persist until fulfilled or cancelled.

Required env vars:
    BTCPAY_API_KEY   API key with btcpay.store.canmodifypaymentrequests
    BTCPAY_STORE_ID  the store to create the payment request under
"""

from __future__ import annotations

import sys

from config import get_client, get_store_id

from btcpay_greenfield_py.api.payment_requests.payment_requests_create_payment_request import (
    sync_detailed as create_payment_request,
)
from btcpay_greenfield_py.api.payment_requests.payment_requests_get_payment_requests import (
    sync_detailed as get_payment_requests,
)
from btcpay_greenfield_py.models.payment_request_base_data import PaymentRequestBaseData


def main() -> None:
    client = get_client()
    store_id = get_store_id()

    with client as c:
        created = create_payment_request(
            store_id=store_id,
            client=c,
            body=PaymentRequestBaseData(
                amount="50.00",
                currency="USD",
                title="Test Payment Request",
                description="Payment for services rendered",
            ),
        )

        if created.status_code.value != 200:
            print(f"creation failed: HTTP {created.status_code} {created.content!r}", file=sys.stderr)
            return

        pr = created.parsed
        print(f"created payment request: {pr.id if pr else '?'}")
        print(f"  title:  {pr.title if pr else '?'}")
        print(f"  amount: {pr.amount if pr else '?'} {pr.currency if pr else '?'}")

        existing = get_payment_requests(store_id=store_id, client=c)
        if existing.status_code.value == 200 and isinstance(existing.parsed, list):
            print(f"\nstore has {len(existing.parsed)} payment request(s)")
            for item in existing.parsed[:5]:
                print(f"  {item.id}: {item.title} — {item.amount} {item.currency}")


if __name__ == "__main__":
    main()
