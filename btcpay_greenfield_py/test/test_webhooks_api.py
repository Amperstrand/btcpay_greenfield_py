# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from btcpay_greenfield_py.api.webhooks_api import WebhooksApi


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_webhooks_create_webhook(self) -> None:
        """Test case for webhooks_create_webhook

        Create a new webhook
        """
        pass

    def test_webhooks_delete_webhook(self) -> None:
        """Test case for webhooks_delete_webhook

        Delete a webhook
        """
        pass

    def test_webhooks_get_webhook(self) -> None:
        """Test case for webhooks_get_webhook

        Get a webhook of a store
        """
        pass

    def test_webhooks_get_webhook_deliveries(self) -> None:
        """Test case for webhooks_get_webhook_deliveries

        Get latest deliveries
        """
        pass

    def test_webhooks_get_webhook_delivery(self) -> None:
        """Test case for webhooks_get_webhook_delivery

        Get a webhook delivery
        """
        pass

    def test_webhooks_get_webhook_delivery_requests(self) -> None:
        """Test case for webhooks_get_webhook_delivery_requests

        Get the delivery's request
        """
        pass

    def test_webhooks_get_webhooks(self) -> None:
        """Test case for webhooks_get_webhooks

        Get webhooks of a store
        """
        pass

    def test_webhooks_redeliver_webhook_delivery(self) -> None:
        """Test case for webhooks_redeliver_webhook_delivery

        Redeliver the delivery
        """
        pass

    def test_webhooks_update_webhook(self) -> None:
        """Test case for webhooks_update_webhook

        Update a webhook
        """
        pass


if __name__ == '__main__':
    unittest.main()
