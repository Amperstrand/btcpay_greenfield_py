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

from btcpay_greenfield_py.models.custodians_get_store_custodian_account_withdrawal_info403_response import CustodiansGetStoreCustodianAccountWithdrawalInfo403Response

class TestCustodiansGetStoreCustodianAccountWithdrawalInfo403Response(unittest.TestCase):
    """CustodiansGetStoreCustodianAccountWithdrawalInfo403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustodiansGetStoreCustodianAccountWithdrawalInfo403Response:
        """Test CustodiansGetStoreCustodianAccountWithdrawalInfo403Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustodiansGetStoreCustodianAccountWithdrawalInfo403Response`
        """
        model = CustodiansGetStoreCustodianAccountWithdrawalInfo403Response()
        if include_optional:
            return CustodiansGetStoreCustodianAccountWithdrawalInfo403Response(
            )
        else:
            return CustodiansGetStoreCustodianAccountWithdrawalInfo403Response(
        )
        """

    def testCustodiansGetStoreCustodianAccountWithdrawalInfo403Response(self):
        """Test CustodiansGetStoreCustodianAccountWithdrawalInfo403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
