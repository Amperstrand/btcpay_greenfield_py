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

from btcpay_greenfield_py.models.create_point_of_sale_app_request import CreatePointOfSaleAppRequest

class TestCreatePointOfSaleAppRequest(unittest.TestCase):
    """CreatePointOfSaleAppRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePointOfSaleAppRequest:
        """Test CreatePointOfSaleAppRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePointOfSaleAppRequest`
        """
        model = CreatePointOfSaleAppRequest()
        if include_optional:
            return CreatePointOfSaleAppRequest(
                app_name = '',
                title = '',
                description = '',
                template = '',
                default_view = 'Cart',
                currency = 'BTC',
                show_custom_amount = True,
                show_discount = True,
                enable_tips = True,
                custom_amount_pay_button_text = 'Pay',
                fixed_amount_pay_button_text = 'Buy for {PRICE_HERE}',
                tip_text = 'Do you want to leave a tip?',
                custom_css_link = '',
                embedded_css = '',
                notification_url = '',
                redirect_url = '',
                redirect_automatically = True,
                requires_refund_email = True,
                checkout_type = 'V1',
                form_id = ''
            )
        else:
            return CreatePointOfSaleAppRequest(
        )
        """

    def testCreatePointOfSaleAppRequest(self):
        """Test CreatePointOfSaleAppRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
