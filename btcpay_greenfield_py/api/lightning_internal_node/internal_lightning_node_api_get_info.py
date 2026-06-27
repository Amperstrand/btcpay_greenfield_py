from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lightning_node_information_data import LightningNodeInformationData
from ...types import Response


def _safe_from_dict(parser, response):
    if not response.content:
        return None
    try:
        return parser(response.json())
    except Exception:
        return None


def _get_kwargs(
    crypto_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/server/lightning/{crypto_code}/info".format(
            crypto_code=quote(str(crypto_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LightningNodeInformationData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(LightningNodeInformationData.from_dict, response)

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
) -> Response[Any | LightningNodeInformationData]:
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
) -> Response[Any | LightningNodeInformationData]:
    """Get node information

     View information about the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningNodeInformationData]
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
) -> Any | LightningNodeInformationData | None:
    """Get node information

     View information about the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningNodeInformationData
    """

    return sync_detailed(
        crypto_code=crypto_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | LightningNodeInformationData]:
    """Get node information

     View information about the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningNodeInformationData]
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
) -> Any | LightningNodeInformationData | None:
    """Get node information

     View information about the lightning node

    Args:
        crypto_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningNodeInformationData
    """

    return (
        await asyncio_detailed(
            crypto_code=crypto_code,
            client=client,
        )
    ).parsed
