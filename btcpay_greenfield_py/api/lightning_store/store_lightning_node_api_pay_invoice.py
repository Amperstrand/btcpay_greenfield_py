from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lightning_payment_data import LightningPaymentData
from ...models.pay_lightning_invoice_request import PayLightningInvoiceRequest
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
    crypto_code: str,
    *,
    body: PayLightningInvoiceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/stores/{store_id}/lightning/{crypto_code}/invoices/pay".format(
            store_id=quote(str(store_id), safe=""),
            crypto_code=quote(str(crypto_code), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(LightningPaymentData.from_dict, response)

        return response_200

    if response.status_code == 202:
        response_202 = _safe_from_dict(LightningPaymentData.from_dict, response)

        return response_202

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: PayLightningInvoiceRequest,
) -> Response[Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Pay Lightning Invoice

     Pay a lightning invoice. In case the payment response times out, the status will be reported as
    pending and the final status can be resolved using the [Get
    payment](#operation/StoreLightningNodeApi_GetPayment) endpoint. The default wait time for payment
    responses is 30 seconds — it might take longer if multiple routes are tried or a hold invoice is
    getting paid.

    Args:
        store_id (str):
        crypto_code (str):
        body (PayLightningInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: PayLightningInvoiceRequest,
) -> Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Pay Lightning Invoice

     Pay a lightning invoice. In case the payment response times out, the status will be reported as
    pending and the final status can be resolved using the [Get
    payment](#operation/StoreLightningNodeApi_GetPayment) endpoint. The default wait time for payment
    responses is 30 seconds — it might take longer if multiple routes are tried or a hold invoice is
    getting paid.

    Args:
        store_id (str):
        crypto_code (str):
        body (PayLightningInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return sync_detailed(
        store_id=store_id,
        crypto_code=crypto_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: PayLightningInvoiceRequest,
) -> Response[Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]]:
    """Pay Lightning Invoice

     Pay a lightning invoice. In case the payment response times out, the status will be reported as
    pending and the final status can be resolved using the [Get
    payment](#operation/StoreLightningNodeApi_GetPayment) endpoint. The default wait time for payment
    responses is 30 seconds — it might take longer if multiple routes are tried or a hold invoice is
    getting paid.

    Args:
        store_id (str):
        crypto_code (str):
        body (PayLightningInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        crypto_code=crypto_code,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    body: PayLightningInvoiceRequest,
) -> Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem] | None:
    """Pay Lightning Invoice

     Pay a lightning invoice. In case the payment response times out, the status will be reported as
    pending and the final status can be resolved using the [Get
    payment](#operation/StoreLightningNodeApi_GetPayment) endpoint. The default wait time for payment
    responses is 30 seconds — it might take longer if multiple routes are tried or a hold invoice is
    getting paid.

    Args:
        store_id (str):
        crypto_code (str):
        body (PayLightningInvoiceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningPaymentData | ProblemDetails | list[ValidationProblemDetailsItem]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            crypto_code=crypto_code,
            client=client,
            body=body,
        )
    ).parsed
