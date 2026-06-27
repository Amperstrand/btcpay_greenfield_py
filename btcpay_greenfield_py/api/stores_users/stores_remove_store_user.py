from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    store_id: str,
    id_or_email: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/stores/{store_id}/users/{id_or_email}".format(
            store_id=quote(str(store_id), safe=""),
            id_or_email=quote(str(id_or_email), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_409

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
    store_id: str,
    id_or_email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Remove Store User

     Removes the specified store user. If there is no other owner, this endpoint will fail.

    Args:
        store_id (str):
        id_or_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        id_or_email=id_or_email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    id_or_email: str,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Remove Store User

     Removes the specified store user. If there is no other owner, this endpoint will fail.

    Args:
        store_id (str):
        id_or_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        store_id=store_id,
        id_or_email=id_or_email,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    id_or_email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Remove Store User

     Removes the specified store user. If there is no other owner, this endpoint will fail.

    Args:
        store_id (str):
        id_or_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        id_or_email=id_or_email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    id_or_email: str,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Remove Store User

     Removes the specified store user. If there is no other owner, this endpoint will fail.

    Args:
        store_id (str):
        id_or_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            id_or_email=id_or_email,
            client=client,
        )
    ).parsed
