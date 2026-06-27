# Contributing

## Project model

This is a **generator-driven SDK**: the source of truth is the OpenAPI spec
(`swagger.json`) plus a generator config (`openapi-python-client.config.yaml`).
The `btcpay_greenfield_py/` package is the **generated output** — do not edit
files under that directory by hand. Your changes will be lost on the next
regeneration.

The hand-written parts of this repo are:

```
swagger.json                              canonical OpenAPI spec
swagger.public-docs.btcpayserver.org.json archived upstream spec (reference only)
openapi-python-client.config.yaml         package-name override
pyproject.toml                            Poetry + ruff + mypy + pytest config
README.md                                 user-facing docs
LICENSE                                   MIT
examples/                                 runnable example scripts
tests/                                    hand-written tests (NOT generated)
scripts/                                  regen + post-process + CI helpers
.github/workflows/ci.yml                  CI pipeline
```

Everything under `btcpay_greenfield_py/` is regenerated.

## Common workflows

### Update the API spec

When BTCPay Server ships a new Greenfield API version:

1. Capture the new spec from a running BTCPay Server instance:
   ```bash
   curl -o swagger.new.json https://your-btcpay-server/swagger/v1/swagger.json
   ```
2. Replace `swagger.json` with the new capture.
3. Regenerate:
   ```bash
   ./scripts/regenerate.sh
   ```
4. Inspect the diff: `git diff btcpay_greenfield_py/`.
5. If new endpoints appear, add smoke tests under `tests/` and examples under `examples/`.
6. Commit the regenerated package + spec + any new tests/examples.

### Fix a generated-code bug

Generated code has known issues (empty-body parsing, list-response shape
mismatches). These are handled by `scripts/post_process_generated.py`, which
runs automatically after generation. **Do not** patch generated files by hand —
extend the post-processor instead.

1. Identify the pattern in the generated code that's broken.
2. Add a regex + replacement to `scripts/post_process_generated.py`.
3. Add a test case to `tests/test_generated_surface.py`.
4. Run `./scripts/regenerate.sh` to verify the patch applies cleanly.
5. Run `./scripts/regenerate-and-diff.sh` to verify the drift check passes.

### Add an example script

1. Create `examples/your_example.py`.
2. Use `from config import get_client, get_store_id` for shared setup.
3. Load all secrets from environment variables — never hard-code keys.
4. Default `BTCPAY_HOST` to `https://testnet.demo.btcpayserver.org`.
5. Handle error responses gracefully (see `examples/create_invoice.py`).
6. Run `python3 -m ruff check examples/your_example.py`.

### Add a test

- **Structural / no-network tests** go in `tests/test_generated_surface.py`.
- **Public endpoint tests** (no auth) go in `tests/test_smoke_public.py`.
- **Authenticated tests** go in `tests/test_smoke_authed.py` — use the
  `authed_client` and `store_id` fixtures from `tests/conftest.py`, which
  auto-skip if creds are missing.

## CI

`.github/workflows/ci.yml` runs 6 jobs on every push and PR:

| Job | What |
|---|---|
| `regenerate-check` | `swagger.json` + config reproduces the committed package exactly |
| `lint` | ruff, Python 3.11/3.12/3.13/3.14 matrix |
| `typecheck` | mypy on examples + tests (Python 3.12) |
| `generated-surface` | Meta-test: every endpoint module exposes the right variants |
| `smoke-public` | `GET /api/v1/health` against testnet (no secrets) |
| `smoke-authed` | Auto-registers a testnet account + runs authed round-trip tests |

The `smoke-authed` job uses `scripts/setup_testnet_creds.py` to auto-register
a throwaway account on `testnet.demo.btcpayserver.org` each run — no secrets
needed.

## Release

1. Bump `version` in `pyproject.toml`.
2. Update `swagger.json` if a new BTCPay version shipped.
3. Run `./scripts/regenerate.sh`.
4. Run `pytest tests/ -v` to verify.
5. `poetry build && poetry publish`.
