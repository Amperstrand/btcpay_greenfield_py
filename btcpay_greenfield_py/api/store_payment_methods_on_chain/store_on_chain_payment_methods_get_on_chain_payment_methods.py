from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.on_chain_payment_method_data import OnChainPaymentMethodData
from ...models.problem_details import ProblemDetails
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
    *,
    enabled: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["enabled"] = enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-methods/OnChain".format(
            store_id=quote(str(store_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | list[OnChainPaymentMethodData]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_on_chain_payment_method_data_list_item_data in _response_200:
            if isinstance(componentsschemas_on_chain_payment_method_data_list_item_data, dict):
                componentsschemas_on_chain_payment_method_data_list_item = OnChainPaymentMethodData.from_dict(componentsschemas_on_chain_payment_method_data_list_item_data)
                response_200.append(componentsschemas_on_chain_payment_method_data_list_item)

        return response_200

    if response.status_code == 401:
        response_401 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_401

    response_default = _safe_from_dict(ProblemDetails.from_dict, response)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | list[OnChainPaymentMethodData]]:
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
    enabled: bool | Unset = UNSET,
) -> Response[ProblemDetails | list[OnChainPaymentMethodData]]:
    """Get store on-chain payment methods

     View information about the stores' configured on-chain payment methods

    Args:
        store_id (str):
        enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[OnChainPaymentMethodData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        enabled=enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
    enabled: bool | Unset = UNSET,
) -> ProblemDetails | list[OnChainPaymentMethodData] | None:
    """Get store on-chain payment methods

     View information about the stores' configured on-chain payment methods

    Args:
        store_id (str):
        enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[OnChainPaymentMethodData]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        enabled=enabled,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
    enabled: bool | Unset = UNSET,
) -> Response[ProblemDetails | list[OnChainPaymentMethodData]]:
    """Get store on-chain payment methods

     View information about the stores' configured on-chain payment methods

    Args:
        store_id (str):
        enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[OnChainPaymentMethodData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        enabled=enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
    enabled: bool | Unset = UNSET,
) -> ProblemDetails | list[OnChainPaymentMethodData] | None:
    """Get store on-chain payment methods

     View information about the stores' configured on-chain payment methods

    Args:
        store_id (str):
        enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[OnChainPaymentMethodData]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            enabled=enabled,
        )
    ).parsed
