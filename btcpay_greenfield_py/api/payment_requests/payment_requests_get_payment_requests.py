from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payment_request_data import PaymentRequestData
from ...models.problem_details import ProblemDetails
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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/payment-requests".format(
            store_id=quote(str(store_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | list[PaymentRequestData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_payment_request_data_list_item_data in _response_200:
            if isinstance(componentsschemas_payment_request_data_list_item_data, dict):
                componentsschemas_payment_request_data_list_item = PaymentRequestData.from_dict(componentsschemas_payment_request_data_list_item_data)
                response_200.append(componentsschemas_payment_request_data_list_item)

        return response_200

    if response.status_code == 401:
        response_401 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | list[PaymentRequestData]]:
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
) -> Response[ProblemDetails | list[PaymentRequestData]]:
    """Get payment requests

     View information about the existing payment requests

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[PaymentRequestData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> ProblemDetails | list[PaymentRequestData] | None:
    """Get payment requests

     View information about the existing payment requests

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[PaymentRequestData]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProblemDetails | list[PaymentRequestData]]:
    """Get payment requests

     View information about the existing payment requests

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[PaymentRequestData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
) -> ProblemDetails | list[PaymentRequestData] | None:
    """Get payment requests

     View information about the existing payment requests

    Args:
        store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[PaymentRequestData]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
        )
    ).parsed
