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

from openapi_client.models.invoice_data_base_receipt import InvoiceDataBaseReceipt

class TestInvoiceDataBaseReceipt(unittest.TestCase):
    """InvoiceDataBaseReceipt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDataBaseReceipt:
        """Test InvoiceDataBaseReceipt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDataBaseReceipt`
        """
        model = InvoiceDataBaseReceipt()
        if include_optional:
            return InvoiceDataBaseReceipt(
                enabled = True,
                show_qr = True,
                show_payments = True
            )
        else:
            return InvoiceDataBaseReceipt(
        )
        """

    def testInvoiceDataBaseReceipt(self):
        """Test InvoiceDataBaseReceipt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
