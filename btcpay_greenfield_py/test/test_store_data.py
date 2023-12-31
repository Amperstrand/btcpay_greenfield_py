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

from btcpay_greenfield_py.models.store_data import StoreData

class TestStoreData(unittest.TestCase):
    """StoreData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StoreData:
        """Test StoreData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StoreData`
        """
        model = StoreData()
        if include_optional:
            return StoreData(
                name = '',
                website = '',
                support_url = '',
                default_currency = 'USD',
                invoice_expiration = None,
                display_expiration_timer = None,
                monitoring_expiration = None,
                speed_policy = 'HighSpeed',
                lightning_description_template = '',
                payment_tolerance = 0,
                archived = True,
                anyone_can_create_invoice = True,
                requires_refund_email = True,
                checkout_type = 'V1',
                receipt = None,
                lightning_amount_in_satoshi = True,
                lightning_private_route_hints = True,
                on_chain_with_ln_invoice_fallback = True,
                redirect_automatically = True,
                show_recommended_fee = True,
                recommended_fee_block_target = 56,
                default_lang = 'en',
                custom_logo = '',
                custom_css = '',
                html_title = '',
                network_fee_mode = 'Always',
                pay_join_enabled = True,
                auto_detect_language = True,
                show_pay_in_wallet_button = True,
                show_store_header = True,
                celebrate_payment = True,
                play_sound_on_payment = True,
                lazy_payment_methods = True,
                default_payment_method = '',
                payment_method_criteria = [
                    btcpay_greenfield_py.models.payment_method_criteria_data.PaymentMethodCriteriaData(
                        payment_method = null, 
                        currency_code = 'USD', 
                        amount = '', 
                        above = True, )
                    ],
                id = ''
            )
        else:
            return StoreData(
        )
        """

    def testStoreData(self):
        """Test StoreData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
