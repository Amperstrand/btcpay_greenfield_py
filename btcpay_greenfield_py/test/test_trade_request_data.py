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

from openapi_client.models.trade_request_data import TradeRequestData

class TestTradeRequestData(unittest.TestCase):
    """TradeRequestData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TradeRequestData:
        """Test TradeRequestData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TradeRequestData`
        """
        model = TradeRequestData()
        if include_optional:
            return TradeRequestData(
                from_asset = '',
                to_asset = '',
                qty = None
            )
        else:
            return TradeRequestData(
        )
        """

    def testTradeRequestData(self):
        """Test TradeRequestData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
