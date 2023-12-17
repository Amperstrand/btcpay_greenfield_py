# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from btcpay_greenfield_py.api.pull_payments_management_api import PullPaymentsManagementApi


class TestPullPaymentsManagementApi(unittest.TestCase):
    """PullPaymentsManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PullPaymentsManagementApi()

    def tearDown(self) -> None:
        pass

    def test_pull_payments_archive_pull_payment(self) -> None:
        """Test case for pull_payments_archive_pull_payment

        Archive a pull payment
        """
        pass

    def test_pull_payments_create_pull_payment(self) -> None:
        """Test case for pull_payments_create_pull_payment

        Create a new pull payment
        """
        pass

    def test_pull_payments_get_pull_payments(self) -> None:
        """Test case for pull_payments_get_pull_payments

        Get store's pull payments
        """
        pass


if __name__ == '__main__':
    unittest.main()
