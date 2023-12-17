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

from openapi_client.models.update_on_chain_automated_transfer_settings import UpdateOnChainAutomatedTransferSettings

class TestUpdateOnChainAutomatedTransferSettings(unittest.TestCase):
    """UpdateOnChainAutomatedTransferSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOnChainAutomatedTransferSettings:
        """Test UpdateOnChainAutomatedTransferSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOnChainAutomatedTransferSettings`
        """
        model = UpdateOnChainAutomatedTransferSettings()
        if include_optional:
            return UpdateOnChainAutomatedTransferSettings(
                fee_target_block = 1.337,
                interval_seconds = None,
                threshold = '0.1',
                process_new_payouts_instantly = True
            )
        else:
            return UpdateOnChainAutomatedTransferSettings(
        )
        """

    def testUpdateOnChainAutomatedTransferSettings(self):
        """Test UpdateOnChainAutomatedTransferSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()