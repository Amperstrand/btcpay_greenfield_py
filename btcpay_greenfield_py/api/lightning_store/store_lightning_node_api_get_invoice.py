from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lightning_invoice_data import LightningInvoiceData
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
    crypto_code: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/lightning/{crypto_code}/invoices/{id}".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LightningInvoiceData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(LightningInvoiceData.from_dict, response)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LightningInvoiceData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    crypto_code: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | LightningInvoiceData]:
    """Get invoice

     View information about the requested lightning invoice

    Args:
        store_id (str):
        crypto_code (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningInvoiceData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    crypto_code: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | LightningInvoiceData | None:
    """Get invoice

     View information about the requested lightning invoice

    Args:
        store_id (str):
        crypto_code (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningInvoiceData
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | LightningInvoiceData]:
    """Get invoice

     View information about the requested lightning invoice

    Args:
        store_id (str):
        crypto_code (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningInvoiceData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | LightningInvoiceData | None:
    """Get invoice

     View information about the requested lightning invoice

    Args:
        store_id (str):
        crypto_code (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningInvoiceData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            id=id,
            client=client,
        )
    ).parsed
