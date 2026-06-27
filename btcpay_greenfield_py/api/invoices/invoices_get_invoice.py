from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_data import InvoiceData
from ...types import Response


def _safe_from_dict(parser, response):
    if not response.content:
        return None
    try:
        return parser(response.json())
    except Exception:
        return None


def _get_kwargs(
    store_id: str,
    invoice_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/invoices/{invoice_id}".format(
            store_id=quote(str(store_id), safe=""),
            invoice_id=quote(str(invoice_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvoiceData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(InvoiceData.from_dict, response)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvoiceData]:
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
) -> Response[Any | InvoiceData]:
    """Get invoice

     View information about the specified invoice

    Args:
        store_id (str):
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvoiceData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        invoice_id=invoice_id,
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
) -> Any | InvoiceData | None:
    """Get invoice

     View information about the specified invoice

    Args:
        store_id (str):
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvoiceData
    """

    return sync_detailed(
        store_id=store_id,
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | InvoiceData]:
    """Get invoice

     View information about the specified invoice

    Args:
        store_id (str):
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvoiceData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        invoice_id=invoice_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | InvoiceData | None:
    """Get invoice

     View information about the specified invoice

    Args:
        store_id (str):
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvoiceData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
