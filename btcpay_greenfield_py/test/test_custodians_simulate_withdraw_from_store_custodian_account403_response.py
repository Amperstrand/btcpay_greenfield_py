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

from openapi_client.models.custodians_simulate_withdraw_from_store_custodian_account403_response import CustodiansSimulateWithdrawFromStoreCustodianAccount403Response

class TestCustodiansSimulateWithdrawFromStoreCustodianAccount403Response(unittest.TestCase):
    """CustodiansSimulateWithdrawFromStoreCustodianAccount403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustodiansSimulateWithdrawFromStoreCustodianAccount403Response:
        """Test CustodiansSimulateWithdrawFromStoreCustodianAccount403Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustodiansSimulateWithdrawFromStoreCustodianAccount403Response`
        """
        model = CustodiansSimulateWithdrawFromStoreCustodianAccount403Response()
        if include_optional:
            return CustodiansSimulateWithdrawFromStoreCustodianAccount403Response(
            )
        else:
            return CustodiansSimulateWithdrawFromStoreCustodianAccount403Response(
        )
        """

    def testCustodiansSimulateWithdrawFromStoreCustodianAccount403Response(self):
        """Test CustodiansSimulateWithdrawFromStoreCustodianAccount403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
