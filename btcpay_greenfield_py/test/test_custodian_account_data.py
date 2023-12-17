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

from btcpay_greenfield_py.models.custodian_account_data import CustodianAccountData

class TestCustodianAccountData(unittest.TestCase):
    """CustodianAccountData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustodianAccountData:
        """Test CustodianAccountData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustodianAccountData`
        """
        model = CustodianAccountData()
        if include_optional:
            return CustodianAccountData(
                id = '',
                store_id = '',
                custodian_code = '',
                name = '',
                asset_balances = [
                    {"asset":"BTC","qty":"1.23456"}
                    ],
                config = None
            )
        else:
            return CustodianAccountData(
        )
        """

    def testCustodianAccountData(self):
        """Test CustodianAccountData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
