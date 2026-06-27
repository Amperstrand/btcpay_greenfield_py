from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payout_data import PayoutData
from ...types import Response


def _safe_from_dict(parser, response):
    if not response.content:
        return None
    try:
        return parser(response.json())
    except Exception:
        return None


def _get_kwargs(
    pull_payment_id: str,
    payout_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pull-payments/{pull_payment_id}/payouts/{payout_id}".format(
            pull_payment_id=quote(str(pull_payment_id), safe=""),
            payout_id=quote(str(payout_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PayoutData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(PayoutData.from_dict, response)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PayoutData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pull_payment_id: str,
    payout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PayoutData]:
    """Get Payout

     Get payout

    Args:
        pull_payment_id (str):
        payout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PayoutData]
    """

    kwargs = _get_kwargs(
        pull_payment_id=pull_payment_id,
        payout_id=payout_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pull_payment_id: str,
    payout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PayoutData | None:
    """Get Payout

     Get payout

    Args:
        pull_payment_id (str):
        payout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PayoutData
    """

    return sync_detailed(
        pull_payment_id=pull_payment_id,
        payout_id=payout_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pull_payment_id: str,
    payout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PayoutData]:
    """Get Payout

     Get payout

    Args:
        pull_payment_id (str):
        payout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PayoutData]
    """

    kwargs = _get_kwargs(
        pull_payment_id=pull_payment_id,
        payout_id=payout_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pull_payment_id: str,
    payout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PayoutData | None:
    """Get Payout

     Get payout

    Args:
        pull_payment_id (str):
        payout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PayoutData
    """

    return (
        await asyncio_detailed(
            pull_payment_id=pull_payment_id,
            payout_id=payout_id,
            client=client,
        )
    ).parsed
