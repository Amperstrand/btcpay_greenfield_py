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

from openapi_client.models.lightning_node_balance_data_onchain import LightningNodeBalanceDataOnchain

class TestLightningNodeBalanceDataOnchain(unittest.TestCase):
    """LightningNodeBalanceDataOnchain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LightningNodeBalanceDataOnchain:
        """Test LightningNodeBalanceDataOnchain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LightningNodeBalanceDataOnchain`
        """
        model = LightningNodeBalanceDataOnchain()
        if include_optional:
            return LightningNodeBalanceDataOnchain(
                confirmed = '',
                unconfirmed = '',
                reserved = ''
            )
        else:
            return LightningNodeBalanceDataOnchain(
        )
        """

    def testLightningNodeBalanceDataOnchain(self):
        """Test LightningNodeBalanceDataOnchain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()