from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_wallet_object_id import OnChainWalletObjectId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: str,
    crypto_code: str,
    *,
    type_: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    include_neighbour_data: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    params["includeNeighbourData"] = include_neighbour_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/onchain/{crypto_code}/wallet/objects".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[OnChainWalletObjectId] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OnChainWalletObjectId.from_dict(response_200_item_data)

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
) -> Response[Any | list[OnChainWalletObjectId]]:
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
    type_: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    include_neighbour_data: bool | Unset = True,
) -> Response[Any | list[OnChainWalletObjectId]]:
    """Get store on-chain wallet objects

     View wallet objects

    Args:
        store_id (str):
        crypto_code (str):
        type_ (str | Unset):
        ids (list[str] | Unset):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[OnChainWalletObjectId]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        type_=type_,
        ids=ids,
        include_neighbour_data=include_neighbour_data,
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
    type_: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    include_neighbour_data: bool | Unset = True,
) -> Any | list[OnChainWalletObjectId] | None:
    """Get store on-chain wallet objects

     View wallet objects

    Args:
        store_id (str):
        crypto_code (str):
        type_ (str | Unset):
        ids (list[str] | Unset):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[OnChainWalletObjectId]
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        client=client,
        type_=type_,
        ids=ids,
        include_neighbour_data=include_neighbour_data,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    include_neighbour_data: bool | Unset = True,
) -> Response[Any | list[OnChainWalletObjectId]]:
    """Get store on-chain wallet objects

     View wallet objects

    Args:
        store_id (str):
        crypto_code (str):
        type_ (str | Unset):
        ids (list[str] | Unset):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[OnChainWalletObjectId]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        type_=type_,
        ids=ids,
        include_neighbour_data=include_neighbour_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    include_neighbour_data: bool | Unset = True,
) -> Any | list[OnChainWalletObjectId] | None:
    """Get store on-chain wallet objects

     View wallet objects

    Args:
        store_id (str):
        crypto_code (str):
        type_ (str | Unset):
        ids (list[str] | Unset):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[OnChainWalletObjectId]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            client=client,
            type_=type_,
            ids=ids,
            include_neighbour_data=include_neighbour_data,
        )
    ).parsed
