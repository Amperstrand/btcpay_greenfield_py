# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.stores_rates_config_api import StoresRatesConfigApi


class TestStoresRatesConfigApi(unittest.TestCase):
    """StoresRatesConfigApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StoresRatesConfigApi()

    def tearDown(self) -> None:
        pass

    def test_stores_get_store_rate_configuration(self) -> None:
        """Test case for stores_get_store_rate_configuration

        Get store rate settings
        """
        pass

    def test_stores_preview_store_rate_configuration(self) -> None:
        """Test case for stores_preview_store_rate_configuration

        Preview rate configuration results
        """
        pass

    def test_stores_update_store_rate_configuration(self) -> None:
        """Test case for stores_update_store_rate_configuration

        Update store rate settings
        """
        pass


if __name__ == '__main__':
    unittest.main()