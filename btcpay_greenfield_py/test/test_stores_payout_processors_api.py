# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from btcpay_greenfield_py.api.stores_payout_processors_api import StoresPayoutProcessorsApi


class TestStoresPayoutProcessorsApi(unittest.TestCase):
    """StoresPayoutProcessorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StoresPayoutProcessorsApi()

    def tearDown(self) -> None:
        pass

    def test_greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method(self) -> None:
        """Test case for greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method

        Get configured store Lightning automated payout processors
        """
        pass

    def test_greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory(self) -> None:
        """Test case for greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory

        Get configured store Lightning automated payout processors
        """
        pass

    def test_greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor(self) -> None:
        """Test case for greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor

        Update configured store Lightning automated payout processors
        """
        pass

    def test_greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method(self) -> None:
        """Test case for greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method

        Get configured store onchain automated payout processors
        """
        pass

    def test_greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory(self) -> None:
        """Test case for greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory

        Get configured store onchain automated payout processors
        """
        pass

    def test_greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method(self) -> None:
        """Test case for greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method

        Update configured store onchain automated payout processors
        """
        pass

    def test_greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory(self) -> None:
        """Test case for greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory

        Update configured store onchain automated payout processors
        """
        pass

    def test_store_payout_processors_get_store_payout_processors(self) -> None:
        """Test case for store_payout_processors_get_store_payout_processors

        Get store configured payout processors
        """
        pass

    def test_store_payout_processors_remove_store_payout_processor(self) -> None:
        """Test case for store_payout_processors_remove_store_payout_processor

        Remove store configured payout processor
        """
        pass


if __name__ == '__main__':
    unittest.main()
