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

from btcpay_greenfield_py.models.create_invoice_request import CreateInvoiceRequest

class TestCreateInvoiceRequest(unittest.TestCase):
    """CreateInvoiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInvoiceRequest:
        """Test CreateInvoiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInvoiceRequest`
        """
        model = CreateInvoiceRequest()
        if include_optional:
            return CreateInvoiceRequest(
                metadata = {"orderId":"pos-app_346KRC5BjXXXo8cRFKwTBmdR6ZJ4","orderUrl":"https://localhost:14142/apps/346KRC5BjXXXo8cRFKwTBmdR6ZJ4/pos","itemDesc":"Tea shop","posData":{"tip":0.48,"cart":[{"id":"pu erh","count":1,"image":"~/img/pos-sample/pu-erh.jpg","price":{"type":2,"value":2,"formatted":"$2.00"},"title":"Pu Erh","inventory":null},{"id":"rooibos","count":1,"image":"~/img/pos-sample/rooibos.jpg","price":{"type":2,"value":1.2,"formatted":"$1.20"},"title":"Rooibos","inventory":null}],"total":3.68,"subTotal":3.2,"customAmount":0,"discountAmount":0,"discountPercentage":0},"receiptData":{"Tip":"$0.48","Cart":{"Pu Erh":"$2.00 x 1 = $2.00","Rooibos":"$1.20 x 1 = $1.20"}}},
                checkout = None,
                receipt = None,
                amount = '5.00',
                currency = 'USD',
                additional_search_terms = [
                    ''
                    ]
            )
        else:
            return CreateInvoiceRequest(
        )
        """

    def testCreateInvoiceRequest(self):
        """Test CreateInvoiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
