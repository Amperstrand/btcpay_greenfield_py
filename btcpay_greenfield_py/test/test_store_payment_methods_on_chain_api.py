# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.store_payment_methods_on_chain_api import StorePaymentMethodsOnChainApi


class TestStorePaymentMethodsOnChainApi(unittest.TestCase):
    """StorePaymentMethodsOnChainApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StorePaymentMethodsOnChainApi()

    def tearDown(self) -> None:
        pass

    def test_store_on_chain_payment_methods_delete_on_chain_payment_method(self) -> None:
        """Test case for store_on_chain_payment_methods_delete_on_chain_payment_method

        Remove store on-chain payment method
        """
        pass

    def test_store_on_chain_payment_methods_generate_on_chain_wallet(self) -> None:
        """Test case for store_on_chain_payment_methods_generate_on_chain_wallet

        Generate store on-chain wallet
        """
        pass

    def test_store_on_chain_payment_methods_get_on_chain_payment_method(self) -> None:
        """Test case for store_on_chain_payment_methods_get_on_chain_payment_method

        Get store on-chain payment method
        """
        pass

    def test_store_on_chain_payment_methods_get_on_chain_payment_method_preview(self) -> None:
        """Test case for store_on_chain_payment_methods_get_on_chain_payment_method_preview

        Preview store on-chain payment method addresses
        """
        pass

    def test_store_on_chain_payment_methods_get_on_chain_payment_methods(self) -> None:
        """Test case for store_on_chain_payment_methods_get_on_chain_payment_methods

        Get store on-chain payment methods
        """
        pass

    def test_store_on_chain_payment_methods_poston_chain_payment_method_preview(self) -> None:
        """Test case for store_on_chain_payment_methods_poston_chain_payment_method_preview

        Preview proposed store on-chain payment method addresses
        """
        pass

    def test_store_on_chain_payment_methods_update_on_chain_payment_method(self) -> None:
        """Test case for store_on_chain_payment_methods_update_on_chain_payment_method

        Update store on-chain payment method
        """
        pass


if __name__ == '__main__':
    unittest.main()
