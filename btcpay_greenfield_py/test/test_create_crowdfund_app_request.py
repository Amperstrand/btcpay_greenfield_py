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

from openapi_client.models.create_crowdfund_app_request import CreateCrowdfundAppRequest

class TestCreateCrowdfundAppRequest(unittest.TestCase):
    """CreateCrowdfundAppRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCrowdfundAppRequest:
        """Test CreateCrowdfundAppRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCrowdfundAppRequest`
        """
        model = CreateCrowdfundAppRequest()
        if include_optional:
            return CreateCrowdfundAppRequest(
                app_name = 'Kukkstarter',
                title = 'My crowdfund app',
                description = 'My app description',
                enabled = True,
                enforce_target_amount = True,
                start_date = 1592312018,
                end_date = 1592312018,
                target_currency = 'BTC',
                target_amount = 420,
                custom_css_link = '',
                main_image_url = '',
                embedded_css = '',
                perks_template = 'test_perk:
  price: 100
  title: test perk
  price_type: "fixed" 
  disabled: false',
                notification_url = '',
                tagline = 'I can't believe it's not butter',
                disqus_shortname = '',
                sounds_enabled = True,
                animations_enabled = True,
                reset_every_amount = 1.337,
                reset_every = 'Never',
                display_perks_value = True,
                sort_perks_by_popularity = True,
                sounds = ["https://github.com/ClaudiuHKS/AdvancedQuakeSounds/raw/master/sound/AQS/doublekill.wav"],
                animation_colors = ["#0000FF","#00FF00","#FF0000"]
            )
        else:
            return CreateCrowdfundAppRequest(
        )
        """

    def testCreateCrowdfundAppRequest(self):
        """Test CreateCrowdfundAppRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
