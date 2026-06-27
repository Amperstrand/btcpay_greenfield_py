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
