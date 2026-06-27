from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payout_data import PayoutData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pull_payment_id: str,
    *,
    include_cancelled: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeCancelled"] = include_cancelled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pull-payments/{pull_payment_id}/payouts".format(
            pull_payment_id=quote(str(pull_payment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[PayoutData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_payout_data_list_item_data in _response_200:
            componentsschemas_payout_data_list_item = PayoutData.from_dict(componentsschemas_payout_data_list_item_data)

            response_200.append(componentsschemas_payout_data_list_item)

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
) -> Response[Any | list[PayoutData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pull_payment_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_cancelled: bool | Unset = False,
) -> Response[Any | list[PayoutData]]:
    """Get Payouts

     Get payouts

    Args:
        pull_payment_id (str):
        include_cancelled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[PayoutData]]
    """

    kwargs = _get_kwargs(
        pull_payment_id=pull_payment_id,
        include_cancelled=include_cancelled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pull_payment_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_cancelled: bool | Unset = False,
) -> Any | list[PayoutData] | None:
    """Get Payouts

     Get payouts

    Args:
        pull_payment_id (str):
        include_cancelled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[PayoutData]
    """

    return sync_detailed(
        pull_payment_id=pull_payment_id,
        client=client,
        include_cancelled=include_cancelled,
    ).parsed


async def asyncio_detailed(
    pull_payment_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_cancelled: bool | Unset = False,
) -> Response[Any | list[PayoutData]]:
    """Get Payouts

     Get payouts

    Args:
        pull_payment_id (str):
        include_cancelled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[PayoutData]]
    """

    kwargs = _get_kwargs(
        pull_payment_id=pull_payment_id,
        include_cancelled=include_cancelled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pull_payment_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_cancelled: bool | Unset = False,
) -> Any | list[PayoutData] | None:
    """Get Payouts

     Get payouts

    Args:
        pull_payment_id (str):
        include_cancelled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[PayoutData]
    """

    return (
        await asyncio_detailed(
            pull_payment_id=pull_payment_id,
            client=client,
            include_cancelled=include_cancelled,
        )
    ).parsed
