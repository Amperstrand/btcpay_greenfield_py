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

from btcpay_greenfield_py.models.invoice_data_base_checkout import InvoiceDataBaseCheckout

class TestInvoiceDataBaseCheckout(unittest.TestCase):
    """InvoiceDataBaseCheckout unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDataBaseCheckout:
        """Test InvoiceDataBaseCheckout
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDataBaseCheckout`
        """
        model = InvoiceDataBaseCheckout()
        if include_optional:
            return InvoiceDataBaseCheckout(
                speed_policy = 'HighSpeed',
                payment_methods = [
                    ''
                    ],
                default_payment_method = '',
                lazy_payment_methods = True,
                expiration_minutes = None,
                monitoring_minutes = None,
                payment_tolerance = 0,
                redirect_url = '',
                redirect_automatically = True,
                requires_refund_email = True,
                checkout_type = ERROR_TO_EXAMPLE_VALUE,
                default_language = ''
            )
        else:
            return InvoiceDataBaseCheckout(
        )
        """

    def testInvoiceDataBaseCheckout(self):
        """Test InvoiceDataBaseCheckout"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
