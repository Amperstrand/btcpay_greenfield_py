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

from btcpay_greenfield_py.models.generate_on_chain_wallet_request import GenerateOnChainWalletRequest

class TestGenerateOnChainWalletRequest(unittest.TestCase):
    """GenerateOnChainWalletRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateOnChainWalletRequest:
        """Test GenerateOnChainWalletRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateOnChainWalletRequest`
        """
        model = GenerateOnChainWalletRequest()
        if include_optional:
            return GenerateOnChainWalletRequest(
                existing_mnemonic = '',
                passphrase = '',
                account_number = 1.337,
                save_private_keys = True,
                import_keys_to_rpc = True,
                word_list = 'English',
                word_count = 12,
                script_pub_key_type = 'Segwit'
            )
        else:
            return GenerateOnChainWalletRequest(
        )
        """

    def testGenerateOnChainWalletRequest(self):
        """Test GenerateOnChainWalletRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
