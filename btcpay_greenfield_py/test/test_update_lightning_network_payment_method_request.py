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

from btcpay_greenfield_py.models.update_lightning_network_payment_method_request import UpdateLightningNetworkPaymentMethodRequest

class TestUpdateLightningNetworkPaymentMethodRequest(unittest.TestCase):
    """UpdateLightningNetworkPaymentMethodRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateLightningNetworkPaymentMethodRequest:
        """Test UpdateLightningNetworkPaymentMethodRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateLightningNetworkPaymentMethodRequest`
        """
        model = UpdateLightningNetworkPaymentMethodRequest()
        if include_optional:
            return UpdateLightningNetworkPaymentMethodRequest(
                connection_string = 'type=clightning;server=...',
                enabled = True
            )
        else:
            return UpdateLightningNetworkPaymentMethodRequest(
        )
        """

    def testUpdateLightningNetworkPaymentMethodRequest(self):
        """Test UpdateLightningNetworkPaymentMethodRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
