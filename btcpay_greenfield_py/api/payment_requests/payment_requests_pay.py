from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_data import InvoiceData
from ...models.payment_requests_pay_body import PaymentRequestsPayBody
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details_item import ValidationProblemDetailsItem
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
    payment_request_id: str,
    *,
    body: PaymentRequestsPayBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/stores/{store_id}/payment-requests/{payment_request_id}/pay".format(
            store_id=quote(str(store_id), safe=""),
            payment_request_id=quote(str(payment_request_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(InvoiceData.from_dict, response)

        return response_200

    if response.status_code == 400:
        response_400 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_400

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
) -> Response[InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    payment_request_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentRequestsPayBody | Unset = UNSET,
) -> Response[InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Create a new invoice for the payment request

     Create a new invoice for the payment request, or reuse an existing one

    Args:
        store_id (str):
        payment_request_id (str):
        body (PaymentRequestsPayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        payment_request_id=payment_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    payment_request_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentRequestsPayBody | Unset = UNSET,
) -> InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Create a new invoice for the payment request

     Create a new invoice for the payment request, or reuse an existing one

    Args:
        store_id (str):
        payment_request_id (str):
        body (PaymentRequestsPayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        store_id=store_id,
        payment_request_id=payment_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    payment_request_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentRequestsPayBody | Unset = UNSET,
) -> Response[InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Create a new invoice for the payment request

     Create a new invoice for the payment request, or reuse an existing one

    Args:
        store_id (str):
        payment_request_id (str):
        body (PaymentRequestsPayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        payment_request_id=payment_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    payment_request_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentRequestsPayBody | Unset = UNSET,
) -> InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Create a new invoice for the payment request

     Create a new invoice for the payment request, or reuse an existing one

    Args:
        store_id (str):
        payment_request_id (str):
        body (PaymentRequestsPayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceData | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            payment_request_id=payment_request_id,
            client=client,
            body=body,
        )
    ).parsed
