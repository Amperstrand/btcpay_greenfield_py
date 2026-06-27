from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_payment_method_preview_result_data import OnChainPaymentMethodPreviewResultData
from ...types import UNSET, Response, Unset


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
    *,
    offset: float | Unset = UNSET,
    amount: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["amount"] = amount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/OnChain/{crypto_code}/preview".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OnChainPaymentMethodPreviewResultData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(OnChainPaymentMethodPreviewResultData.from_dict, response)

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
) -> Response[Any | OnChainPaymentMethodPreviewResultData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    offset: float | Unset = UNSET,
    amount: float | Unset = UNSET,
) -> Response[Any | OnChainPaymentMethodPreviewResultData]:
    """Preview store on-chain payment method addresses

     View addresses of the current payment method of the store

    Args:
        store_id (str):
        crypto_code (str):
        offset (float | Unset):
        amount (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainPaymentMethodPreviewResultData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        offset=offset,
        amount=amount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    offset: float | Unset = UNSET,
    amount: float | Unset = UNSET,
) -> Any | OnChainPaymentMethodPreviewResultData | None:
    """Preview store on-chain payment method addresses

     View addresses of the current payment method of the store

    Args:
        store_id (str):
        crypto_code (str):
        offset (float | Unset):
        amount (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainPaymentMethodPreviewResultData
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        client=client,
        offset=offset,
        amount=amount,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    offset: float | Unset = UNSET,
    amount: float | Unset = UNSET,
) -> Response[Any | OnChainPaymentMethodPreviewResultData]:
    """Preview store on-chain payment method addresses

     View addresses of the current payment method of the store

    Args:
        store_id (str):
        crypto_code (str):
        offset (float | Unset):
        amount (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainPaymentMethodPreviewResultData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        offset=offset,
        amount=amount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    offset: float | Unset = UNSET,
    amount: float | Unset = UNSET,
) -> Any | OnChainPaymentMethodPreviewResultData | None:
    """Preview store on-chain payment method addresses

     View addresses of the current payment method of the store

    Args:
        store_id (str):
        crypto_code (str):
        offset (float | Unset):
        amount (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainPaymentMethodPreviewResultData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            client=client,
            offset=offset,
            amount=amount,
        )
    ).parsed
