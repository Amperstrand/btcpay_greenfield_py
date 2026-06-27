# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-27

Complete rewrite from the 2023 openapi-generator-cli urllib3 client to a modern
openapi-python-client httpx+attrs client. No backwards compatibility with the
v0.x API surface — see [`MIGRATION.md`](MIGRATION.md) for migration guidance.

### Added

- **Generated client** regenerated with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
  from the BTCPay Server Greenfield API v1 spec. Stack: httpx (sync + async),
  attrs models, PEP 561 `py.typed`, Python 3.11+. 370 files, 50k LOC, 171
  endpoints × 4 variants (`sync`, `sync_detailed`, `asyncio`, `asyncio_detailed`).
- **`btcpay_greenfield_extras.webhooks`** — framework-agnostic HMAC-SHA256
  webhook signature verification with typed event dispatch. Supports all 7
  BTCPay event types. Includes optional Flask blueprint integration.
- **`btcpay_greenfield_extras.middleware`** — production middleware: retry on
  5xx with exponential backoff, configurable timeout defaults (10s connect /
  30s read), structured logging (auth headers never logged), metrics callback
  protocol for Prometheus/Datadog integration.
- **CI pipeline** (`.github/workflows/ci.yml`) — 6 jobs across Python 3.11–3.14:
  regenerate-check (no-drift invariant), ruff lint, mypy typecheck, unit tests
  (webhooks + middleware + generated-surface meta-tests), public smoke tests
  against `testnet.demo.btcpayserver.org`, authed smoke tests with auto-registration
  (no manual secrets needed).
- **Post-processor** (`scripts/post_process_generated.py`) — patches two
  generated-code bugs across 197 call sites: empty-body JSON parse crash on
  error responses, and list-iteration type mismatch when server returns object
  instead of list.
- **Spec patcher** (`scripts/patch_swagger.py`) — works around upstream
  `InvoiceMetadata.anyOf` schema bug that produced duplicate model names and
  broken `to_dict()` runtime imports.
- **Auto-registration** (`scripts/setup_testnet_creds.py`) — programmatically
  registers a throwaway account on `testnet.demo.btcpayserver.org` each CI run,
  creates an unrestricted API key + store, emits `::add-mask::` directives to
  redact secrets from logs.
- **9 example scripts**: health check, invoice creation, user creation, pull
  payments, payment requests, lightning node info, custodians, webhook receiver.
- **Documentation**: README (usage + regen + CI setup + webhook + middleware
  sections), CONTRIBUTING.md (generator-driven workflow), MIGRATION.md (v0→v1
  patterns), LICENSE (MIT).
- **557 tests**: 514 generated-surface meta-tests (structural), 20 webhook
  unit tests, 12 middleware unit tests, 7 authed smoke tests (verified passing
  against auto-registered testnet account), 4 public smoke tests.

### Changed

- **Source spec** switched from `docs.btcpayserver.org` public swagger.json
  (missing ~50 `requestBody` definitions) to a runtime capture from a live
  BTCPay Server instance. Original archived as `swagger.public-docs.btcpayserver.org.json`.
- **Package layout** flattened from doubled-nested `btcpay_greenfield_py/btcpay_greenfield_py/`
  to flat `btcpay_greenfield_py/` at repo root.
- **Auth format** documented: BTCPay uses `Authorization: token <key>`, not
  `Bearer`. The `AuthenticatedClient` accepts `prefix="token"` to handle this.
- **Python floor** raised from 3.7 (EOL) to 3.11.

### Removed

- Old urllib3-based generated code (~140k LOC).
- `openapitools.json`, `readme.sh`, `setup.py`, `setup.cfg`, `tox.ini`,
  `.travis.yml`, `.gitlab-ci.yml`.
- Auto-generated per-endpoint markdown docs (`docs/*.md`) and auto-generated
  test stubs (`test/test_*.py`).
- Hardcoded API key from `config.py` (now loaded from environment variables).

### Fixed

- `examples/create_invoice.py` was calling `HealthApi` instead of the invoice
  creation endpoint (copy-paste bug from v0.x).

[1.0.0]: https://github.com/Amperstrand/btcpay_greenfield_py/releases/tag/v1.0.0
