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

from btcpay_greenfield_py.models.withdrawal_result_data import WithdrawalResultData

class TestWithdrawalResultData(unittest.TestCase):
    """WithdrawalResultData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WithdrawalResultData:
        """Test WithdrawalResultData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WithdrawalResultData`
        """
        model = WithdrawalResultData()
        if include_optional:
            return WithdrawalResultData(
                asset = '',
                payment_method = '',
                ledger_entries = [
                    {"asset":"BTC","qty":"1.23456","type":"Trade"}
                    ],
                withdrawal_id = '',
                account_id = '',
                custodian_code = '',
                status = '',
                transaction_id = '',
                target_address = ''
            )
        else:
            return WithdrawalResultData(
        )
        """

    def testWithdrawalResultData(self):
        """Test WithdrawalResultData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
