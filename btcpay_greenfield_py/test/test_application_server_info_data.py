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

from btcpay_greenfield_py.models.application_server_info_data import ApplicationServerInfoData

class TestApplicationServerInfoData(unittest.TestCase):
    """ApplicationServerInfoData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationServerInfoData:
        """Test ApplicationServerInfoData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationServerInfoData`
        """
        model = ApplicationServerInfoData()
        if include_optional:
            return ApplicationServerInfoData(
                version = '',
                onion = '',
                supported_payment_methods = [
                    ''
                    ],
                fully_synched = True,
                sync_status = [
                    btcpay_greenfield_py.models.application_server_info_sync_status_data.ApplicationServerInfoSyncStatusData(
                        crypto_code = 'BTC', 
                        node_information = btcpay_greenfield_py.models.application_server_info_node_status_data.ApplicationServerInfoNodeStatusData(
                            headers = 56, 
                            blocks = 56, 
                            verification_progress = 0, ), 
                        chain_height = 56, 
                        sync_height = 1.337, 
                        available = True, )
                    ]
            )
        else:
            return ApplicationServerInfoData(
        )
        """

    def testApplicationServerInfoData(self):
        """Test ApplicationServerInfoData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
