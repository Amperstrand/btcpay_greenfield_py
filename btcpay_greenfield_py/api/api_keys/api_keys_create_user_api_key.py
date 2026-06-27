from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_key_data import ApiKeyData
from ...models.api_keys_create_user_api_key_body import ApiKeysCreateUserApiKeyBody
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
    id_or_email: str,
    *,
    body: ApiKeysCreateUserApiKeyBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/users/{id_or_email}/api-keys".format(
            id_or_email=quote(str(id_or_email), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiKeyData | ProblemDetails:
    if response.status_code == 200:
        response_200 = _safe_from_dict(ApiKeyData.from_dict, response)

        return response_200

    if response.status_code == 401:
        response_401 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_401

    response_default = _safe_from_dict(ProblemDetails.from_dict, response)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKeyData | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_or_email: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeysCreateUserApiKeyBody | Unset = UNSET,
) -> Response[ApiKeyData | ProblemDetails]:
    """Create a new API Key for a user

     Create a new API Key for a user

    Args:
        id_or_email (str):
        body (ApiKeysCreateUserApiKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyData | ProblemDetails]
    """

    kwargs = _get_kwargs(
        id_or_email=id_or_email,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_or_email: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeysCreateUserApiKeyBody | Unset = UNSET,
) -> ApiKeyData | ProblemDetails | None:
    """Create a new API Key for a user

     Create a new API Key for a user

    Args:
        id_or_email (str):
        body (ApiKeysCreateUserApiKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyData | ProblemDetails
    """

    return sync_detailed(
        id_or_email=id_or_email,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id_or_email: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeysCreateUserApiKeyBody | Unset = UNSET,
) -> Response[ApiKeyData | ProblemDetails]:
    """Create a new API Key for a user

     Create a new API Key for a user

    Args:
        id_or_email (str):
        body (ApiKeysCreateUserApiKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyData | ProblemDetails]
    """

    kwargs = _get_kwargs(
        id_or_email=id_or_email,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_or_email: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeysCreateUserApiKeyBody | Unset = UNSET,
) -> ApiKeyData | ProblemDetails | None:
    """Create a new API Key for a user

     Create a new API Key for a user

    Args:
        id_or_email (str):
        body (ApiKeysCreateUserApiKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyData | ProblemDetails
    """

    return (
        await asyncio_detailed(
            id_or_email=id_or_email,
            client=client,
            body=body,
        )
    ).parsed
