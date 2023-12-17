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

from openapi_client.models.on_chain_payment_method_data_with_sensitive_data import OnChainPaymentMethodDataWithSensitiveData

class TestOnChainPaymentMethodDataWithSensitiveData(unittest.TestCase):
    """OnChainPaymentMethodDataWithSensitiveData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnChainPaymentMethodDataWithSensitiveData:
        """Test OnChainPaymentMethodDataWithSensitiveData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnChainPaymentMethodDataWithSensitiveData`
        """
        model = OnChainPaymentMethodDataWithSensitiveData()
        if include_optional:
            return OnChainPaymentMethodDataWithSensitiveData(
                derivation_scheme = 'xpub...',
                label = '',
                account_key_path = 'abcd82a1/84'/0'/0'',
                crypto_code = '',
                enabled = True,
                payment_method = '',
                mnemonic = ''
            )
        else:
            return OnChainPaymentMethodDataWithSensitiveData(
        )
        """

    def testOnChainPaymentMethodDataWithSensitiveData(self):
        """Test OnChainPaymentMethodDataWithSensitiveData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
