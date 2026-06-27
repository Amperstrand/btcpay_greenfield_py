from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custodians_get_store_custodian_account_deposit_address_response_200 import (
    CustodiansGetStoreCustodianAccountDepositAddressResponse200,
)
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
    payment_method: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/custodian-accounts/{account_id}/addresses/{payment_method}".format(
            store_id=quote(str(store_id), safe=""),
            account_id=quote(str(account_id), safe=""),
            payment_method=quote(str(payment_method), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200 | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(CustodiansGetStoreCustodianAccountDepositAddressResponse200.from_dict, response)

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
) -> Response[Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    account_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200]:
    """Get a deposit address for custodian

     Get a new deposit address for the custodian using the specified payment method (network + crypto
    code).

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        payment_method=payment_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    account_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
) -> Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200 | None:
    """Get a deposit address for custodian

     Get a new deposit address for the custodian using the specified payment method (network + crypto
    code).

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200
    """

    return sync_detailed(
        store_id=store_id,
        account_id=account_id,
        payment_method=payment_method,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    account_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200]:
    """Get a deposit address for custodian

     Get a new deposit address for the custodian using the specified payment method (network + crypto
    code).

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        payment_method=payment_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    account_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
) -> Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200 | None:
    """Get a deposit address for custodian

     Get a new deposit address for the custodian using the specified payment method (network + crypto
    code).

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustodiansGetStoreCustodianAccountDepositAddressResponse200
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            account_id=account_id,
            payment_method=payment_method,
            client=client,
        )
    ).parsed
