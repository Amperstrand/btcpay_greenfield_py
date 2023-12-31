# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from btcpay_greenfield_py.api.stores_email_api import StoresEmailApi


class TestStoresEmailApi(unittest.TestCase):
    """StoresEmailApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StoresEmailApi()

    def tearDown(self) -> None:
        pass

    def test_stores_get_store_email_settings(self) -> None:
        """Test case for stores_get_store_email_settings

        Get store email settings
        """
        pass

    def test_stores_send_store_email(self) -> None:
        """Test case for stores_send_store_email

        Send an email for a store
        """
        pass

    def test_stores_update_store_email_settings(self) -> None:
        """Test case for stores_update_store_email_settings

        Update store email settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
