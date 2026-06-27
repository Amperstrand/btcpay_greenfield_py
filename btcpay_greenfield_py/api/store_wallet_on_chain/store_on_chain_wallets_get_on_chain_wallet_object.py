from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_wallet_object_id import OnChainWalletObjectId
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
    object_type: str,
    object_id: str,
    *,
    include_neighbour_data: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeNeighbourData"] = include_neighbour_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/onchain/{crypto_code}/wallet/objects/{object_type}/{object_id}".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OnChainWalletObjectId | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(OnChainWalletObjectId.from_dict, response)

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
) -> Response[Any | OnChainWalletObjectId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    crypto_code: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient,
    include_neighbour_data: bool | Unset = True,
) -> Response[Any | OnChainWalletObjectId]:
    """Get store on-chain wallet object

     View wallet object

    Args:
        store_id (str):
        crypto_code (str):
        object_type (str):
        object_id (str):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainWalletObjectId]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        object_type=object_type,
        object_id=object_id,
        include_neighbour_data=include_neighbour_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    crypto_code: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient,
    include_neighbour_data: bool | Unset = True,
) -> Any | OnChainWalletObjectId | None:
    """Get store on-chain wallet object

     View wallet object

    Args:
        store_id (str):
        crypto_code (str):
        object_type (str):
        object_id (str):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainWalletObjectId
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        object_type=object_type,
        object_id=object_id,
        client=client,
        include_neighbour_data=include_neighbour_data,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient,
    include_neighbour_data: bool | Unset = True,
) -> Response[Any | OnChainWalletObjectId]:
    """Get store on-chain wallet object

     View wallet object

    Args:
        store_id (str):
        crypto_code (str):
        object_type (str):
        object_id (str):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OnChainWalletObjectId]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        object_type=object_type,
        object_id=object_id,
        include_neighbour_data=include_neighbour_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient,
    include_neighbour_data: bool | Unset = True,
) -> Any | OnChainWalletObjectId | None:
    """Get store on-chain wallet object

     View wallet object

    Args:
        store_id (str):
        crypto_code (str):
        object_type (str):
        object_id (str):
        include_neighbour_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OnChainWalletObjectId
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            object_type=object_type,
            object_id=object_id,
            client=client,
            include_neighbour_data=include_neighbour_data,
        )
    ).parsed
