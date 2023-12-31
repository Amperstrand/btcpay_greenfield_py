# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from btcpay_greenfield_py.models.pull_payments_create_pull_payment_request import PullPaymentsCreatePullPaymentRequest

class TestPullPaymentsCreatePullPaymentRequest(unittest.TestCase):
    """PullPaymentsCreatePullPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PullPaymentsCreatePullPaymentRequest:
        """Test PullPaymentsCreatePullPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PullPaymentsCreatePullPaymentRequest`
        """
        model = PullPaymentsCreatePullPaymentRequest()
        if include_optional:
            return PullPaymentsCreatePullPaymentRequest(
                name = '',
                description = '',
                amount = '0.1',
                currency = 'BTC',
                period = 604800,
                bolt11_expiration = '30',
                auto_approve_claims = False,
                starts_at = 1592312018,
                expires_at = 1593129600,
                payment_methods = [
                    'BTC'
                    ]
            )
        else:
            return PullPaymentsCreatePullPaymentRequest(
        )
        """

    def testPullPaymentsCreatePullPaymentRequest(self):
        """Test PullPaymentsCreatePullPaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
