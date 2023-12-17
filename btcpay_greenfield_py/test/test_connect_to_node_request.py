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

from openapi_client.models.connect_to_node_request import ConnectToNodeRequest

class TestConnectToNodeRequest(unittest.TestCase):
    """ConnectToNodeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectToNodeRequest:
        """Test ConnectToNodeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectToNodeRequest`
        """
        model = ConnectToNodeRequest()
        if include_optional:
            return ConnectToNodeRequest(
                node_uri = ''
            )
        else:
            return ConnectToNodeRequest(
        )
        """

    def testConnectToNodeRequest(self):
        """Test ConnectToNodeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()