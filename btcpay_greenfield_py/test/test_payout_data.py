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

from btcpay_greenfield_py.models.payout_data import PayoutData

class TestPayoutData(unittest.TestCase):
    """PayoutData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayoutData:
        """Test PayoutData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayoutData`
        """
        model = PayoutData()
        if include_optional:
            return PayoutData(
                id = '',
                revision = 56,
                pull_payment_id = '',
                var_date = '',
                destination = '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2',
                amount = '10399.18',
                payment_method = '',
                crypto_code = 'BTC',
                payment_method_amount = '1.12300000',
                state = 'AwaitingPayment',
                payment_proof = { },
                metadata = {"source":"Payout created through the API"}
            )
        else:
            return PayoutData(
        )
        """

    def testPayoutData(self):
        """Test PayoutData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
