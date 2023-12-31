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

from btcpay_greenfield_py.models.crowdfund_app_data import CrowdfundAppData

class TestCrowdfundAppData(unittest.TestCase):
    """CrowdfundAppData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CrowdfundAppData:
        """Test CrowdfundAppData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrowdfundAppData`
        """
        model = CrowdfundAppData()
        if include_optional:
            return CrowdfundAppData(
                id = '3ki4jsAkN4u9rv1PUzj1odX4Nx7s',
                name = 'my test app',
                store_id = '9CiNzKoANXxmk5ayZngSXrHTiVvvgCrwrpFQd4m2K776',
                created = 1651554744,
                app_type = 'PointOfSale',
                archived = True,
                title = 'My crowdfund app',
                description = 'My crowdfund description',
                enabled = True,
                enforce_target_amount = False,
                start_date = 1592312018,
                end_date = 1592312018,
                target_currency = 'BTC',
                target_amount = 420.69,
                custom_css_link = '',
                main_image_url = '',
                embedded_css = '',
                perks = [{"description":null,"id":"test perk","image":null,"price":{"type":2,"formatted":"$100.00","value":100},"title":"test perk","buyButtonText":null,"inventory":null,"paymentMethods":null,"disabled":false},{"description":"this is an amazing perk","id":"test test","image":"https://mainnet.demo.btcpayserver.org/img/errorpages/404_nicolas.jpg","price":{"type":1,"formatted":"$69.42","value":69.42},"title":"test test","buyButtonText":null,"inventory":5,"paymentMethods":null,"disabled":false},{"description":null,"id":"f$t45hj764325","image":null,"price":{"type":0,"formatted":null,"value":null},"title":"amazing perk","buyButtonText":"button text","inventory":null,"paymentMethods":null,"disabled":true}],
                notification_url = '',
                tagline = 'I can't believe it's not butter',
                disqus_enabled = True,
                disqus_shortname = '',
                sounds_enabled = False,
                animations_enabled = True,
                reset_every_amount = 1,
                reset_every = 'Day',
                display_perks_value = False,
                sort_perks_by_popularity = True,
                sounds = ["https://github.com/ClaudiuHKS/AdvancedQuakeSounds/raw/master/sound/AQS/doublekill.wav"],
                animation_colors = ["#FF0000","#00FF00","#0000FF"]
            )
        else:
            return CrowdfundAppData(
        )
        """

    def testCrowdfundAppData(self):
        """Test CrowdfundAppData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
