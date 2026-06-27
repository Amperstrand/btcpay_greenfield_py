from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_point_of_sale_app_request import CreatePointOfSaleAppRequest
from ...models.point_of_sale_app_data import PointOfSaleAppData
from ...models.validation_problem_details_item import ValidationProblemDetailsItem
from ...types import Response


def _safe_from_dict(parser, response):
    if not response.content:
        return None
    try:
        return parser(response.json())
    except Exception:
        return None


def _get_kwargs(
    app_id: str,
    *,
    body: CreatePointOfSaleAppRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/apps/pos/{app_id}".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PointOfSaleAppData | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(PointOfSaleAppData.from_dict, response)

        return response_200

    if response.status_code == 422:
        response_422 = []
        _response_422 = response.json()
        for componentsschemas_validation_problem_details_item_data in _response_422:
            if isinstance(componentsschemas_validation_problem_details_item_data, dict):
                componentsschemas_validation_problem_details_item = ValidationProblemDetailsItem.from_dict(componentsschemas_validation_problem_details_item_data)
                response_422.append(componentsschemas_validation_problem_details_item)

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PointOfSaleAppData | list[ValidationProblemDetailsItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatePointOfSaleAppRequest,
) -> Response[PointOfSaleAppData | list[ValidationProblemDetailsItem]]:
    """Update a Point of Sale app

     Use this endpoint for updating the properties of a POS app

    Args:
        app_id (str):
        body (CreatePointOfSaleAppRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PointOfSaleAppData | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatePointOfSaleAppRequest,
) -> PointOfSaleAppData | list[ValidationProblemDetailsItem] | None:
    """Update a Point of Sale app

     Use this endpoint for updating the properties of a POS app

    Args:
        app_id (str):
        body (CreatePointOfSaleAppRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PointOfSaleAppData | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatePointOfSaleAppRequest,
) -> Response[PointOfSaleAppData | list[ValidationProblemDetailsItem]]:
    """Update a Point of Sale app

     Use this endpoint for updating the properties of a POS app

    Args:
        app_id (str):
        body (CreatePointOfSaleAppRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PointOfSaleAppData | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatePointOfSaleAppRequest,
) -> PointOfSaleAppData | list[ValidationProblemDetailsItem] | None:
    """Update a Point of Sale app

     Use this endpoint for updating the properties of a POS app

    Args:
        app_id (str):
        body (CreatePointOfSaleAppRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PointOfSaleAppData | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
