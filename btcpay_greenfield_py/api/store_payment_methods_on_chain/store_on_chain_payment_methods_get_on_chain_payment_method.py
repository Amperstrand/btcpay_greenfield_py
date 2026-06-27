from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_payment_method_data import OnChainPaymentMethodData
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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/onchain/{crypto_code}".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OnChainPaymentMethodData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(OnChainPaymentMethodData.from_dict, response)

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
) -> Response[Any | OnChainPaymentMethodData]:
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
) -> Response[Any | OnChainPaymentMethodData]:
    """Get store on-chain payment method

     View information about the specified payment method

    Args:
        store_id (str):
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainPaymentMethodData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
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
) -> Any | OnChainPaymentMethodData | None:
    """Get store on-chain payment method

     View information about the specified payment method

    Args:
        store_id (str):
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainPaymentMethodData
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OnChainPaymentMethodData]:
    """Get store on-chain payment method

     View information about the specified payment method

    Args:
        store_id (str):
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainPaymentMethodData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Any | OnChainPaymentMethodData | None:
    """Get store on-chain payment method

     View information about the specified payment method

    Args:
        store_id (str):
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainPaymentMethodData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            client=client,
        )
    ).parsed
