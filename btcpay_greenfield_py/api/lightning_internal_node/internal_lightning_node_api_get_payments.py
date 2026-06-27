from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.lightning_payment_data import LightningPaymentData
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
    crypto_code: str,
    *,
    include_pending: bool | None | Unset = False,
    offset_index: float | None | Unset = 0.0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_pending: bool | None | Unset
    if isinstance(include_pending, Unset):
        json_include_pending = UNSET
    else:
        json_include_pending = include_pending
    params["includePending"] = json_include_pending

    json_offset_index: float | None | Unset
    if isinstance(offset_index, Unset):
        json_offset_index = UNSET
    else:
        json_offset_index = offset_index
    params["offsetIndex"] = json_offset_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/server/lightning/{crypto_code}/payments".format(
            crypto_code=quote(str(crypto_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[LightningPaymentData]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LightningPaymentData.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = _safe_from_dict(ProblemDetails.from_dict, response)

        return response_401

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    response_default = _safe_from_dict(ProblemDetails.from_dict, response)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | list[LightningPaymentData]]:
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
    include_pending: bool | None | Unset = False,
    offset_index: float | None | Unset = 0.0,
) -> Response[Any | ProblemDetails | list[LightningPaymentData]]:
    """Get payments

     View information about the lightning payments

    Args:
        crypto_code (str):
        include_pending (bool | None | Unset):  Default: False.
        offset_index (float | None | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[LightningPaymentData]]
    """

    kwargs = _get_kwargs(
        crypto_code=crypto_code,
        include_pending=include_pending,
        offset_index=offset_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    include_pending: bool | None | Unset = False,
    offset_index: float | None | Unset = 0.0,
) -> Any | ProblemDetails | list[LightningPaymentData] | None:
    """Get payments

     View information about the lightning payments

    Args:
        crypto_code (str):
        include_pending (bool | None | Unset):  Default: False.
        offset_index (float | None | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[LightningPaymentData]
    """

    return sync_detailed(
        crypto_code=crypto_code,
        client=client,
        include_pending=include_pending,
        offset_index=offset_index,
    ).parsed


async def asyncio_detailed(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    include_pending: bool | None | Unset = False,
    offset_index: float | None | Unset = 0.0,
) -> Response[Any | ProblemDetails | list[LightningPaymentData]]:
    """Get payments

     View information about the lightning payments

    Args:
        crypto_code (str):
        include_pending (bool | None | Unset):  Default: False.
        offset_index (float | None | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[LightningPaymentData]]
    """

    kwargs = _get_kwargs(
        crypto_code=crypto_code,
        include_pending=include_pending,
        offset_index=offset_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    crypto_code: str,
    *,
    client: AuthenticatedClient,
    include_pending: bool | None | Unset = False,
    offset_index: float | None | Unset = 0.0,
) -> Any | ProblemDetails | list[LightningPaymentData] | None:
    """Get payments

     View information about the lightning payments

    Args:
        crypto_code (str):
        include_pending (bool | None | Unset):  Default: False.
        offset_index (float | None | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[LightningPaymentData]
    """

    return (
        await asyncio_detailed(
            crypto_code=crypto_code,
            client=client,
            include_pending=include_pending,
            offset_index=offset_index,
        )
    ).parsed
