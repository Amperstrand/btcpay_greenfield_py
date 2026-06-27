from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pull_payment_data import PullPaymentData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: str,
    *,
    include_archived: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeArchived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/pull-payments".format(
            store_id=quote(str(store_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[PullPaymentData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_pull_payment_data_list_item_data in _response_200:
            if isinstance(componentsschemas_pull_payment_data_list_item_data, dict):
                componentsschemas_pull_payment_data_list_item = PullPaymentData.from_dict(componentsschemas_pull_payment_data_list_item_data)
                response_200.append(componentsschemas_pull_payment_data_list_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[PullPaymentData]]:
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
    include_archived: bool | Unset = False,
) -> Response[list[PullPaymentData]]:
    """Get store's pull payments

     Get the pull payments of a store

    Args:
        store_id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[PullPaymentData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
    include_archived: bool | Unset = False,
) -> list[PullPaymentData] | None:
    """Get store's pull payments

     Get the pull payments of a store

    Args:
        store_id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[PullPaymentData]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
    include_archived: bool | Unset = False,
) -> Response[list[PullPaymentData]]:
    """Get store's pull payments

     Get the pull payments of a store

    Args:
        store_id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[PullPaymentData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
    include_archived: bool | Unset = False,
) -> list[PullPaymentData] | None:
    """Get store's pull payments

     Get the pull payments of a store

    Args:
        store_id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[PullPaymentData]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            include_archived=include_archived,
        )
    ).parsed
