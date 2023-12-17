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

from btcpay_greenfield_py.models.lightning_node_balance_data import LightningNodeBalanceData

class TestLightningNodeBalanceData(unittest.TestCase):
    """LightningNodeBalanceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LightningNodeBalanceData:
        """Test LightningNodeBalanceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LightningNodeBalanceData`
        """
        model = LightningNodeBalanceData()
        if include_optional:
            return LightningNodeBalanceData(
                onchain = None,
                offchain = None
            )
        else:
            return LightningNodeBalanceData(
        )
        """

    def testLightningNodeBalanceData(self):
        """Test LightningNodeBalanceData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
