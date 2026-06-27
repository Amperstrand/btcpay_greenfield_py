from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.store_rate_configuration import StoreRateConfiguration
from ...models.store_rate_result import StoreRateResult
from ...models.validation_problem_details_item import ValidationProblemDetailsItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: str,
    *,
    body: StoreRateConfiguration,
    currency_pair: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_currency_pair: list[str] | None | Unset
    if isinstance(currency_pair, Unset):
        json_currency_pair = UNSET
    elif isinstance(currency_pair, list):
        json_currency_pair = currency_pair

    else:
        json_currency_pair = currency_pair
    params["currencyPair"] = json_currency_pair

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/stores/{store_id}/rates/configuration/preview".format(
            store_id=quote(str(store_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[StoreRateResult] | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StoreRateResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for componentsschemas_validation_problem_details_item_data in _response_400:
            if isinstance(componentsschemas_validation_problem_details_item_data, dict):
                componentsschemas_validation_problem_details_item = ValidationProblemDetailsItem.from_dict(componentsschemas_validation_problem_details_item_data)
                response_400.append(componentsschemas_validation_problem_details_item)

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]]:
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
    body: StoreRateConfiguration,
    currency_pair: list[str] | None | Unset = UNSET,
) -> Response[Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]]:
    """Preview rate configuration results

     Preview rate configuration results before you set it on the store

    Args:
        store_id (str):
        currency_pair (list[str] | None | Unset):
        body (StoreRateConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        body=body,
        currency_pair=currency_pair,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
    body: StoreRateConfiguration,
    currency_pair: list[str] | None | Unset = UNSET,
) -> Any | list[StoreRateResult] | list[ValidationProblemDetailsItem] | None:
    """Preview rate configuration results

     Preview rate configuration results before you set it on the store

    Args:
        store_id (str):
        currency_pair (list[str] | None | Unset):
        body (StoreRateConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        body=body,
        currency_pair=currency_pair,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
    body: StoreRateConfiguration,
    currency_pair: list[str] | None | Unset = UNSET,
) -> Response[Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]]:
    """Preview rate configuration results

     Preview rate configuration results before you set it on the store

    Args:
        store_id (str):
        currency_pair (list[str] | None | Unset):
        body (StoreRateConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        body=body,
        currency_pair=currency_pair,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
    body: StoreRateConfiguration,
    currency_pair: list[str] | None | Unset = UNSET,
) -> Any | list[StoreRateResult] | list[ValidationProblemDetailsItem] | None:
    """Preview rate configuration results

     Preview rate configuration results before you set it on the store

    Args:
        store_id (str):
        currency_pair (list[str] | None | Unset):
        body (StoreRateConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[StoreRateResult] | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            body=body,
            currency_pair=currency_pair,
        )
    ).parsed
