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

from openapi_client.models.create_payout_request import CreatePayoutRequest

class TestCreatePayoutRequest(unittest.TestCase):
    """CreatePayoutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePayoutRequest:
        """Test CreatePayoutRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePayoutRequest`
        """
        model = CreatePayoutRequest()
        if include_optional:
            return CreatePayoutRequest(
                destination = '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2',
                amount = '10399.18',
                payment_method = ''
            )
        else:
            return CreatePayoutRequest(
        )
        """

    def testCreatePayoutRequest(self):
        """Test CreatePayoutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()