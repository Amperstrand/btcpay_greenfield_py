from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_payment_method_data_model import InvoicePaymentMethodDataModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: str,
    invoice_id: str,
    *,
    only_accounted_payments: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["onlyAccountedPayments"] = only_accounted_payments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/invoices/{invoice_id}/payment-methods".format(
            store_id=quote(str(store_id), safe=""),
            invoice_id=quote(str(invoice_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[InvoicePaymentMethodDataModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InvoicePaymentMethodDataModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[InvoicePaymentMethodDataModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    only_accounted_payments: bool | Unset = True,
) -> Response[Any | list[InvoicePaymentMethodDataModel]]:
    """Get invoice payment methods

     View information about the specified invoice's payment methods

    Args:
        store_id (str):
        invoice_id (str):
        only_accounted_payments (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[InvoicePaymentMethodDataModel]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        invoice_id=invoice_id,
        only_accounted_payments=only_accounted_payments,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    only_accounted_payments: bool | Unset = True,
) -> Any | list[InvoicePaymentMethodDataModel] | None:
    """Get invoice payment methods

     View information about the specified invoice's payment methods

    Args:
        store_id (str):
        invoice_id (str):
        only_accounted_payments (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[InvoicePaymentMethodDataModel]
    """

    return sync_detailed(
        store_id=store_id,
        invoice_id=invoice_id,
        client=client,
        only_accounted_payments=only_accounted_payments,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    only_accounted_payments: bool | Unset = True,
) -> Response[Any | list[InvoicePaymentMethodDataModel]]:
    """Get invoice payment methods

     View information about the specified invoice's payment methods

    Args:
        store_id (str):
        invoice_id (str):
        only_accounted_payments (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[InvoicePaymentMethodDataModel]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        invoice_id=invoice_id,
        only_accounted_payments=only_accounted_payments,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    only_accounted_payments: bool | Unset = True,
) -> Any | list[InvoicePaymentMethodDataModel] | None:
    """Get invoice payment methods

     View information about the specified invoice's payment methods

    Args:
        store_id (str):
        invoice_id (str):
        only_accounted_payments (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[InvoicePaymentMethodDataModel]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            invoice_id=invoice_id,
            client=client,
            only_accounted_payments=only_accounted_payments,
        )
    ).parsed
