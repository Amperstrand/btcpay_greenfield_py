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

from openapi_client.models.on_chain_wallet_transaction_data import OnChainWalletTransactionData

class TestOnChainWalletTransactionData(unittest.TestCase):
    """OnChainWalletTransactionData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnChainWalletTransactionData:
        """Test OnChainWalletTransactionData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnChainWalletTransactionData`
        """
        model = OnChainWalletTransactionData()
        if include_optional:
            return OnChainWalletTransactionData(
                transaction_hash = '',
                comment = '',
                amount = '',
                block_hash = '',
                block_height = '',
                confirmations = '',
                timestamp = 1592312018,
                status = 'Confirmed',
                labels = [
                    { }
                    ]
            )
        else:
            return OnChainWalletTransactionData(
        )
        """

    def testOnChainWalletTransactionData(self):
        """Test OnChainWalletTransactionData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
