"""Optional Flask integration for BTCPay Server webhooks.

Usage::

    from flask import Flask
    from btcpay_greenfield_extras.integrations.flask import create_btcpay_webhook_blueprint

    app = Flask(__name__)
    webhook_bp = create_btcpay_webhook_blueprint(secret="your-webhook-secret")
    webhook_bp.on("InvoiceSettled", lambda e: print(f"paid: {e.invoice_id}"))
    app.register_blueprint(webhook_bp, url_prefix="/webhooks/btcpay")

The blueprint exposes a POST ``/`` route that:
1. Reads the raw body and ``BTCPay-Sig`` header.
2. Verifies the HMAC-SHA256 signature.
3. Parses the JSON into a typed event model.
4. Dispatches to registered handlers.
5. Returns 200 on success, 401 on bad signature, 400 on parse error.

Requires Flask: ``pip install flask``
"""

from __future__ import annotations

from ..webhooks import InvalidSignatureError, WebhookEventProcessor


def create_btcpay_webhook_blueprint(secret: str, *, url_rule: str = "/"):
    """Create a Flask Blueprint that handles BTCPay webhook deliveries.

    Parameters
    ----------
    secret
        The webhook secret (configured when creating the webhook in BTCPay).
    url_rule
        The path within the blueprint to register. Defaults to ``/``.

    Returns
    -------
    flask.Blueprint
        A blueprint with an ``on(event_type, handler)`` method for registering
        typed event handlers, and an ``on_unknown(handler)`` for fallback.
    """
    from flask import Blueprint, request

    processor = WebhookEventProcessor()

    bp = Blueprint("btcpay_webhook", __name__)

    @bp.route(url_rule, methods=["POST"])
    def _handle() -> tuple[str, int]:
        raw_body = request.get_data()
        sig_header = request.headers.get("BTCPay-Sig", "")

        try:
            processor.handle_raw(raw_body, sig_header, secret)
        except InvalidSignatureError:
            return "invalid signature", 401
        except Exception as exc:
            return f"parse error: {exc}", 400

        return "", 200

    # Expose processor's registration API on the blueprint
    bp.on = processor.on  # type: ignore[attr-defined]
    bp.on_unknown = processor.on_unknown  # type: ignore[attr-defined]
    return bp
