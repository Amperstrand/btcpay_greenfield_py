# btcpay_greenfield_py

A modern, auto-generated Python client for the [BTCPay Server](https://btcpayserver.org) [Greenfield API v1](https://docs.btcpayserver.org/API/Greenfield/v1/).

> **Status:** This is the only complete Python client targeting the BTCPay Server **Greenfield** REST API. The official `btcpayserver/btcpay-python` library targets the legacy BitPay-compatible API and does not support Greenfield. The BTCPay project ships official Greenfield clients for .NET and PHP only — there is **no** official Python client.

## What this project is

This repo is a **generator-driven SDK**: the source of truth is the OpenAPI spec (`swagger.json`) plus a generator config (`openapi-python-client.config.yaml`). The `btcpay_greenfield_py/` package is the generated output. Regenerating is one command.

| Layer | Tool | Output |
|---|---|---|
| Spec | `swagger.json` (from a running BTCPay Server) | OpenAPI 3.0, 119 paths, 141 schemas |
| Generator | [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) v0.29+ | httpx + attrs, sync + async |
| Package | `btcpay_greenfield_py/` | 31 API modules, 169 models, ~684 endpoint functions |

### Stack

- **HTTP:** [`httpx`](https://www.python-httpx.org/) — sync **and** async, HTTP/2-ready
- **Models:** [`attrs`](https://www.attrs.org/) — typed, validated, with `from_dict` / `to_dict`
- **Python:** 3.11+
- **Typing:** ships `py.typed` (PEP 561)
- **Lint:** `ruff`
- **Build:** Poetry / `pyproject.toml`

## Install

```bash
pip install btcpay-greenfield-py
```

For development:

```bash
pipx install poetry
poetry install
```

## Usage

The BTCPay Greenfield API uses two auth schemes (see [Greenfield Authorization](https://docs.btcpayserver.org/BTCPayServer/greenfield-authorization/)):

- **API Key** — sent as `Authorization: token <key>` (the canonical form)
- **Basic** — HTTP Basic with username/password (grants `unrestricted` implicitly)

```python
from btcpay_greenfield_py import AuthenticatedClient

# API key auth (recommended)
client = AuthenticatedClient(
    base_url="https://testnet.demo.btcpayserver.org",
    token="YOUR_API_KEY",
    prefix="token",  # BTCPay's expected prefix; defaults to "Bearer"
)
```

Calling an endpoint — every path/method combo becomes a module with **four** variants (`sync`, `sync_detailed`, `asyncio`, `asyncio_detailed`):

```python
from btcpay_greenfield_py.api.health.health_get_health import sync as get_health

with client as client:
    health = get_health(client=client)
    print(health)
```

Async:

```python
import asyncio
from btcpay_greenfield_py.api.health.health_get_health import asyncio as get_health_async

async def main():
    async with client as client:
        health = await get_health_async(client=client)
        print(health)

asyncio.run(main())
```

Creating an invoice (requires a store ID and the `btcpay.store.cancreateinvoice` permission):

```python
from btcpay_greenfield_py.api.invoices.invoices_create_invoice import sync as create_invoice
from btcpay_greenfield_py.models.create_invoice_request import CreateInvoiceRequest

with client as client:
    invoice = create_invoice(
        store_id="YOUR_STORE_ID",
        client=client,
        body=CreateInvoiceRequest(amount="5.00", currency="USD"),
    )
    print(invoice.id, invoice.checkout_link)
```

See [`examples/`](examples/) for runnable scripts.

## Webhook handling

BTCPay Server sends signed webhook events on invoice status changes (`InvoiceSettled`, `InvoiceExpired`, etc.). The `btcpay_greenfield_extras` package provides framework-agnostic HMAC-SHA256 signature verification and typed event dispatch.

```python
from btcpay_greenfield_extras import verify_and_parse

# raw_body = the exact bytes from the HTTP request (NOT parsed JSON)
# btcpay_sig = the BTCPay-Sig header value ("sha256=...")
# secret = the webhook secret configured when creating the webhook in BTCPay
event = verify_and_parse(raw_body, btcpay_sig, secret)

if event.type_ == "InvoiceSettled":
    print(f"invoice {event.invoice_id} settled")
    print(f"  store: {event.store_id}")
    print(f"  overpaid: {event.over_paid}")
```

For callback-based dispatch:

```python
from btcpay_greenfield_extras import WebhookEventProcessor

processor = WebhookEventProcessor()
processor.on("InvoiceSettled", lambda e: print(f"paid: {e.invoice_id}"))
processor.on("InvoiceExpired", lambda e: print(f"expired: {e.invoice_id}"))
processor.on_unknown(lambda e: print(f"unknown event: {e.type_}"))

# In your webhook handler:
processor.handle_raw(raw_body, btcpay_sig, secret)
```

### Flask integration

```python
from flask import Flask
from btcpay_greenfield_extras.integrations.flask import create_btcpay_webhook_blueprint

app = Flask(__name__)
bp = create_btcpay_webhook_blueprint(secret="your-webhook-secret")
bp.on("InvoiceSettled", lambda e: print(f"paid: {e.invoice_id}"))
app.register_blueprint(bp, url_prefix="/webhooks/btcpay")
```

### Runnable receiver

```bash
python examples/webhook_receiver.py
# prints a random secret on startup, listens on :8080
```

See [`examples/webhook_receiver.py`](examples/webhook_receiver.py) for a stdlib-only receiver (no framework dependency).

## Production middleware

The `btcpay_greenfield_extras.middleware` module provides retry, timeout, logging, and metrics for production deployments.

```python
from btcpay_greenfield_py import AuthenticatedClient
from btcpay_greenfield_extras import configure_production_client

client = AuthenticatedClient(base_url="https://btcpay.example.com", token="...", prefix="token")
configure_production_client(client, max_retries=3, timeout=30.0)
```

This wraps the underlying httpx client with:

- **Retry** on 5xx + transient connection errors (`ConnectError`, `ReadTimeout`, `WriteTimeout`, `PoolTimeout`) with exponential backoff (0.5s → 1s → 2s)
- **Timeout** defaults: 10s connect, 30s read, 10s write, 5s pool (the generated client defaults to no timeout, which is dangerous)
- **Structured logging** via stdlib `logging` — logs `method + URL + status_code`. Auth headers are NEVER logged.
- **Metrics callbacks** — optional `MetricsCallback` protocol for plugging into Prometheus, Datadog, etc.

Custom metrics example:

```python
from btcpay_greenfield_extras import configure_production_client

def my_metrics(*, method, url, status, duration_s, retried, error):
    print(f"{method} {url} → {status} in {duration_s:.3f}s (retried={retried})")

configure_production_client(client, metrics=my_metrics)
```

## Regenerating

The package under `btcpay_greenfield_py/` is generated. To regenerate after updating `swagger.json`:

```bash
# install the generator once
pipx install openapi-python-client

# regenerate in-place (patches swagger.json workarounds → regenerates → replaces package)
./scripts/regenerate.sh
```

What this does behind the scenes:
1. [`scripts/patch_swagger.py`](scripts/patch_swagger.py) rewrites the broken `InvoiceMetadata.anyOf` in the spec into a plain freeform object (the published BTCPay spec has title-bearing subschemas that openapi-python-client cannot disambiguate, producing a broken runtime import in the generated `CreateInvoiceRequest.to_dict()`).
2. `openapi-python-client generate` emits a fresh `btcpay-greenfield-py/` project.
3. The package directory is swapped in, leaving the hand-curated `pyproject.toml` and `README.md` untouched.

The [`openapi-python-client.config.yaml`](openapi-python-client.config.yaml) pins the package name override so the import name stays `btcpay_greenfield_py`.

### Source spec

`swagger.json` is captured from a running BTCPay Server instance. The published spec at `docs.btcpayserver.org/API/Greenfield/v1/swagger.json` is missing request-body definitions for ~50 POST/PUT endpoints, so a runtime capture is used. `swagger.public-docs.btcpayserver.org.json` is retained for reference.

## Testing

CI (`.github/workflows/ci.yml`) runs six jobs on every push and pull request:

| Job | What it verifies |
|---|---|
| `regenerate-check` | `swagger.json` + generator config reproduces the committed `btcpay_greenfield_py/` exactly |
| `lint` | `ruff check` on package + examples + tests |
| `typecheck` | `mypy` on examples + tests (generated code is loosely typed) |
| `generated-surface` | Meta-test iterating every endpoint module, asserts each exposes the right variant functions |
| `smoke-public` | Hits `/api/v1/health` against `https://testnet.demo.btcpayserver.org/` — no secrets required |
| `smoke-authed` | Round-trip invoice create/archive on testnet — only runs when `BTCPAY_CI_AUTHED_ENABLED=1` repo variable is set |

Run tests locally:

```bash
pytest -q                              # everything except network tests
pytest tests/test_generated_surface.py # meta-test only (no network)
pytest -m "not network"                # everything except real-HTTP tests
BTCPAY_HOST=https://testnet.demo.btcpayserver.org pytest tests/test_smoke_public.py -v
```

### Authed smoke tests

To enable the authed smoke tests in CI:

1. Register an account on https://testnet.demo.btcpayserver.org/ (free, no email verification).
2. Create a store. Note the store ID from the store settings URL.
3. Go to **Account** → **API Keys** → **Create new API key**. Grant at minimum:
   - `btcpay.user.canviewprofile`
   - `btcpay.store.canviewstoresettings`
   - `btcpay.store.canviewinvoices`
   - `btcpay.store.cancreateinvoice`
   - `btcpay.store.canmodifyinvoices` (for the archive step)
4. In your GitHub repo, add **Settings → Secrets and variables → Actions**:
   - Secrets: `BTCPAY_TESTNET_API_KEY` (the key from step 3), `BTCPAY_TESTNET_STORE_ID`
   - Variables: `BTCPAY_CI_AUTHED_ENABLED` = `true`

Once enabled, the `smoke-authed` job will run on every push and exercise the authenticated write path against the testnet demo.

### Why no auto-registration?

BTCPay Server's signup form is gated by a Cloudflare Turnstile CAPTCHA that cannot be solved programmatically in CI. Manual one-time account creation is the tradeoff for having real end-to-end coverage of the write path.

## License

MIT — same as BTCPay Server itself.
