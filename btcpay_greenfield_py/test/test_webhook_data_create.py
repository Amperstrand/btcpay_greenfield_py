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

from openapi_client.models.webhook_data_create import WebhookDataCreate

class TestWebhookDataCreate(unittest.TestCase):
    """WebhookDataCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookDataCreate:
        """Test WebhookDataCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookDataCreate`
        """
        model = WebhookDataCreate()
        if include_optional:
            return WebhookDataCreate(
                enabled = True,
                automatic_redelivery = True,
                url = '',
                authorized_events = openapi_client.models.webhook_data_base_authorized_events.WebhookDataBase_authorizedEvents(
                    everything = True, 
                    specific_events = [
                        ''
                        ], ),
                secret = ''
            )
        else:
            return WebhookDataCreate(
        )
        """

    def testWebhookDataCreate(self):
        """Test WebhookDataCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()