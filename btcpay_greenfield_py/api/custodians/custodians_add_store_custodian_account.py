from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custodian_account_request import CreateCustodianAccountRequest
from ...models.custodian_account_data import CustodianAccountData
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
    *,
    body: CreateCustodianAccountRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/stores/{store_id}/custodian-accounts".format(
            store_id=quote(str(store_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CustodianAccountData | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(CustodianAccountData.from_dict, response)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CustodianAccountData]:
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
    body: CreateCustodianAccountRequest,
) -> Response[Any | CustodianAccountData]:
    """Add a custodial account to a store.

     Add a custodial account to a store.

    Args:
        store_id (str):
        body (CreateCustodianAccountRequest):  Example: {'accountId': 'xxxxxxxxxxxxxxx',
            'storeId': 'xxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'name': 'My Kraken Account',
            'config': {'WithdrawToAddressNamePerPaymentMethod': {'BTC-OnChain': 'My Ledger Nano'},
            'ApiKey': 'xxx', 'PrivateKey': 'xxx'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustodianAccountData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateCustodianAccountRequest,
) -> Any | CustodianAccountData | None:
    """Add a custodial account to a store.

     Add a custodial account to a store.

    Args:
        store_id (str):
        body (CreateCustodianAccountRequest):  Example: {'accountId': 'xxxxxxxxxxxxxxx',
            'storeId': 'xxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'name': 'My Kraken Account',
            'config': {'WithdrawToAddressNamePerPaymentMethod': {'BTC-OnChain': 'My Ledger Nano'},
            'ApiKey': 'xxx', 'PrivateKey': 'xxx'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustodianAccountData
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateCustodianAccountRequest,
) -> Response[Any | CustodianAccountData]:
    """Add a custodial account to a store.

     Add a custodial account to a store.

    Args:
        store_id (str):
        body (CreateCustodianAccountRequest):  Example: {'accountId': 'xxxxxxxxxxxxxxx',
            'storeId': 'xxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'name': 'My Kraken Account',
            'config': {'WithdrawToAddressNamePerPaymentMethod': {'BTC-OnChain': 'My Ledger Nano'},
            'ApiKey': 'xxx', 'PrivateKey': 'xxx'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustodianAccountData]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateCustodianAccountRequest,
) -> Any | CustodianAccountData | None:
    """Add a custodial account to a store.

     Add a custodial account to a store.

    Args:
        store_id (str):
        body (CreateCustodianAccountRequest):  Example: {'accountId': 'xxxxxxxxxxxxxxx',
            'storeId': 'xxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'name': 'My Kraken Account',
            'config': {'WithdrawToAddressNamePerPaymentMethod': {'BTC-OnChain': 'My Ledger Nano'},
            'ApiKey': 'xxx', 'PrivateKey': 'xxx'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustodianAccountData
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            body=body,
        )
    ).parsed
