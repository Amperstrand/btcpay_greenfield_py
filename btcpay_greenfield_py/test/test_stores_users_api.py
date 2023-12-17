# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from btcpay_greenfield_py.api.stores_users_api import StoresUsersApi


class TestStoresUsersApi(unittest.TestCase):
    """StoresUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StoresUsersApi()

    def tearDown(self) -> None:
        pass

    def test_stores_add_store_user(self) -> None:
        """Test case for stores_add_store_user

        Add a store user
        """
        pass

    def test_stores_get_store_users(self) -> None:
        """Test case for stores_get_store_users

        Get store users
        """
        pass

    def test_stores_remove_store_user(self) -> None:
        """Test case for stores_remove_store_user

        Remove Store User
        """
        pass


if __name__ == '__main__':
    unittest.main()
