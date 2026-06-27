"""Runnable BTCPay webhook receiver using only the Python standard library.

Listens on localhost:8080 and verifies + dispatches incoming webhooks.

Usage::

    python examples/webhook_receiver.py

Then configure your BTCPay Server webhook to point to your tunnelled URL
(e.g. via ``ngrok http 8080``) with the secret printed on startup.
"""

from __future__ import annotations

import os
import secrets
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

from btcpay_greenfield_extras import WebhookEventProcessor, verify_and_parse


def make_handler(secret: str, processor: WebhookEventProcessor) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            sig = self.headers.get("BTCPay-Sig", "")

            try:
                event = verify_and_parse(body, sig, secret)
            except Exception as exc:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(f"rejected: {exc}\n".encode())
                return

            processor.process(event)
            self.send_response(200)
            self.end_headers()

        def log_message(self, fmt: str, *args: object) -> None:
            print(f"[webhook] {fmt % args}", file=sys.stderr)

    return Handler


def main() -> None:
    secret = os.environ.get("BTCPAY_WEBHOOK_SECRET") or secrets.token_urlsafe(24)
    port = int(os.environ.get("PORT", "8080"))

    processor = WebhookEventProcessor()

    def log_event(label: str):
        def handler(event: object) -> None:
            t = getattr(event, "type_", "?")
            inv = getattr(event, "invoice_id", None)
            print(f"[event] {label}: type={t} invoice={inv}")
        return handler

    for event_type in (
        "InvoiceCreated",
        "InvoiceReceivedPayment",
        "InvoiceProcessing",
        "InvoiceSettled",
        "InvoicePaymentSettled",
        "InvoiceExpired",
        "InvoiceInvalid",
    ):
        processor.on(event_type, log_event(event_type))

    processor.on_unknown(lambda e: print(f"[event] UNKNOWN: type={getattr(e, 'type_', '?')}"))

    print(f"BTCPay webhook receiver listening on http://localhost:{port}")
    print(f"Webhook secret: {secret}")
    print("Configure your BTCPay Server webhook with this secret.")
    print("Press Ctrl+C to stop.\n")

    HTTPServer(("0.0.0.0", port), make_handler(secret, processor)).serve_forever()


if __name__ == "__main__":
    main()
