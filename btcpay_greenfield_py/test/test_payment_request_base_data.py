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

from openapi_client.models.payment_request_base_data import PaymentRequestBaseData

class TestPaymentRequestBaseData(unittest.TestCase):
    """PaymentRequestBaseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentRequestBaseData:
        """Test PaymentRequestBaseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentRequestBaseData`
        """
        model = PaymentRequestBaseData()
        if include_optional:
            return PaymentRequestBaseData(
                amount = '',
                title = '',
                currency = '',
                email = '',
                description = '',
                expiry_date = 1592312018,
                embedded_css = '',
                custom_css_link = '',
                allow_custom_payment_amounts = True,
                form_id = '',
                form_response = openapi_client.models.form_response.formResponse()
            )
        else:
            return PaymentRequestBaseData(
        )
        """

    def testPaymentRequestBaseData(self):
        """Test PaymentRequestBaseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
