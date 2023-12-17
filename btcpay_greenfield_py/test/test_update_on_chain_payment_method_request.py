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

from btcpay_greenfield_py.models.update_on_chain_payment_method_request import UpdateOnChainPaymentMethodRequest

class TestUpdateOnChainPaymentMethodRequest(unittest.TestCase):
    """UpdateOnChainPaymentMethodRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOnChainPaymentMethodRequest:
        """Test UpdateOnChainPaymentMethodRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOnChainPaymentMethodRequest`
        """
        model = UpdateOnChainPaymentMethodRequest()
        if include_optional:
            return UpdateOnChainPaymentMethodRequest(
                derivation_scheme = 'xpub...',
                label = '',
                account_key_path = 'abcd82a1/84'/0'/0'',
                enabled = True
            )
        else:
            return UpdateOnChainPaymentMethodRequest(
        )
        """

    def testUpdateOnChainPaymentMethodRequest(self):
        """Test UpdateOnChainPaymentMethodRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
