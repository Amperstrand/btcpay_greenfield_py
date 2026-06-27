from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    permissions: list[str] | None | Unset = UNSET,
    application_name: None | str | Unset = UNSET,
    strict: bool | None | Unset = True,
    selective_stores: bool | None | Unset = False,
    redirect: None | str | Unset = UNSET,
    application_identifier: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_permissions: list[str] | None | Unset
    if isinstance(permissions, Unset):
        json_permissions = UNSET
    elif isinstance(permissions, list):
        json_permissions = permissions

    else:
        json_permissions = permissions
    params["permissions"] = json_permissions

    json_application_name: None | str | Unset
    if isinstance(application_name, Unset):
        json_application_name = UNSET
    else:
        json_application_name = application_name
    params["applicationName"] = json_application_name

    json_strict: bool | None | Unset
    if isinstance(strict, Unset):
        json_strict = UNSET
    else:
        json_strict = strict
    params["strict"] = json_strict

    json_selective_stores: bool | None | Unset
    if isinstance(selective_stores, Unset):
        json_selective_stores = UNSET
    else:
        json_selective_stores = selective_stores
    params["selectiveStores"] = json_selective_stores

    json_redirect: None | str | Unset
    if isinstance(redirect, Unset):
        json_redirect = UNSET
    else:
        json_redirect = redirect
    params["redirect"] = json_redirect

    json_application_identifier: None | str | Unset
    if isinstance(application_identifier, Unset):
        json_application_identifier = UNSET
    else:
        json_application_identifier = application_identifier
    params["applicationIdentifier"] = json_application_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api-keys/authorize",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 307:
        return None

    if response.status_code == 401:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    permissions: list[str] | None | Unset = UNSET,
    application_name: None | str | Unset = UNSET,
    strict: bool | None | Unset = True,
    selective_stores: bool | None | Unset = False,
    redirect: None | str | Unset = UNSET,
    application_identifier: None | str | Unset = UNSET,
) -> Response[Any]:
    """Authorize User

     Redirect the browser to this endpoint to request the user to generate an api-key with specific
    permissions

    Args:
        permissions (list[str] | None | Unset):
        application_name (None | str | Unset):
        strict (bool | None | Unset):  Default: True.
        selective_stores (bool | None | Unset):  Default: False.
        redirect (None | str | Unset):
        application_identifier (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        permissions=permissions,
        application_name=application_name,
        strict=strict,
        selective_stores=selective_stores,
        redirect=redirect,
        application_identifier=application_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    permissions: list[str] | None | Unset = UNSET,
    application_name: None | str | Unset = UNSET,
    strict: bool | None | Unset = True,
    selective_stores: bool | None | Unset = False,
    redirect: None | str | Unset = UNSET,
    application_identifier: None | str | Unset = UNSET,
) -> Response[Any]:
    """Authorize User

     Redirect the browser to this endpoint to request the user to generate an api-key with specific
    permissions

    Args:
        permissions (list[str] | None | Unset):
        application_name (None | str | Unset):
        strict (bool | None | Unset):  Default: True.
        selective_stores (bool | None | Unset):  Default: False.
        redirect (None | str | Unset):
        application_identifier (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        permissions=permissions,
        application_name=application_name,
        strict=strict,
        selective_stores=selective_stores,
        redirect=redirect,
        application_identifier=application_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
