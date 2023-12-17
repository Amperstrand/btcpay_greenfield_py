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

from openapi_client.models.webhook_event import WebhookEvent

class TestWebhookEvent(unittest.TestCase):
    """WebhookEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEvent:
        """Test WebhookEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEvent`
        """
        model = WebhookEvent()
        if include_optional:
            return WebhookEvent(
                delivery_id = '',
                webhook_id = '',
                original_delivery_id = '',
                is_redelivery = True,
                type = '',
                timestamp = 1592312018
            )
        else:
            return WebhookEvent(
        )
        """

    def testWebhookEvent(self):
        """Test WebhookEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
