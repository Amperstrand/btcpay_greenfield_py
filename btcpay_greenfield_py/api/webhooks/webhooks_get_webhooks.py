from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_data import WebhookData
from ...types import Response


def _get_kwargs(
    store_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/webhooks".format(
            store_id=quote(str(store_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[WebhookData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_webhook_data_list_item_data in _response_200:
            if isinstance(componentsschemas_webhook_data_list_item_data, dict):
                componentsschemas_webhook_data_list_item = WebhookData.from_dict(componentsschemas_webhook_data_list_item_data)
                response_200.append(componentsschemas_webhook_data_list_item)

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
) -> Response[Any | list[WebhookData]]:
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
) -> Response[Any | list[WebhookData]]:
    """Get webhooks of a store

     View webhooks of a store

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[WebhookData]]
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
) -> Any | list[WebhookData] | None:
    """Get webhooks of a store

     View webhooks of a store

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[WebhookData]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[WebhookData]]:
    """Get webhooks of a store

     View webhooks of a store

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[WebhookData]]
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
) -> Any | list[WebhookData] | None:
    """Get webhooks of a store

     View webhooks of a store

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[WebhookData]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
        )
    ).parsed
