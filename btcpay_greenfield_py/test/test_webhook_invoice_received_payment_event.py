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

from btcpay_greenfield_py.models.webhook_invoice_received_payment_event import WebhookInvoiceReceivedPaymentEvent

class TestWebhookInvoiceReceivedPaymentEvent(unittest.TestCase):
    """WebhookInvoiceReceivedPaymentEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookInvoiceReceivedPaymentEvent:
        """Test WebhookInvoiceReceivedPaymentEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookInvoiceReceivedPaymentEvent`
        """
        model = WebhookInvoiceReceivedPaymentEvent()
        if include_optional:
            return WebhookInvoiceReceivedPaymentEvent(
                delivery_id = '',
                webhook_id = '',
                original_delivery_id = '',
                is_redelivery = True,
                type = '',
                timestamp = 1592312018,
                store_id = '',
                invoice_id = '',
                metadata = None,
                after_expiration = True,
                payment_method = '',
                payment = btcpay_greenfield_py.models.payment.Payment(
                    id = '', 
                    received_date = null, 
                    value = '', 
                    fee = '', 
                    status = 'Invalid', 
                    destination = '', )
            )
        else:
            return WebhookInvoiceReceivedPaymentEvent(
        )
        """

    def testWebhookInvoiceReceivedPaymentEvent(self):
        """Test WebhookInvoiceReceivedPaymentEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
