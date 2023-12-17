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

from openapi_client.models.lock_user_request import LockUserRequest

class TestLockUserRequest(unittest.TestCase):
    """LockUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LockUserRequest:
        """Test LockUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LockUserRequest`
        """
        model = LockUserRequest()
        if include_optional:
            return LockUserRequest(
                locked = True
            )
        else:
            return LockUserRequest(
        )
        """

    def testLockUserRequest(self):
        """Test LockUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
