from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.application_user_data import ApplicationUserData
from ...models.users_create_user_body import UsersCreateUserBody
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
    *,
    body: UsersCreateUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApplicationUserData | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 201:
        response_201 = _safe_from_dict(ApplicationUserData.from_dict, response)

        return response_201

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for componentsschemas_validation_problem_details_item_data in _response_400:
            if isinstance(componentsschemas_validation_problem_details_item_data, dict):
                componentsschemas_validation_problem_details_item = ValidationProblemDetailsItem.from_dict(componentsschemas_validation_problem_details_item_data)
                response_400.append(componentsschemas_validation_problem_details_item)

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApplicationUserData | list[ValidationProblemDetailsItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UsersCreateUserBody,
) -> Response[Any | ApplicationUserData | list[ValidationProblemDetailsItem]]:
    """Create user

     Create a new user.

    This operation can be called without authentication in any of this cases:
    * There is not any administrator yet on the server,
    * The subscriptions are not disabled in the server's policies.

    If the first administrator is created by this call, subscriptions are automatically disabled.

    Args:
        body (UsersCreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApplicationUserData | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UsersCreateUserBody,
) -> Any | ApplicationUserData | list[ValidationProblemDetailsItem] | None:
    """Create user

     Create a new user.

    This operation can be called without authentication in any of this cases:
    * There is not any administrator yet on the server,
    * The subscriptions are not disabled in the server's policies.

    If the first administrator is created by this call, subscriptions are automatically disabled.

    Args:
        body (UsersCreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApplicationUserData | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UsersCreateUserBody,
) -> Response[Any | ApplicationUserData | list[ValidationProblemDetailsItem]]:
    """Create user

     Create a new user.

    This operation can be called without authentication in any of this cases:
    * There is not any administrator yet on the server,
    * The subscriptions are not disabled in the server's policies.

    If the first administrator is created by this call, subscriptions are automatically disabled.

    Args:
        body (UsersCreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApplicationUserData | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UsersCreateUserBody,
) -> Any | ApplicationUserData | list[ValidationProblemDetailsItem] | None:
    """Create user

     Create a new user.

    This operation can be called without authentication in any of this cases:
    * There is not any administrator yet on the server,
    * The subscriptions are not disabled in the server's policies.

    If the first administrator is created by this call, subscriptions are automatically disabled.

    Args:
        body (UsersCreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApplicationUserData | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
