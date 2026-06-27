from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trade_request_data import TradeRequestData
from ...models.trade_result_data import TradeResultData
from ...types import UNSET, Response, Unset


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
    *,
    body: TradeRequestData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/stores/{store_id}/custodian-accounts/{account_id}/trades/market".format(
            store_id=quote(str(store_id), safe=""),
            account_id=quote(str(account_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | TradeResultData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(TradeResultData.from_dict, response)

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
) -> Response[Any | TradeResultData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: TradeRequestData | Unset = UNSET,
) -> Response[Any | TradeResultData]:
    """Trade one asset for another

     Trade one asset for another using a market order (=instant purchase with instant result or failure).
    A suitable asset pair will automatically be selected. If no asset pair is available, the call will
    fail.

    Args:
        store_id (str):
        account_id (str):
        body (TradeRequestData | Unset):  Example: {'fromAsset': 'USD', 'toAsset': 'BTC', 'qty':
            '50%'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TradeResultData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: TradeRequestData | Unset = UNSET,
) -> Any | TradeResultData | None:
    """Trade one asset for another

     Trade one asset for another using a market order (=instant purchase with instant result or failure).
    A suitable asset pair will automatically be selected. If no asset pair is available, the call will
    fail.

    Args:
        store_id (str):
        account_id (str):
        body (TradeRequestData | Unset):  Example: {'fromAsset': 'USD', 'toAsset': 'BTC', 'qty':
            '50%'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TradeResultData
    """

    return sync_detailed(
        store_id=store_id,
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: TradeRequestData | Unset = UNSET,
) -> Response[Any | TradeResultData]:
    """Trade one asset for another

     Trade one asset for another using a market order (=instant purchase with instant result or failure).
    A suitable asset pair will automatically be selected. If no asset pair is available, the call will
    fail.

    Args:
        store_id (str):
        account_id (str):
        body (TradeRequestData | Unset):  Example: {'fromAsset': 'USD', 'toAsset': 'BTC', 'qty':
            '50%'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TradeResultData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: TradeRequestData | Unset = UNSET,
) -> Any | TradeResultData | None:
    """Trade one asset for another

     Trade one asset for another using a market order (=instant purchase with instant result or failure).
    A suitable asset pair will automatically be selected. If no asset pair is available, the call will
    fail.

    Args:
        store_id (str):
        account_id (str):
        body (TradeRequestData | Unset):  Example: {'fromAsset': 'USD', 'toAsset': 'BTC', 'qty':
            '50%'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TradeResultData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
