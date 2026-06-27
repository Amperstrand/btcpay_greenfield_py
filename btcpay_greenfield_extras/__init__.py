"""Hand-written extensions to the generated btcpay_greenfield_py client.

This package contains production utilities that live outside the generated
package so they survive regeneration:

- :mod:`webhooks` — HMAC-SHA256 signature verification + typed event dispatch
- :mod:`integrations.flask` — optional Flask blueprint
- :mod:`integrations.fastapi` — optional FastAPI router (planned)
"""

from __future__ import annotations

from .webhooks import (
    InvalidSignatureError,
    UnknownEventTypeError,
    WebhookEventProcessor,
    parse_event,
    verify_and_parse,
    verify_signature,
)

__all__ = (
    "InvalidSignatureError",
    "UnknownEventTypeError",
    "WebhookEventProcessor",
    "parse_event",
    "verify_and_parse",
    "verify_signature",
)
