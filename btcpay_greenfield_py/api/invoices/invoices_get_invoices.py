from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.invoice_data import InvoiceData
from ...models.invoice_status import InvoiceStatus
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
    store_id: str,
    *,
    order_id: list[str] | Unset = UNSET,
    status: InvoiceStatus | Unset = UNSET,
    text_search: str | Unset = UNSET,
    start_date: float | Unset = UNSET,
    end_date: float | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_order_id: list[str] | Unset = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = order_id

    params["orderId"] = json_order_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["textSearch"] = text_search

    params["startDate"] = start_date

    params["endDate"] = end_date

    json_skip: float | None | Unset
    if isinstance(skip, Unset):
        json_skip = UNSET
    else:
        json_skip = skip
    params["skip"] = json_skip

    json_take: float | None | Unset
    if isinstance(take, Unset):
        json_take = UNSET
    else:
        json_take = take
    params["take"] = json_take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/stores/{store_id}/invoices".format(
            store_id=quote(str(store_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | list[InvoiceData]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_invoice_data_list_item_data in _response_200:
            if isinstance(componentsschemas_invoice_data_list_item_data, dict):
                componentsschemas_invoice_data_list_item = InvoiceData.from_dict(componentsschemas_invoice_data_list_item_data)
                response_200.append(componentsschemas_invoice_data_list_item)

        return response_200

    if response.status_code == 401:
        response_401 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_401

    response_default = _safe_from_dict(ProblemDetails.from_dict, response)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | list[InvoiceData]]:
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
    order_id: list[str] | Unset = UNSET,
    status: InvoiceStatus | Unset = UNSET,
    text_search: str | Unset = UNSET,
    start_date: float | Unset = UNSET,
    end_date: float | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> Response[ProblemDetails | list[InvoiceData]]:
    """Get invoices

     View information about the existing invoices

    Args:
        store_id (str):
        order_id (list[str] | Unset):
        status (InvoiceStatus | Unset): The status of the invoice
        text_search (str | Unset):
        start_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        end_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[InvoiceData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        order_id=order_id,
        status=status,
        text_search=text_search,
        start_date=start_date,
        end_date=end_date,
        skip=skip,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    *,
    client: AuthenticatedClient,
    order_id: list[str] | Unset = UNSET,
    status: InvoiceStatus | Unset = UNSET,
    text_search: str | Unset = UNSET,
    start_date: float | Unset = UNSET,
    end_date: float | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> ProblemDetails | list[InvoiceData] | None:
    """Get invoices

     View information about the existing invoices

    Args:
        store_id (str):
        order_id (list[str] | Unset):
        status (InvoiceStatus | Unset): The status of the invoice
        text_search (str | Unset):
        start_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        end_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[InvoiceData]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        order_id=order_id,
        status=status,
        text_search=text_search,
        start_date=start_date,
        end_date=end_date,
        skip=skip,
        take=take,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    *,
    client: AuthenticatedClient,
    order_id: list[str] | Unset = UNSET,
    status: InvoiceStatus | Unset = UNSET,
    text_search: str | Unset = UNSET,
    start_date: float | Unset = UNSET,
    end_date: float | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> Response[ProblemDetails | list[InvoiceData]]:
    """Get invoices

     View information about the existing invoices

    Args:
        store_id (str):
        order_id (list[str] | Unset):
        status (InvoiceStatus | Unset): The status of the invoice
        text_search (str | Unset):
        start_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        end_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[InvoiceData]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        order_id=order_id,
        status=status,
        text_search=text_search,
        start_date=start_date,
        end_date=end_date,
        skip=skip,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    *,
    client: AuthenticatedClient,
    order_id: list[str] | Unset = UNSET,
    status: InvoiceStatus | Unset = UNSET,
    text_search: str | Unset = UNSET,
    start_date: float | Unset = UNSET,
    end_date: float | Unset = UNSET,
    skip: float | None | Unset = UNSET,
    take: float | None | Unset = UNSET,
) -> ProblemDetails | list[InvoiceData] | None:
    """Get invoices

     View information about the existing invoices

    Args:
        store_id (str):
        order_id (list[str] | Unset):
        status (InvoiceStatus | Unset): The status of the invoice
        text_search (str | Unset):
        start_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        end_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        skip (float | None | Unset):
        take (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[InvoiceData]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            order_id=order_id,
            status=status,
            text_search=text_search,
            start_date=start_date,
            end_date=end_date,
            skip=skip,
            take=take,
        )
    ).parsed
