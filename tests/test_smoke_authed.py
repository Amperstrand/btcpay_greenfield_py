"""Authenticated smoke tests — requires BTCPAY_API_KEY (and BTCPAY_STORE_ID for store-scoped tests).

These are skipped automatically unless the env vars are set, so they run in CI
only when the repo has the appropriate secrets configured. See README "CI setup".
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.network


def test_whoami(authed_client) -> None:
    """GET /api/v1/users/me — verifies the API key is valid and the auth header format works."""
    from btcpay_greenfield_py.api.users.users_get_current_user import sync_detailed

    with authed_client as c:
        r = sync_detailed(client=c)
    assert r.status_code.value == 200, f"got {r.status_code}: {r.content!r}"
    assert r.parsed is not None
    assert r.parsed.email  # the API always returns the user's email


def test_list_stores(authed_client) -> None:
    """GET /api/v1/stores — list stores the API key has access to."""
    from btcpay_greenfield_py.api.stores.stores_get_stores import sync_detailed

    with authed_client as c:
        r = sync_detailed(client=c)
    assert r.status_code.value == 200
    assert isinstance(r.parsed, list)


def test_list_invoices_for_store(authed_client, store_id) -> None:
    """GET /api/v1/stores/{storeId}/invoices — list invoices in the configured store."""
    from btcpay_greenfield_py.api.invoices.invoices_get_invoices import sync_detailed

    with authed_client as c:
        r = sync_detailed(store_id=store_id, client=c)
    assert r.status_code.value == 200
    assert isinstance(r.parsed, list)


def test_create_and_archive_invoice(authed_client, store_id) -> None:
    """Round-trip exercise of the invoice create + error-response parsing path.

    On testnet.demo.btcpayserver.org, freshly-registered stores have no wallet
    linked, so BTCPay refuses to create invoices with a 400. The point of this
    test is NOT to assert that invoice creation succeeds — it's to assert that:

    1. The library successfully transmits the request and parses the response.
    2. The library does NOT crash on a 4xx with an unexpected body shape
       (BTCPay returns ``{"code": ..., "message": ...}`` even though the spec
       declares the 400 response as ``list[ValidationProblemDetailsItem]``).
    3. If invoice creation DOES succeed (e.g. against a configured self-hosted
       server), we follow up by archiving the created invoice.
    """
    from btcpay_greenfield_py.api.invoices.invoices_archive_invoice import sync_detailed as archive
    from btcpay_greenfield_py.api.invoices.invoices_create_invoice import sync_detailed as create
    from btcpay_greenfield_py.models.create_invoice_request import CreateInvoiceRequest

    with authed_client as c:
        created = create(
            store_id=store_id,
            client=c,
            body=CreateInvoiceRequest(amount="0.50", currency="USD"),
        )

        if created.status_code.value == 200:
            # Happy path: invoice was created. Verify parsing worked and archive it.
            assert created.parsed is not None, "200 with empty parsed body"
            invoice_id = created.parsed.id
            assert invoice_id, "server did not return an invoice id"

            archived = archive(store_id=store_id, invoice_id=invoice_id, client=c)
            assert archived.status_code.value in (200, 204), archived.content
        else:
            # Testnet-without-wallet path: 4xx with body the spec types as a list
            # but the server actually sends a single object. Library must NOT
            # crash — `parsed` should be an empty list, None, or a ProblemDetails.
            assert created.status_code.value in (400, 403), (
                f"unexpected status {created.status_code}: {created.content!r}"
            )
            assert created.parsed is None or created.parsed == [] or hasattr(created.parsed, "message"), (
                f"library returned an unexpected parsed value for error response: "
                f"{created.parsed!r}"
            )


def test_create_and_list_pull_payment(authed_client, store_id) -> None:
    """Round-trip: create a pull payment, then list the store's pull payments.

    On testnet.demo.btcpayserver.org, pull payment creation may return 500
    if the store lacks proper payment method configuration. The test verifies
    the library handles both success and server-side failure without crashing.
    """
    from btcpay_greenfield_py.api.pull_payments_management.pull_payments_create_pull_payment import (
        sync_detailed as create_pp,
    )
    from btcpay_greenfield_py.api.pull_payments_management.pull_payments_get_pull_payments import (
        sync_detailed as get_pps,
    )
    from btcpay_greenfield_py.models.pull_payments_create_pull_payment_body import (
        PullPaymentsCreatePullPaymentBody,
    )

    with authed_client as c:
        created = create_pp(
            store_id=store_id,
            client=c,
            body=PullPaymentsCreatePullPaymentBody(
                name="CI Test Pull Payment",
                amount="10.00",
                currency="USD",
            ),
        )

        if created.status_code.value == 200:
            assert created.parsed is not None
            pp_id = created.parsed.id
            assert pp_id, "server did not return a pull payment id"

            listed = get_pps(store_id=store_id, client=c)
            assert listed.status_code.value == 200
            assert isinstance(listed.parsed, list)
            ids = [p.id for p in listed.parsed]
            assert pp_id in ids, f"created pull payment {pp_id} not found in list"
        else:
            assert created.status_code.value in (400, 500), (
                f"unexpected status {created.status_code}: {created.content!r}"
            )


def test_create_and_list_payment_request(authed_client, store_id) -> None:
    """Round-trip: create a payment request, then list the store's payment requests.

    Payment requests don't require a configured wallet, so this should succeed
    on testnet.demo.btcpayserver.org.
    """
    from btcpay_greenfield_py.api.payment_requests.payment_requests_create_payment_request import (
        sync_detailed as create_pr,
    )
    from btcpay_greenfield_py.api.payment_requests.payment_requests_get_payment_requests import (
        sync_detailed as get_prs,
    )
    from btcpay_greenfield_py.models.payment_request_base_data import PaymentRequestBaseData

    with authed_client as c:
        created = create_pr(
            store_id=store_id,
            client=c,
            body=PaymentRequestBaseData(
                amount="25.00",
                currency="USD",
                title="CI Test Payment Request",
            ),
        )
        assert created.status_code.value == 200, f"create failed: {created.content!r}"
        assert created.parsed is not None
        pr_id = created.parsed.id
        assert pr_id, "server did not return a payment request id"

        listed = get_prs(store_id=store_id, client=c)
        assert listed.status_code.value == 200
        assert isinstance(listed.parsed, list)
        ids = [p.id for p in listed.parsed]
        assert pr_id in ids, f"created payment request {pr_id} not found in list: {ids}"


def test_list_supported_custodians(authed_client) -> None:
    """GET /api/v1/custodians — list supported custodian integrations.

    The custodians feature may not be installed on all BTCPay Server instances
    (testnet.demo returns 404). The test verifies the library handles both
    presence and absence of the feature without crashing.
    """
    from btcpay_greenfield_py.api.custodians.custodians_get_supported_custodians import (
        sync_detailed as get_custodians,
    )

    with authed_client as c:
        r = get_custodians(client=c)

    assert r.status_code.value in (200, 404), (
        f"unexpected status {r.status_code}: {r.content!r}"
    )
    if r.status_code.value == 200:
        assert isinstance(r.parsed, list)
