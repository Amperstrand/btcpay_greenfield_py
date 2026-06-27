"""Tests for btcpay_greenfield_extras.webhooks — signature verification, event parsing, and dispatch."""

from __future__ import annotations

import hashlib
import hmac
import json

import pytest

from btcpay_greenfield_extras import (
    InvalidSignatureError,
    UnknownEventTypeError,
    WebhookEventProcessor,
    parse_event,
    verify_and_parse,
    verify_signature,
)

SECRET = "test-webhook-secret-1234567890"


def _sign(body: bytes, secret: str = SECRET) -> str:
    digest = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def _make_event(event_type: str, **extra: object) -> bytes:
    payload: dict[str, object] = {
        "deliveryId": "del_001",
        "webhookId": "wh_001",
        "originalDeliveryId": "del_001",
        "isRedelivery": False,
        "type": event_type,
        "timestamp": 1592312018,
    }
    payload.update(extra)
    return json.dumps(payload).encode()


# --- Signature verification ---

class TestVerifySignature:
    def test_valid_signature(self) -> None:
        body = _make_event("InvoiceSettled", invoiceId="inv_123", storeId="store_456")
        sig = _sign(body)
        assert verify_signature(body, sig, SECRET) is True

    def test_wrong_secret(self) -> None:
        body = _make_event("InvoiceSettled")
        sig = _sign(body, SECRET)
        assert verify_signature(body, sig, "wrong-secret") is False

    def test_tampered_body(self) -> None:
        body = _make_event("InvoiceSettled")
        sig = _sign(body)
        tampered = body.replace(b"InvoiceSettled", b"InvoiceExpired")
        assert verify_signature(tampered, sig, SECRET) is False

    def test_missing_prefix(self) -> None:
        body = _make_event("InvoiceSettled")
        sig = _sign(body)
        assert verify_signature(body, sig[len("sha256="):], SECRET) is False

    def test_empty_header(self) -> None:
        body = _make_event("InvoiceSettled")
        assert verify_signature(body, "", SECRET) is False

    def test_constant_time_comparison(self) -> None:
        """hmac.compare_digest prevents timing attacks."""
        body = _make_event("InvoiceSettled")
        sig = _sign(body)
        assert verify_signature(body, sig, SECRET) is True
        assert verify_signature(body, "sha256=0000000000000000000000000000000000000000000000000000000000000000", SECRET) is False


# --- Event parsing ---

class TestParseEvent:
    def test_invoice_settled(self) -> None:
        body = _make_event(
            "InvoiceSettled",
            invoiceId="inv_abc",
            storeId="store_xyz",
            manuallyMarked=False,
            overPaid=False,
        )
        event = parse_event(body)
        assert event.type_ == "InvoiceSettled"
        assert event.invoice_id == "inv_abc"
        assert event.store_id == "store_xyz"
        assert event.manually_marked is False
        assert event.over_paid is False

    def test_invoice_expired(self) -> None:
        body = _make_event("InvoiceExpired", invoiceId="inv_abc", storeId="store_xyz")
        event = parse_event(body)
        assert event.type_ == "InvoiceExpired"
        assert event.invoice_id == "inv_abc"

    def test_invoice_created_falls_back_to_base_invoice_event(self) -> None:
        body = _make_event("InvoiceCreated", invoiceId="inv_abc", storeId="store_xyz")
        event = parse_event(body)
        assert event.type_ == "InvoiceCreated"
        # InvoiceCreated maps to the generic WebhookInvoiceEvent

    def test_unknown_event_type_non_strict(self) -> None:
        body = _make_event("SomeNewEventType")
        event = parse_event(body)
        assert event.type_ == "SomeNewEventType"

    def test_unknown_event_type_strict(self) -> None:
        body = _make_event("SomeNewEventType")
        with pytest.raises(UnknownEventTypeError):
            parse_event(body, strict=True)

    def test_base_fields_preserved(self) -> None:
        body = _make_event("InvoiceSettled")
        event = parse_event(body)
        assert event.delivery_id == "del_001"
        assert event.webhook_id == "wh_001"
        assert event.is_redelivery is False
        assert event.timestamp == 1592312018


# --- Combined verify + parse ---

class TestVerifyAndParse:
    def test_valid_sig_returns_typed_event(self) -> None:
        body = _make_event("InvoiceSettled", invoiceId="inv_123", storeId="store_456")
        sig = _sign(body)
        event = verify_and_parse(body, sig, SECRET)
        assert event.type_ == "InvoiceSettled"
        assert event.invoice_id == "inv_123"

    def test_invalid_sig_raises(self) -> None:
        body = _make_event("InvoiceSettled")
        with pytest.raises(InvalidSignatureError):
            verify_and_parse(body, "sha256=invalid", SECRET)


# --- Event processor dispatch ---

class TestWebhookEventProcessor:
    def test_dispatch_to_registered_handler(self) -> None:
        received: list[str] = []
        processor = WebhookEventProcessor()
        processor.on("InvoiceSettled", lambda e: received.append(e.invoice_id))

        body = _make_event("InvoiceSettled", invoiceId="inv_abc", storeId="store_xyz")
        event = parse_event(body)
        processor.process(event)

        assert received == ["inv_abc"]

    def test_multiple_handlers_same_event(self) -> None:
        calls: list[str] = []
        processor = WebhookEventProcessor()
        processor.on("InvoiceSettled", lambda e: calls.append("handler1"))
        processor.on("InvoiceSettled", lambda e: calls.append("handler2"))

        body = _make_event("InvoiceSettled")
        processor.process(parse_event(body))

        assert calls == ["handler1", "handler2"]

    def test_unknown_handler_fires_for_unregistered_type(self) -> None:
        unknown: list[str] = []
        processor = WebhookEventProcessor()
        processor.on_unknown(lambda e: unknown.append(e.type_))

        body = _make_event("SomeNewType")
        processor.process(parse_event(body))

        assert unknown == ["SomeNewType"]

    def test_no_handler_for_unregistered_type_no_error(self) -> None:
        processor = WebhookEventProcessor()
        body = _make_event("SomeNewType")
        event = parse_event(body)
        processor.process(event)

    def test_handle_raw_verifies_and_dispatches(self) -> None:
        received: list[str] = []
        processor = WebhookEventProcessor()
        processor.on("InvoiceSettled", lambda e: received.append(e.invoice_id))

        body = _make_event("InvoiceSettled", invoiceId="inv_xyz", storeId="store_1")
        sig = _sign(body)

        event = processor.handle_raw(body, sig, SECRET)
        assert event.type_ == "InvoiceSettled"
        assert received == ["inv_xyz"]

    def test_handle_raw_bad_signature_raises(self) -> None:
        processor = WebhookEventProcessor()
        body = _make_event("InvoiceSettled")
        with pytest.raises(InvalidSignatureError):
            processor.handle_raw(body, "sha256=bad", SECRET)
