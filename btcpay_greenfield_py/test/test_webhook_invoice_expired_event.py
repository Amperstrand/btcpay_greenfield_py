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

from openapi_client.models.webhook_invoice_expired_event import WebhookInvoiceExpiredEvent

class TestWebhookInvoiceExpiredEvent(unittest.TestCase):
    """WebhookInvoiceExpiredEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookInvoiceExpiredEvent:
        """Test WebhookInvoiceExpiredEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookInvoiceExpiredEvent`
        """
        model = WebhookInvoiceExpiredEvent()
        if include_optional:
            return WebhookInvoiceExpiredEvent(
                delivery_id = '',
                webhook_id = '',
                original_delivery_id = '',
                is_redelivery = True,
                type = '',
                timestamp = 1592312018,
                store_id = '',
                invoice_id = '',
                metadata = None,
                partially_paid = True
            )
        else:
            return WebhookInvoiceExpiredEvent(
        )
        """

    def testWebhookInvoiceExpiredEvent(self):
        """Test WebhookInvoiceExpiredEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
