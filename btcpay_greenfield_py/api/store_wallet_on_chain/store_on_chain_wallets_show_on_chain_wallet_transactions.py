from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_wallet_transaction_data import OnChainWalletTransactionData
from ...models.transaction_status import TransactionStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: str,
    crypto_code: str,
    *,
    status_filter: list[TransactionStatus] | Unset = UNSET,
    label_filter: str | Unset = UNSET,
    skip: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status_filter: list[str] | Unset = UNSET
    if not isinstance(status_filter, Unset):
        json_status_filter = []
        for status_filter_item_data in status_filter:
            status_filter_item = status_filter_item_data.value
            json_status_filter.append(status_filter_item)

    params["statusFilter"] = json_status_filter

    params["labelFilter"] = label_filter

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/onchain/{crypto_code}/wallet/transactions".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[OnChainWalletTransactionData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OnChainWalletTransactionData.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
) -> Response[Any | list[OnChainWalletTransactionData]]:
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
    status_filter: list[TransactionStatus] | Unset = UNSET,
    label_filter: str | Unset = UNSET,
    skip: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Any | list[OnChainWalletTransactionData]]:
    """Get store on-chain wallet transactions

     Get store on-chain wallet transactions

    Args:
        store_id (str):
        crypto_code (str):
        status_filter (list[TransactionStatus] | Unset):
        label_filter (str | Unset):
        skip (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[OnChainWalletTransactionData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        status_filter=status_filter,
        label_filter=label_filter,
        skip=skip,
        limit=limit,
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
    status_filter: list[TransactionStatus] | Unset = UNSET,
    label_filter: str | Unset = UNSET,
    skip: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Any | list[OnChainWalletTransactionData] | None:
    """Get store on-chain wallet transactions

     Get store on-chain wallet transactions

    Args:
        store_id (str):
        crypto_code (str):
        status_filter (list[TransactionStatus] | Unset):
        label_filter (str | Unset):
        skip (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[OnChainWalletTransactionData]
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        client=client,
        status_filter=status_filter,
        label_filter=label_filter,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    status_filter: list[TransactionStatus] | Unset = UNSET,
    label_filter: str | Unset = UNSET,
    skip: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Any | list[OnChainWalletTransactionData]]:
    """Get store on-chain wallet transactions

     Get store on-chain wallet transactions

    Args:
        store_id (str):
        crypto_code (str):
        status_filter (list[TransactionStatus] | Unset):
        label_filter (str | Unset):
        skip (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[OnChainWalletTransactionData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        status_filter=status_filter,
        label_filter=label_filter,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    status_filter: list[TransactionStatus] | Unset = UNSET,
    label_filter: str | Unset = UNSET,
    skip: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Any | list[OnChainWalletTransactionData] | None:
    """Get store on-chain wallet transactions

     Get store on-chain wallet transactions

    Args:
        store_id (str):
        crypto_code (str):
        status_filter (list[TransactionStatus] | Unset):
        label_filter (str | Unset):
        skip (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[OnChainWalletTransactionData]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            client=client,
            status_filter=status_filter,
            label_filter=label_filter,
            skip=skip,
            limit=limit,
        )
    ).parsed
