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

from openapi_client.models.get_rate_sources200_response_inner import GetRateSources200ResponseInner

class TestGetRateSources200ResponseInner(unittest.TestCase):
    """GetRateSources200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRateSources200ResponseInner:
        """Test GetRateSources200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRateSources200ResponseInner`
        """
        model = GetRateSources200ResponseInner()
        if include_optional:
            return GetRateSources200ResponseInner(
                id = '',
                name = ''
            )
        else:
            return GetRateSources200ResponseInner(
        )
        """

    def testGetRateSources200ResponseInner(self):
        """Test GetRateSources200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()