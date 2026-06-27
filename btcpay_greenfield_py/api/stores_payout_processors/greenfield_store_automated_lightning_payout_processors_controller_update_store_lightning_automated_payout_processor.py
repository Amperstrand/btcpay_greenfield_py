from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lightning_automated_transfer_settings import LightningAutomatedTransferSettings
from ...models.update_lightning_automated_transfer_settings import UpdateLightningAutomatedTransferSettings
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
    payment_method: str,
    *,
    body: UpdateLightningAutomatedTransferSettings,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/stores/{store_id}/payout-processors/LightningAutomatedPayoutSenderFactory/{payment_method}".format(
            store_id=quote(str(store_id), safe=""),
            payment_method=quote(str(payment_method), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LightningAutomatedTransferSettings | None:
    if response.status_code == 200:
        response_200 = _safe_from_dict(LightningAutomatedTransferSettings.from_dict, response)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LightningAutomatedTransferSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLightningAutomatedTransferSettings,
) -> Response[Any | LightningAutomatedTransferSettings]:
    """Update configured store Lightning automated payout processors

     Update configured store Lightning automated payout processors

    Args:
        store_id (str):
        payment_method (str):
        body (UpdateLightningAutomatedTransferSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningAutomatedTransferSettings]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        payment_method=payment_method,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLightningAutomatedTransferSettings,
) -> Any | LightningAutomatedTransferSettings | None:
    """Update configured store Lightning automated payout processors

     Update configured store Lightning automated payout processors

    Args:
        store_id (str):
        payment_method (str):
        body (UpdateLightningAutomatedTransferSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningAutomatedTransferSettings
    """

    return sync_detailed(
        store_id=store_id,
        payment_method=payment_method,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    store_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLightningAutomatedTransferSettings,
) -> Response[Any | LightningAutomatedTransferSettings]:
    """Update configured store Lightning automated payout processors

     Update configured store Lightning automated payout processors

    Args:
        store_id (str):
        payment_method (str):
        body (UpdateLightningAutomatedTransferSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightningAutomatedTransferSettings]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        payment_method=payment_method,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: str,
    payment_method: str,
    *,
    client: AuthenticatedClient,
    body: UpdateLightningAutomatedTransferSettings,
) -> Any | LightningAutomatedTransferSettings | None:
    """Update configured store Lightning automated payout processors

     Update configured store Lightning automated payout processors

    Args:
        store_id (str):
        payment_method (str):
        body (UpdateLightningAutomatedTransferSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightningAutomatedTransferSettings
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            payment_method=payment_method,
            client=client,
            body=body,
        )
    ).parsed
