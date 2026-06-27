"""Truly public smoke tests — no auth required.

The ONLY endpoint on a default BTCPay Server instance that accepts fully
anonymous requests is GET /api/v1/health. The /misc/* metadata endpoints are
marked as unauthenticated in the OpenAPI spec, but the testnet.demo.btcpayserver.org
deployment returns 401 for them in practice — they live behind the same login
wall as everything else.

If you want broader smoke coverage without secrets, run a local BTCPay Server
in regtest (where /misc/* ARE public) and point BTCPAY_HOST at it.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.network


def test_health(unauth_client) -> None:
    from btcpay_greenfield_py.api.health.health_get_health import sync_detailed

    with unauth_client as c:
        r = sync_detailed(client=c)
    assert r.status_code.value == 200
    assert r.parsed is not None
    assert hasattr(r.parsed, "synchronized")
    assert isinstance(r.parsed.synchronized, bool)
