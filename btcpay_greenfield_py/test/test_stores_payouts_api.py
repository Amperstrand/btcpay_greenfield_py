# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.stores_payouts_api import StoresPayoutsApi


class TestStoresPayoutsApi(unittest.TestCase):
    """StoresPayoutsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StoresPayoutsApi()

    def tearDown(self) -> None:
        pass

    def test_get_store_payout(self) -> None:
        """Test case for get_store_payout

        Get Payout
        """
        pass

    def test_payouts_create_payout_through_store(self) -> None:
        """Test case for payouts_create_payout_through_store

        Create Payout
        """
        pass

    def test_pull_payments_approve_payout(self) -> None:
        """Test case for pull_payments_approve_payout

        Approve Payout
        """
        pass

    def test_pull_payments_cancel_payout(self) -> None:
        """Test case for pull_payments_cancel_payout

        Cancel Payout
        """
        pass

    def test_pull_payments_get_store_payouts(self) -> None:
        """Test case for pull_payments_get_store_payouts

        Get Store Payouts
        """
        pass

    def test_pull_payments_mark_payout(self) -> None:
        """Test case for pull_payments_mark_payout

        Mark Payout
        """
        pass

    def test_pull_payments_mark_payout_paid(self) -> None:
        """Test case for pull_payments_mark_payout_paid

        Mark Payout as Paid
        """
        pass


if __name__ == '__main__':
    unittest.main()
