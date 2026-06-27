from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.withdrawal_result_data import WithdrawalResultData
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
    account_id: str,
    withdrawal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/custodian-accounts/{account_id}/withdrawals/{withdrawal_id}".format(
            store_id=quote(str(store_id), safe=""),
            account_id=quote(str(account_id), safe=""),
            withdrawal_id=quote(str(withdrawal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | WithdrawalResultData | str | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(WithdrawalResultData.from_dict, response)

        return response_200

    if response.status_code == 403:

        def _parse_response_403(data: object) -> str:
            return cast(str, data)

        response_403 = _parse_response_403(response.json())

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
) -> Response[Any | WithdrawalResultData | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    account_id: str,
    withdrawal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | WithdrawalResultData | str]:
    """Get withdrawal info

     Get the details about a past withdrawal.

    Args:
        store_id (str):
        account_id (str):
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WithdrawalResultData | str]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        withdrawal_id=withdrawal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    account_id: str,
    withdrawal_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | WithdrawalResultData | str | None:
    """Get withdrawal info

     Get the details about a past withdrawal.

    Args:
        store_id (str):
        account_id (str):
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WithdrawalResultData | str
    """

    return sync_detailed(
        store_id=store_id,
        account_id=account_id,
        withdrawal_id=withdrawal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    account_id: str,
    withdrawal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | WithdrawalResultData | str]:
    """Get withdrawal info

     Get the details about a past withdrawal.

    Args:
        store_id (str):
        account_id (str):
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WithdrawalResultData | str]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        withdrawal_id=withdrawal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    account_id: str,
    withdrawal_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | WithdrawalResultData | str | None:
    """Get withdrawal info

     Get the details about a past withdrawal.

    Args:
        store_id (str):
        account_id (str):
        withdrawal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WithdrawalResultData | str
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            account_id=account_id,
            withdrawal_id=withdrawal_id,
            client=client,
        )
    ).parsed
