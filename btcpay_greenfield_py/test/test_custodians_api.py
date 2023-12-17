# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.custodians_api import CustodiansApi


class TestCustodiansApi(unittest.TestCase):
    """CustodiansApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CustodiansApi()

    def tearDown(self) -> None:
        pass

    def test_custodians_add_store_custodian_account(self) -> None:
        """Test case for custodians_add_store_custodian_account

        Add a custodial account to a store.
        """
        pass

    def test_custodians_delete_store_custodian_account(self) -> None:
        """Test case for custodians_delete_store_custodian_account

        Delete store custodian account
        """
        pass

    def test_custodians_get_store_custodian_account(self) -> None:
        """Test case for custodians_get_store_custodian_account

        Get store custodian account
        """
        pass

    def test_custodians_get_store_custodian_account_deposit_address(self) -> None:
        """Test case for custodians_get_store_custodian_account_deposit_address

        Get a deposit address for custodian
        """
        pass

    def test_custodians_get_store_custodian_account_trade_quote(self) -> None:
        """Test case for custodians_get_store_custodian_account_trade_quote

        Get quote for trading one asset for another
        """
        pass

    def test_custodians_get_store_custodian_account_withdrawal_info(self) -> None:
        """Test case for custodians_get_store_custodian_account_withdrawal_info

        Get withdrawal info
        """
        pass

    def test_custodians_get_store_custodian_accounts(self) -> None:
        """Test case for custodians_get_store_custodian_accounts

        List store custodian accounts
        """
        pass

    def test_custodians_get_supported_custodians(self) -> None:
        """Test case for custodians_get_supported_custodians

        List supported custodians
        """
        pass

    def test_custodians_simulate_withdraw_from_store_custodian_account(self) -> None:
        """Test case for custodians_simulate_withdraw_from_store_custodian_account

        Simulate a withdrawal
        """
        pass

    def test_custodians_store_custodian_account_trade_market(self) -> None:
        """Test case for custodians_store_custodian_account_trade_market

        Trade one asset for another
        """
        pass

    def test_custodians_update_store_custodian_account(self) -> None:
        """Test case for custodians_update_store_custodian_account

        Update custodial account
        """
        pass

    def test_custodians_withdraw_from_store_custodian_account(self) -> None:
        """Test case for custodians_withdraw_from_store_custodian_account

        Withdraw to store wallet
        """
        pass


if __name__ == '__main__':
    unittest.main()