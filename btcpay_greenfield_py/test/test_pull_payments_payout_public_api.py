# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.pull_payments_payout_public_api import PullPaymentsPayoutPublicApi


class TestPullPaymentsPayoutPublicApi(unittest.TestCase):
    """PullPaymentsPayoutPublicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PullPaymentsPayoutPublicApi()

    def tearDown(self) -> None:
        pass

    def test_pull_payments_get_payout(self) -> None:
        """Test case for pull_payments_get_payout

        Get Payout
        """
        pass


if __name__ == '__main__':
    unittest.main()
