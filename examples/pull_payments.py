"""Pull payment example: create and list pull payments.

Pull payments allow recipients to request payouts up to a specified amount.
Common uses: salaries, refunds, community payouts.

Required env vars:
    BTCPAY_API_KEY   API key with btcpay.store.cancreatepullpayments
    BTCPAY_STORE_ID  the store to create the pull payment under
"""

from __future__ import annotations

import sys

from config import get_client, get_store_id

from btcpay_greenfield_py.api.pull_payments_management.pull_payments_create_pull_payment import (
    sync_detailed as create_pull_payment,
)
from btcpay_greenfield_py.api.pull_payments_management.pull_payments_get_pull_payments import (
    sync_detailed as get_pull_payments,
)
from btcpay_greenfield_py.models.pull_payments_create_pull_payment_body import (
    PullPaymentsCreatePullPaymentBody,
)


def main() -> None:
    client = get_client()
    store_id = get_store_id()

    with client as c:
        created = create_pull_payment(
            store_id=store_id,
            client=c,
            body=PullPaymentsCreatePullPaymentBody(
                name="Test Pull Payment",
                amount="100.00",
                currency="USD",
            ),
        )

        if created.status_code.value != 200:
            print(f"creation failed: HTTP {created.status_code} {created.content!r}", file=sys.stderr)
            return

        pp = created.parsed
        print(f"created pull payment: {pp.id if pp else '?'}")
        print(f"  name:   {pp.name if pp else '?'}")
        print(f"  amount: {pp.amount if pp else '?'} {pp.currency if pp else '?'}")

        existing = get_pull_payments(store_id=store_id, client=c)
        if existing.status_code.value == 200 and isinstance(existing.parsed, list):
            print(f"\nstore has {len(existing.parsed)} pull payment(s)")
            for item in existing.parsed[:5]:
                print(f"  {item.id}: {item.name} — {item.amount} {item.currency}")


if __name__ == "__main__":
    main()
