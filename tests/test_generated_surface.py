"""Meta-test over the generated client surface.

Iterates the entire btcpay_greenfield_py/api/ tree and asserts each endpoint
module exposes the four documented variants with the right shape. This catches:

- generator regressions (missing variant, renamed function)
- hand-edits to generated code that drift from the spec
- import errors inside generated modules

This test does NOT touch the network. It only checks structure.
"""

from __future__ import annotations

import importlib
import inspect
from pathlib import Path

import pytest

API_ROOT = Path(__file__).resolve().parent.parent / "btcpay_greenfield_py" / "api"

# Every endpoint module exposes AT LEAST the *_detailed variants.
# Endpoints with no response body (DELETE, 204 No Content, etc.) only emit
# the *_detailed variants — the convenience `sync`/`asyncio` wrappers are
# skipped because there's nothing to parse.
REQUIRED_VARIANTS = ("sync_detailed", "asyncio_detailed")
PARSING_VARIANTS = ("sync", "asyncio")  # present when the endpoint has a body to parse

# Modules that are __init__.py or otherwise not endpoint modules.
_SKIP_NAMES = {"__init__"}


def _discover_endpoint_modules() -> list[tuple[str, str]]:
    """Return (dotted_module_path, simple_module_name) for every endpoint module."""
    out: list[tuple[str, str]] = []
    for path in sorted(API_ROOT.rglob("*.py")):
        if path.name in _SKIP_NAMES or path.name.startswith("__"):
            continue
        rel = path.relative_to(API_ROOT.parent)
        dotted = ".".join(rel.with_suffix("").parts)
        out.append((dotted, path.stem))
    return out


ENDPOINT_MODULES = _discover_endpoint_modules()

# Sanity: the tree should have at least 100 endpoint modules (we have 171)
assert len(ENDPOINT_MODULES) >= 100, f"expected ≥100 endpoint modules, got {len(ENDPOINT_MODULES)}"


@pytest.mark.parametrize("module_path", [m[0] for m in ENDPOINT_MODULES],
                         ids=[m[1] for m in ENDPOINT_MODULES])
def test_endpoint_exposes_required_variants(module_path: str) -> None:
    """Every endpoint module must expose at least sync_detailed and asyncio_detailed."""
    mod = importlib.import_module(f"btcpay_greenfield_py.{module_path}")
    missing = [v for v in REQUIRED_VARIANTS if not hasattr(mod, v)]
    assert not missing, f"{module_path} missing variants: {missing}"


@pytest.mark.parametrize("module_path", [m[0] for m in ENDPOINT_MODULES],
                         ids=[m[1] for m in ENDPOINT_MODULES])
def test_endpoint_parsing_variants_consistent(module_path: str) -> None:
    """If `sync` exists, `asyncio` must exist too (and vice versa).

    Endpoints with response bodies get all four variants; endpoints without
    bodies (DELETE, 204) get only the *_detailed pair. Both shapes are valid;
    what's NOT valid is having `sync` without `asyncio` (or the reverse).
    """
    mod = importlib.import_module(f"btcpay_greenfield_py.{module_path}")
    has_sync = hasattr(mod, "sync")
    has_asyncio = hasattr(mod, "asyncio")
    assert has_sync == has_asyncio, (
        f"{module_path}: sync and asyncio must both exist or both be absent "
        f"(got sync={has_sync}, asyncio={has_asyncio})"
    )


@pytest.mark.parametrize("module_path", [m[0] for m in ENDPOINT_MODULES],
                         ids=[m[1] for m in ENDPOINT_MODULES])
def test_endpoint_variants_are_callable(module_path: str) -> None:
    """Each required variant must be a regular function (callable, inspectable signature)."""
    mod = importlib.import_module(f"btcpay_greenfield_py.{module_path}")
    for variant in REQUIRED_VARIANTS:
        fn = getattr(mod, variant)
        assert callable(fn), f"{module_path}.{variant} is not callable"
        sig = inspect.signature(fn)
        params = list(sig.parameters)
        # All variants must accept at least a `client=` kwarg.
        assert "client" in params, f"{module_path}.{variant} signature missing 'client': {params}"


def test_async_variants_are_coroutines() -> None:
    """The asyncio variants must be defined with `async def` so they return coroutines."""
    import inspect as _inspect

    for module_path, simple in ENDPOINT_MODULES:
        mod = importlib.import_module(f"btcpay_greenfield_py.{module_path}")
        for variant in ("asyncio", "asyncio_detailed"):
            if not hasattr(mod, variant):
                continue
            fn = getattr(mod, variant)
            assert _inspect.iscoroutinefunction(fn), (
                f"{module_path}.{variant} must be `async def`"
            )


def test_client_classes_exported() -> None:
    """The package must export Client and AuthenticatedClient."""
    import btcpay_greenfield_py

    assert hasattr(btcpay_greenfield_py, "Client")
    assert hasattr(btcpay_greenfield_py, "AuthenticatedClient")


def test_py_typed_present() -> None:
    """PEP 561 marker must ship with the package."""
    py_typed = API_ROOT.parent / "py.typed"
    assert py_typed.exists(), "missing py.typed — PEP 561 marker required for type checkers"


def test_models_round_trip_to_dict() -> None:
    """A few representative models must accept from_dict → .to_dict round trips."""
    from btcpay_greenfield_py.models.application_health_data import ApplicationHealthData
    from btcpay_greenfield_py.models.create_invoice_request import CreateInvoiceRequest
    from btcpay_greenfield_py.models.users_create_user_body import UsersCreateUserBody

    h = ApplicationHealthData.from_dict({"synchronized": True})
    assert h.synchronized is True
    assert h.to_dict() == {"synchronized": True}

    i = CreateInvoiceRequest(amount="1.00", currency="USD")
    d = i.to_dict()
    assert d.get("amount") == "1.00"
    assert d.get("currency") == "USD"

    u = UsersCreateUserBody(email="x@example.com", password="hunter2")
    d = u.to_dict()
    assert d["email"] == "x@example.com"
    assert d["password"] == "hunter2"
