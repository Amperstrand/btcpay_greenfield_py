"""Create a new BTCPay Server user (server admin only).

Note: This endpoint requires server-administrator API key permissions
(``btcpay.server.cancreateuser``). It will not work against the public
testnet.demo.btcpayserver.org demo because demo accounts are not admins.
Run this against your own self-hosted BTCPay Server.

Required env vars:
    BTCPAY_API_KEY   admin API key with btcpay.server.cancreateuser permission

Optional:
    BTCPAY_HOST      defaults to https://testnet.demo.btcpayserver.org

Usage:
    BTCPAY_API_KEY=<admin-key> python examples/create_user.py
"""

from __future__ import annotations

import os
import sys
from pprint import pprint

from config import get_client

from btcpay_greenfield_py.api.users.users_create_user import sync as create_user
from btcpay_greenfield_py.models.users_create_user_body import UsersCreateUserBody


def main() -> None:
    email = os.environ.get("NEW_USER_EMAIL", "newuser@example.com")
    password = os.environ.get("NEW_USER_PASSWORD", "Tr0ub4dour&3")
    is_admin = os.environ.get("NEW_USER_IS_ADMIN", "0") in {"1", "true", "yes"}

    client = get_client()

    with client as client:
        result = create_user(
            client=client,
            body=UsersCreateUserBody(
                email=email,
                password=password,
                is_administrator=is_admin,
            ),
        )

    if result is None:
        print("server returned no body — verify the API key has admin permissions", file=sys.stderr)
        sys.exit(1)

    pprint(result.to_dict())


if __name__ == "__main__":
    main()
