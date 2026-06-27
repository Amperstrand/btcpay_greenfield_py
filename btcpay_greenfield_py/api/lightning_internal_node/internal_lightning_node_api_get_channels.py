from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lightning_channel_data import LightningChannelData
from ...types import Response


def _get_kwargs(
    crypto_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/server/lightning/{crypto_code}/channels".format(
            crypto_code=quote(str(crypto_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[LightningChannelData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LightningChannelData.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[LightningChannelData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[LightningChannelData]]:
    """Get channels

     View information about the current channels of the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[LightningChannelData]]
    """

    kwargs = _get_kwargs(
        crypto_code=crypto_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[LightningChannelData] | None:
    """Get channels

     View information about the current channels of the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[LightningChannelData]
    """

    return sync_detailed(
        crypto_code=crypto_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[LightningChannelData]]:
    """Get channels

     View information about the current channels of the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[LightningChannelData]]
    """

    kwargs = _get_kwargs(
        crypto_code=crypto_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[LightningChannelData] | None:
    """Get channels

     View information about the current channels of the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[LightningChannelData]
    """

    return (
        await asyncio_detailed(
            crypto_code=crypto_code,
            client=client,
        )
    ).parsed
