from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.on_chain_automated_transfer_settings import OnChainAutomatedTransferSettings
from ...types import Response


def _get_kwargs(
    store_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payout-processors/OnChainAutomatedTransferSenderFactory".format(
            store_id=quote(str(store_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[OnChainAutomatedTransferSettings] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OnChainAutomatedTransferSettings.from_dict(response_200_item_data)

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
) -> Response[Any | list[OnChainAutomatedTransferSettings]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[OnChainAutomatedTransferSettings]]:
    """Get configured store onchain automated payout processors

     Get configured store onchain automated payout processors

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[OnChainAutomatedTransferSettings]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[OnChainAutomatedTransferSettings] | None:
    """Get configured store onchain automated payout processors

     Get configured store onchain automated payout processors

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[OnChainAutomatedTransferSettings]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[OnChainAutomatedTransferSettings]]:
    """Get configured store onchain automated payout processors

     Get configured store onchain automated payout processors

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[OnChainAutomatedTransferSettings]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[OnChainAutomatedTransferSettings] | None:
    """Get configured store onchain automated payout processors

     Get configured store onchain automated payout processors

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[OnChainAutomatedTransferSettings]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
        )
    ).parsed
