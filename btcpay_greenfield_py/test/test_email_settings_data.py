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

from btcpay_greenfield_py.models.email_settings_data import EmailSettingsData

class TestEmailSettingsData(unittest.TestCase):
    """EmailSettingsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailSettingsData:
        """Test EmailSettingsData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailSettingsData`
        """
        model = EmailSettingsData()
        if include_optional:
            return EmailSettingsData(
                server = '',
                port = 1.337,
                login = '',
                password = '',
                var_from = '',
                from_display = '',
                disable_certificate_check = True
            )
        else:
            return EmailSettingsData(
        )
        """

    def testEmailSettingsData(self):
        """Test EmailSettingsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
