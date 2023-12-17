# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from btcpay_greenfield_py.api.pull_payments_public_api import PullPaymentsPublicApi


class TestPullPaymentsPublicApi(unittest.TestCase):
    """PullPaymentsPublicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PullPaymentsPublicApi()

    def tearDown(self) -> None:
        pass

    def test_pull_payments_create_payout(self) -> None:
        """Test case for pull_payments_create_payout

        Create Payout
        """
        pass

    def test_pull_payments_get_payout(self) -> None:
        """Test case for pull_payments_get_payout

        Get Payout
        """
        pass

    def test_pull_payments_get_payouts(self) -> None:
        """Test case for pull_payments_get_payouts

        Get Payouts
        """
        pass

    def test_pull_payments_get_pull_payment(self) -> None:
        """Test case for pull_payments_get_pull_payment

        Get Pull Payment
        """
        pass

    def test_pull_payments_get_pull_payment_lnurl(self) -> None:
        """Test case for pull_payments_get_pull_payment_lnurl

        Get Pull Payment LNURL details
        """
        pass


if __name__ == '__main__':
    unittest.main()
