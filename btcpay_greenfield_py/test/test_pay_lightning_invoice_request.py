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

from openapi_client.models.pay_lightning_invoice_request import PayLightningInvoiceRequest

class TestPayLightningInvoiceRequest(unittest.TestCase):
    """PayLightningInvoiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayLightningInvoiceRequest:
        """Test PayLightningInvoiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayLightningInvoiceRequest`
        """
        model = PayLightningInvoiceRequest()
        if include_optional:
            return PayLightningInvoiceRequest(
                bolt11 = '',
                amount = '',
                max_fee_percent = '6.15',
                max_fee_flat = '21',
                send_timeout = None
            )
        else:
            return PayLightningInvoiceRequest(
        )
        """

    def testPayLightningInvoiceRequest(self):
        """Test PayLightningInvoiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()