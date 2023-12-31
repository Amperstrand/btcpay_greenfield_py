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

from btcpay_greenfield_py.models.lightning_network_payment_method_data import LightningNetworkPaymentMethodData

class TestLightningNetworkPaymentMethodData(unittest.TestCase):
    """LightningNetworkPaymentMethodData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LightningNetworkPaymentMethodData:
        """Test LightningNetworkPaymentMethodData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LightningNetworkPaymentMethodData`
        """
        model = LightningNetworkPaymentMethodData()
        if include_optional:
            return LightningNetworkPaymentMethodData(
                connection_string = 'type=clightning;server=...',
                enabled = True,
                crypto_code = '',
                payment_method = ''
            )
        else:
            return LightningNetworkPaymentMethodData(
        )
        """

    def testLightningNetworkPaymentMethodData(self):
        """Test LightningNetworkPaymentMethodData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
