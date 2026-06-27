from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_data import NotificationData
from ...types import UNSET, Response, Unset


def _safe_from_dict(parser, response):
    if not response.content:
        return None
    try:
        return parser(response.json())
    except Exception:
        return None


def _get_kwargs(
    *,
    seen: None | str | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_seen: None | str | Unset
    if isinstance(seen, Unset):
        json_seen = UNSET
    else:
        json_seen = seen
    params["seen"] = json_seen

    json_skip: float | None | Unset
    if isinstance(skip, Unset):
        json_skip = UNSET
    else:
        json_skip = skip
    params["skip"] = json_skip

    json_take: float | None | Unset
    if isinstance(take, Unset):
        json_take = UNSET
    else:
        json_take = take
    params["take"] = json_take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/me/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> NotificationData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(NotificationData.from_dict, response)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[NotificationData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    seen: None | str | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> Response[NotificationData]:
    """Get notifications

     View current user's notifications

    Args:
        seen (None | str | Unset):
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationData]
    """

    kwargs = _get_kwargs(
        seen=seen,
        skip=skip,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    seen: None | str | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> NotificationData | None:
    """Get notifications

     View current user's notifications

    Args:
        seen (None | str | Unset):
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationData
    """

    return sync_detailed(
        client=client,
        seen=seen,
        skip=skip,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    seen: None | str | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> Response[NotificationData]:
    """Get notifications

     View current user's notifications

    Args:
        seen (None | str | Unset):
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationData]
    """

    kwargs = _get_kwargs(
        seen=seen,
        skip=skip,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    seen: None | str | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> NotificationData | None:
    """Get notifications

     View current user's notifications

    Args:
        seen (None | str | Unset):
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationData
    """

    return (
        await asyncio_detailed(
            client=client,
            seen=seen,
            skip=skip,
            take=take,
        )
    ).parsed
