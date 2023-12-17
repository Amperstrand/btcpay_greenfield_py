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

from openapi_client.models.create_custodian_account_request import CreateCustodianAccountRequest

class TestCreateCustodianAccountRequest(unittest.TestCase):
    """CreateCustodianAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCustodianAccountRequest:
        """Test CreateCustodianAccountRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCustodianAccountRequest`
        """
        model = CreateCustodianAccountRequest()
        if include_optional:
            return CreateCustodianAccountRequest(
                id = '',
                store_id = '',
                custodian_code = '',
                name = '',
                config = None
            )
        else:
            return CreateCustodianAccountRequest(
        )
        """

    def testCreateCustodianAccountRequest(self):
        """Test CreateCustodianAccountRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
