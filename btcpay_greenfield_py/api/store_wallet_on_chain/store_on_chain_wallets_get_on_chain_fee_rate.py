from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_wallet_fee_rate_data import OnChainWalletFeeRateData
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
    block_target: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["blockTarget"] = block_target

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/onchain/{crypto_code}/wallet/feerate".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OnChainWalletFeeRateData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(OnChainWalletFeeRateData.from_dict, response)

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
) -> Response[Any | OnChainWalletFeeRateData]:
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
    block_target: float | Unset = UNSET,
) -> Response[Any | OnChainWalletFeeRateData]:
    """Get store on-chain wallet fee rate

     Get wallet onchain fee rate

    Args:
        store_id (str):
        crypto_code (str):
        block_target (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainWalletFeeRateData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        block_target=block_target,
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
    block_target: float | Unset = UNSET,
) -> Any | OnChainWalletFeeRateData | None:
    """Get store on-chain wallet fee rate

     Get wallet onchain fee rate

    Args:
        store_id (str):
        crypto_code (str):
        block_target (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainWalletFeeRateData
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        client=client,
        block_target=block_target,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    block_target: float | Unset = UNSET,
) -> Response[Any | OnChainWalletFeeRateData]:
    """Get store on-chain wallet fee rate

     Get wallet onchain fee rate

    Args:
        store_id (str):
        crypto_code (str):
        block_target (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainWalletFeeRateData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        block_target=block_target,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    block_target: float | Unset = UNSET,
) -> Any | OnChainWalletFeeRateData | None:
    """Get store on-chain wallet fee rate

     Get wallet onchain fee rate

    Args:
        store_id (str):
        crypto_code (str):
        block_target (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainWalletFeeRateData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            client=client,
            block_target=block_target,
        )
    ).parsed
