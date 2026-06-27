from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.quote_result_data import QuoteResultData
from ...types import UNSET, Response


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
    from_asset: str,
    to_asset: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fromAsset"] = from_asset

    params["toAsset"] = to_asset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/custodian-accounts/{account_id}/trades/quote".format(
            store_id=quote(str(store_id), safe=""),
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | QuoteResultData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(QuoteResultData.from_dict, response)

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
) -> Response[Any | QuoteResultData]:
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
    from_asset: str,
    to_asset: str,
) -> Response[Any | QuoteResultData]:
    """Get quote for trading one asset for another

     Get the current bid and ask price for converting one asset into another.

    Args:
        store_id (str):
        account_id (str):
        from_asset (str):
        to_asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | QuoteResultData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        from_asset=from_asset,
        to_asset=to_asset,
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
    from_asset: str,
    to_asset: str,
) -> Any | QuoteResultData | None:
    """Get quote for trading one asset for another

     Get the current bid and ask price for converting one asset into another.

    Args:
        store_id (str):
        account_id (str):
        from_asset (str):
        to_asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | QuoteResultData
    """

    return sync_detailed(
        store_id=store_id,
        account_id=account_id,
        client=client,
        from_asset=from_asset,
        to_asset=to_asset,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    from_asset: str,
    to_asset: str,
) -> Response[Any | QuoteResultData]:
    """Get quote for trading one asset for another

     Get the current bid and ask price for converting one asset into another.

    Args:
        store_id (str):
        account_id (str):
        from_asset (str):
        to_asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | QuoteResultData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        from_asset=from_asset,
        to_asset=to_asset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    from_asset: str,
    to_asset: str,
) -> Any | QuoteResultData | None:
    """Get quote for trading one asset for another

     Get the current bid and ask price for converting one asset into another.

    Args:
        store_id (str):
        account_id (str):
        from_asset (str):
        to_asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | QuoteResultData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            account_id=account_id,
            client=client,
            from_asset=from_asset,
            to_asset=to_asset,
        )
    ).parsed
