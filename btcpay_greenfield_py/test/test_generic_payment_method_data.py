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

from btcpay_greenfield_py.models.generic_payment_method_data import GenericPaymentMethodData

class TestGenericPaymentMethodData(unittest.TestCase):
    """GenericPaymentMethodData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericPaymentMethodData:
        """Test GenericPaymentMethodData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericPaymentMethodData`
        """
        model = GenericPaymentMethodData()
        if include_optional:
            return GenericPaymentMethodData(
                enabled = True,
                crypto_code = '',
                data = btcpay_greenfield_py.models.generic_payment_method_data_data.GenericPaymentMethodData_data()
            )
        else:
            return GenericPaymentMethodData(
        )
        """

    def testGenericPaymentMethodData(self):
        """Test GenericPaymentMethodData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
