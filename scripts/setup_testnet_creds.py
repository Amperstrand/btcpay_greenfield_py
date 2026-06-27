#!/usr/bin/env python3
"""Auto-register a throwaway BTCPay Server account on testnet.demo.btcpayserver.org.

testnet.demo.btcpayserver.org allows anonymous POST /api/v1/users (no Turnstile,
no admin required). This script creates a unique account, provisions an
unrestricted API key, creates a test store, and emits the credentials as
GitHub Actions environment directives (``key=value`` lines consumed by
``$GITHUB_ENV``).

Locally, you can source the output:

    eval "$(python3 scripts/setup_testnet_creds.py)"
    pytest tests/test_smoke_authed.py -v

The account and store persist on the testnet server (we cannot self-delete
without admin), but the email is random + disposable and the server is reset
periodually.
"""
from __future__ import annotations

import os
import secrets
import sys

import httpx

HOST = "https://testnet.demo.btcpayserver.org"


def main() -> int:
    email = f"ci+{secrets.token_hex(4)}@example.com"
    password = secrets.token_urlsafe(16)

    with httpx.Client(base_url=HOST, timeout=30, follow_redirects=True) as client:
        r = client.post("/api/v1/users", json={"email": email, "password": password})
        if r.status_code not in (200, 201):
            print(f"!! registration failed: HTTP {r.status_code} {r.text}", file=sys.stderr)
            return 1

        r = client.post(
            "/api/v1/api-keys",
            auth=(email, password),
            json={"label": "ci", "permissions": ["unrestricted"]},
        )
        if r.status_code != 200:
            print(f"!! api-key creation failed: HTTP {r.status_code} {r.text}", file=sys.stderr)
            return 1
        api_key = r.json()["apiKey"]

        r = client.post(
            "/api/v1/stores",
            headers={"Authorization": f"token {api_key}"},
            json={"name": "CI Smoke Test", "defaultCurrency": "USD"},
        )
        if r.status_code != 200:
            print(f"!! store creation failed: HTTP {r.status_code} {r.text}", file=sys.stderr)
            return 1
        store_id = r.json()["id"]

    # Emit GitHub Actions ::add-mask:: directives BEFORE printing the values
    # so the auto-registered API key is redacted from CI step logs.
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::add-mask::{api_key}")
        print(f"::add-mask::{store_id}")

    print(f"BTCPAY_HOST={HOST}")
    print(f"BTCPAY_API_KEY={api_key}")
    print(f"BTCPAY_STORE_ID={store_id}")
    print(f"# registered {email}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
