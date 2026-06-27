from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_lightning_channel_request import OpenLightningChannelRequest
from ...models.problem_details import ProblemDetails
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
    crypto_code: str,
    *,
    body: OpenLightningChannelRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/server/lightning/{crypto_code}/channels".format(
            crypto_code=quote(str(crypto_code), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

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
) -> Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: OpenLightningChannelRequest,
) -> Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Open channel

     Open a channel with another lightning node. You should connect to that node first.

    Args:
        crypto_code (str):
        body (OpenLightningChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        crypto_code=crypto_code,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: OpenLightningChannelRequest,
) -> Any | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Open channel

     Open a channel with another lightning node. You should connect to that node first.

    Args:
        crypto_code (str):
        body (OpenLightningChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        crypto_code=crypto_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: OpenLightningChannelRequest,
) -> Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Open channel

     Open a channel with another lightning node. You should connect to that node first.

    Args:
        crypto_code (str):
        body (OpenLightningChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        crypto_code=crypto_code,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: OpenLightningChannelRequest,
) -> Any | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Open channel

     Open a channel with another lightning node. You should connect to that node first.

    Args:
        crypto_code (str):
        body (OpenLightningChannelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            crypto_code=crypto_code,
            client=client,
            body=body,
        )
    ).parsed
