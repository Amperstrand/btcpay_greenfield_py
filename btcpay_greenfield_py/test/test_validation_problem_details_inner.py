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

from btcpay_greenfield_py.models.validation_problem_details_inner import ValidationProblemDetailsInner

class TestValidationProblemDetailsInner(unittest.TestCase):
    """ValidationProblemDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationProblemDetailsInner:
        """Test ValidationProblemDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationProblemDetailsInner`
        """
        model = ValidationProblemDetailsInner()
        if include_optional:
            return ValidationProblemDetailsInner(
                path = '',
                message = ''
            )
        else:
            return ValidationProblemDetailsInner(
        )
        """

    def testValidationProblemDetailsInner(self):
        """Test ValidationProblemDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
