"""Framework-agnostic BTCPay Server webhook verification and event dispatch.

BTCPay Server signs every webhook delivery with HMAC-SHA256 using the webhook's
secret. The signature is sent in the ``BTCPay-Sig`` header as
``sha256=<hex_digest>``.

Usage
-----
::

    from btcpay_greenfield_extras import verify_and_parse

    raw_body: bytes = request.get_data()      # Flask
    sig_header: str = request.headers["BTCPay-Sig"]
    secret: str = "your-webhook-secret"

    event = verify_and_parse(raw_body, sig_header, secret)
    # event is now a typed model (WebhookInvoiceSettledEvent, etc.)

    if event.type_ == "InvoiceSettled":
        invoice_id = event.invoice_id
        ...

For callback-based dispatch, see :class:`WebhookEventProcessor`.
"""

from __future__ import annotations

import hashlib
import hmac
from typing import Any, Protocol, runtime_checkable

# Event type strings (from BTCPay Server source / generated WebhookEvent.type_ docstring)
INVOICE_CREATED = "InvoiceCreated"
INVOICE_RECEIVED_PAYMENT = "InvoiceReceivedPayment"
INVOICE_PROCESSING = "InvoiceProcessing"
INVOICE_EXPIRED = "InvoiceExpired"
INVOICE_SETTLED = "InvoiceSettled"
INVOICE_INVALID = "InvoiceInvalid"
INVOICE_PAYMENT_SETTLED = "InvoicePaymentSettled"

# Map BTCPay event type strings to their generated model classes.
# Lazy import to avoid loading the entire package on first use.
def _event_model_map() -> dict[str, type]:
    from btcpay_greenfield_py.models.webhook_invoice_event import WebhookInvoiceEvent
    from btcpay_greenfield_py.models.webhook_invoice_expired_event import (
        WebhookInvoiceExpiredEvent,
    )
    from btcpay_greenfield_py.models.webhook_invoice_invalid_event import (
        WebhookInvoiceInvalidEvent,
    )
    from btcpay_greenfield_py.models.webhook_invoice_processing_event import (
        WebhookInvoiceProcessingEvent,
    )
    from btcpay_greenfield_py.models.webhook_invoice_received_payment_event import (
        WebhookInvoiceReceivedPaymentEvent,
    )
    from btcpay_greenfield_py.models.webhook_invoice_settled_event import (
        WebhookInvoiceSettledEvent,
    )

    # InvoicePaymentSettled has no dedicated model in the generated package;
    # fall back to the generic WebhookInvoiceEvent which has invoice_id + store_id.
    return {
        INVOICE_CREATED: WebhookInvoiceEvent,
        INVOICE_RECEIVED_PAYMENT: WebhookInvoiceReceivedPaymentEvent,
        INVOICE_PROCESSING: WebhookInvoiceProcessingEvent,
        INVOICE_EXPIRED: WebhookInvoiceExpiredEvent,
        INVOICE_SETTLED: WebhookInvoiceSettledEvent,
        INVOICE_INVALID: WebhookInvoiceInvalidEvent,
        INVOICE_PAYMENT_SETTLED: WebhookInvoiceEvent,
    }


class InvalidSignatureError(Exception):
    """Raised when the ``BTCPay-Sig`` header does not match the body + secret."""


class UnknownEventTypeError(Exception):
    """Raised when the event ``type`` is not in the known event map.

    BTCPay may add new event types in future releases. When this happens,
    :func:`parse_event` falls back to the base ``WebhookEvent`` model unless
    ``strict=True`` is passed.
    """


def verify_signature(
    body: bytes | bytearray,
    btcpay_sig_header: str,
    secret: str,
) -> bool:
    """Verify the ``BTCPay-Sig`` header against the raw request body.

    Parameters
    ----------
    body
        The **raw** HTTP request body bytes. Do NOT pass parsed/decoded JSON.
        The signature is computed over the exact bytes BTCPay sent.
    btcpay_sig_header
        The value of the ``BTCPay-Sig`` HTTP header (e.g. ``"sha256=abc..."``).
    secret
        The webhook secret configured when the webhook was created via
        ``POST /api/v1/stores/{storeId}/webhooks``.
    """
    prefix = "sha256="
    if not btcpay_sig_header.startswith(prefix):
        return False
    expected = btcpay_sig_header[len(prefix):]

    computed = hmac.new(
        secret.encode("utf-8"),
        bytes(body),
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected, computed)


def parse_event(
    body: bytes | bytearray,
    *,
    strict: bool = False,
) -> Any:
    """Parse a raw webhook body into a typed event model.

    Does NOT verify the signature — use :func:`verify_and_parse` for that.

    Parameters
    ----------
    body
        Raw HTTP request body bytes.
    strict
        If ``True``, raise :class:`UnknownEventTypeError` for unrecognized event types.
        If ``False`` (default), fall back to the base ``WebhookEvent`` model.
    """
    import json

    data = json.loads(body)
    event_type = data.get("type", "")

    model_map = _event_model_map()
    from btcpay_greenfield_py.models.webhook_event import WebhookEvent

    model_cls = model_map.get(event_type)
    if model_cls is None:
        if strict:
            raise UnknownEventTypeError(f"unrecognized webhook event type: {event_type!r}")
        model_cls = WebhookEvent

    return model_cls.from_dict(data)


def verify_and_parse(
    body: bytes | bytearray,
    btcpay_sig_header: str,
    secret: str,
    *,
    strict: bool = False,
) -> Any:
    """Verify the signature AND parse the body in one call.

    Raises :class:`InvalidSignatureError` if the signature doesn't match.
    """
    if not verify_signature(body, btcpay_sig_header, secret):
        raise InvalidSignatureError(
            "BTCPay-Sig header does not match the computed HMAC. "
            "Check that the webhook secret is correct and that you're passing "
            "the RAW request body (not parsed JSON)."
        )
    return parse_event(body, strict=strict)


@runtime_checkable
class EventHandler(Protocol):
    """Protocol for typed event handler callbacks."""

    def __call__(self, event: Any) -> None: ...


class WebhookEventProcessor:
    """Callback-based event dispatcher.

    Register handlers for specific event types, then call :meth:`process`
    with an already-parsed event (or :meth:`handle_raw` with the raw body
    + signature for verify-then-dispatch in one call).

    Example::

        processor = WebhookEventProcessor()
        processor.on("InvoiceSettled", handle_payment)
        processor.on("InvoiceExpired", handle_expiry)
        processor.on_unknown(handle_unknown)

        event = verify_and_parse(body, sig, secret)
        processor.process(event)
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = {}
        self._unknown_handler: EventHandler | None = None

    def on(self, event_type: str, handler: EventHandler) -> WebhookEventProcessor:
        self._handlers.setdefault(event_type, []).append(handler)
        return self

    def on_unknown(self, handler: EventHandler) -> WebhookEventProcessor:
        self._unknown_handler = handler
        return self

    def process(self, event: Any) -> None:
        event_type = getattr(event, "type_", None) or ""
        handlers = self._handlers.get(event_type)
        if handlers:
            for h in handlers:
                h(event)
        elif self._unknown_handler:
            self._unknown_handler(event)

    def handle_raw(
        self,
        body: bytes | bytearray,
        btcpay_sig_header: str,
        secret: str,
        *,
        strict: bool = False,
    ) -> Any:
        """Verify signature, parse event, dispatch to handlers. Returns the parsed event."""
        event = verify_and_parse(body, btcpay_sig_header, secret, strict=strict)
        self.process(event)
        return event
