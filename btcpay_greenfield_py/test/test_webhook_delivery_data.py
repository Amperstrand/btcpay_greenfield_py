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

from btcpay_greenfield_py.models.webhook_delivery_data import WebhookDeliveryData

class TestWebhookDeliveryData(unittest.TestCase):
    """WebhookDeliveryData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookDeliveryData:
        """Test WebhookDeliveryData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookDeliveryData`
        """
        model = WebhookDeliveryData()
        if include_optional:
            return WebhookDeliveryData(
                id = '',
                timestamp = 1592312018,
                http_code = 1.337,
                error_message = '',
                status = ''
            )
        else:
            return WebhookDeliveryData(
        )
        """

    def testWebhookDeliveryData(self):
        """Test WebhookDeliveryData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
