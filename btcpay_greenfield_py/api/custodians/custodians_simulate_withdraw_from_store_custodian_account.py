from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.withdrawal_request_data import WithdrawalRequestData
from ...models.withdrawal_simulation_result_data import WithdrawalSimulationResultData
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
    body: WithdrawalRequestData,
    payment_method: str,
    qty: float,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["paymentMethod"] = payment_method

    params["qty"] = qty

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/stores/{store_id}/custodian-accounts/{account_id}/withdrawals/simulation".format(
            store_id=quote(str(store_id), safe=""),
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | WithdrawalSimulationResultData | str | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(WithdrawalSimulationResultData.from_dict, response)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | WithdrawalSimulationResultData | str]:
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
    body: WithdrawalRequestData,
    payment_method: str,
    qty: float,
) -> Response[Any | WithdrawalSimulationResultData | str]:
    """Simulate a withdrawal

     Get more information about a potential withdrawal including fees, minimum and maximum quantities for
    the given asset and quantity.

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):
        qty (float):
        body (WithdrawalRequestData):  Example: {'paymentMethod': 'BTC-OnChain', 'qty':
            '0.123456'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WithdrawalSimulationResultData | str]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        body=body,
        payment_method=payment_method,
        qty=qty,
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
    body: WithdrawalRequestData,
    payment_method: str,
    qty: float,
) -> Any | WithdrawalSimulationResultData | str | None:
    """Simulate a withdrawal

     Get more information about a potential withdrawal including fees, minimum and maximum quantities for
    the given asset and quantity.

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):
        qty (float):
        body (WithdrawalRequestData):  Example: {'paymentMethod': 'BTC-OnChain', 'qty':
            '0.123456'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WithdrawalSimulationResultData | str
    """

    return sync_detailed(
        store_id=store_id,
        account_id=account_id,
        client=client,
        body=body,
        payment_method=payment_method,
        qty=qty,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: WithdrawalRequestData,
    payment_method: str,
    qty: float,
) -> Response[Any | WithdrawalSimulationResultData | str]:
    """Simulate a withdrawal

     Get more information about a potential withdrawal including fees, minimum and maximum quantities for
    the given asset and quantity.

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):
        qty (float):
        body (WithdrawalRequestData):  Example: {'paymentMethod': 'BTC-OnChain', 'qty':
            '0.123456'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WithdrawalSimulationResultData | str]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        account_id=account_id,
        body=body,
        payment_method=payment_method,
        qty=qty,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: WithdrawalRequestData,
    payment_method: str,
    qty: float,
) -> Any | WithdrawalSimulationResultData | str | None:
    """Simulate a withdrawal

     Get more information about a potential withdrawal including fees, minimum and maximum quantities for
    the given asset and quantity.

    Args:
        store_id (str):
        account_id (str):
        payment_method (str):
        qty (float):
        body (WithdrawalRequestData):  Example: {'paymentMethod': 'BTC-OnChain', 'qty':
            '0.123456'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WithdrawalSimulationResultData | str
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            account_id=account_id,
            client=client,
            body=body,
            payment_method=payment_method,
            qty=qty,
        )
    ).parsed
