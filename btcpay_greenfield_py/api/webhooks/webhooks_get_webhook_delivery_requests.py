from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_get_webhook_delivery_requests_response_200 import WebhooksGetWebhookDeliveryRequestsResponse200
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
    webhook_id: str,
    delivery_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/webhooks/{webhook_id}/deliveries/{delivery_id}/request".format(
            store_id=quote(str(store_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | WebhooksGetWebhookDeliveryRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(WebhooksGetWebhookDeliveryRequestsResponse200.from_dict, response)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | WebhooksGetWebhookDeliveryRequestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | WebhooksGetWebhookDeliveryRequestsResponse200]:
    """Get the delivery's request

     The delivery's JSON request sent to the endpoint

    Args:
        store_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WebhooksGetWebhookDeliveryRequestsResponse200]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        webhook_id=webhook_id,
        delivery_id=delivery_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | WebhooksGetWebhookDeliveryRequestsResponse200 | None:
    """Get the delivery's request

     The delivery's JSON request sent to the endpoint

    Args:
        store_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WebhooksGetWebhookDeliveryRequestsResponse200
    """

    return sync_detailed(
        store_id=store_id,
        webhook_id=webhook_id,
        delivery_id=delivery_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | WebhooksGetWebhookDeliveryRequestsResponse200]:
    """Get the delivery's request

     The delivery's JSON request sent to the endpoint

    Args:
        store_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WebhooksGetWebhookDeliveryRequestsResponse200]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        webhook_id=webhook_id,
        delivery_id=delivery_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | WebhooksGetWebhookDeliveryRequestsResponse200 | None:
    """Get the delivery's request

     The delivery's JSON request sent to the endpoint

    Args:
        store_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WebhooksGetWebhookDeliveryRequestsResponse200
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            webhook_id=webhook_id,
            delivery_id=delivery_id,
            client=client,
        )
    ).parsed
