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

from btcpay_greenfield_py.models.api_keys_create_api_key_request import ApiKeysCreateApiKeyRequest

class TestApiKeysCreateApiKeyRequest(unittest.TestCase):
    """ApiKeysCreateApiKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKeysCreateApiKeyRequest:
        """Test ApiKeysCreateApiKeyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKeysCreateApiKeyRequest`
        """
        model = ApiKeysCreateApiKeyRequest()
        if include_optional:
            return ApiKeysCreateApiKeyRequest(
                label = '',
                permissions = [
                    ''
                    ]
            )
        else:
            return ApiKeysCreateApiKeyRequest(
        )
        """

    def testApiKeysCreateApiKeyRequest(self):
        """Test ApiKeysCreateApiKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
