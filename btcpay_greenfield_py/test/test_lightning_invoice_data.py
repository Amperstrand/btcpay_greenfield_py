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

from openapi_client.models.lightning_invoice_data import LightningInvoiceData

class TestLightningInvoiceData(unittest.TestCase):
    """LightningInvoiceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LightningInvoiceData:
        """Test LightningInvoiceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LightningInvoiceData`
        """
        model = LightningInvoiceData()
        if include_optional:
            return LightningInvoiceData(
                id = '',
                status = 'Expired',
                bolt11 = '',
                paid_at = 1592312018,
                expires_at = 1592312018,
                amount = '',
                amount_received = '',
                payment_hash = '',
                preimage = '',
                custom_records = None
            )
        else:
            return LightningInvoiceData(
        )
        """

    def testLightningInvoiceData(self):
        """Test LightningInvoiceData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()