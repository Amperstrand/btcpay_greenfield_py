# PointOfSaleAppData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the app | [optional] 
**name** | **str** | Name given to the app when it was created | [optional] 
**store_id** | **str** | Id of the store to which the app belongs | [optional] 
**created** | **int** | UNIX timestamp for when the app was created | [optional] 
**app_type** | **str** | Type of the app which was created | [optional] 
**archived** | **bool** | If true, the app does not appear in the apps list by default. | [optional] [default to False]
**title** | **str** | Display title of the app | [optional] 
**description** | **str** | App description | [optional] 
**default_view** | **str** | App view type (e.g., static, cart, etc...) | [optional] 
**show_custom_amount** | **bool** | Whether the option to enter a custom amount is shown | [optional] 
**show_discount** | **bool** | Whether the option to enter a discount is shown | [optional] 
**enable_tips** | **bool** | Whether the option to enter a tip is shown | [optional] 
**currency** | **str** | Currency used for the app | [optional] 
**items** | **object** | JSON object of app items | [optional] 
**fixed_amount_pay_button_text** | **str** | Payment button text template for items with a set price | [optional] 
**custom_amount_pay_button_text** | **str** | Payment button text which appears for items which allow user to input a custom amount | [optional] 
**tip_text** | **str** | Prompt which appears next to the tip amount field if tipping is enabled | [optional] 
**custom_css_link** | **str** | Link to a custom CSS stylesheet to be used in the app | [optional] 
**notification_url** | **str** | Callback notification url to POST to once when invoice is paid for and once when there are enough blockchain confirmations | [optional] 
**redirect_url** | **str** | URL user is redirected to once invoice is paid | [optional] 
**embedded_css** | **str** | Custom CSS embedded into the app | [optional] 
**redirect_automatically** | **bool** | Whether user is redirected to specified redirect URL automatically after the invoice is paid | [optional] 
**requires_refund_email** | **bool** | Whether refund email is required when paying the invoice. Defaults to &#x60;null&#x60; if not explicitly set. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.point_of_sale_app_data import PointOfSaleAppData

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfSaleAppData from a JSON string
point_of_sale_app_data_instance = PointOfSaleAppData.from_json(json)
# print the JSON string representation of the object
print PointOfSaleAppData.to_json()

# convert the object into a dict
point_of_sale_app_data_dict = point_of_sale_app_data_instance.to_dict()
# create an instance of PointOfSaleAppData from a dict
point_of_sale_app_data_form_dict = point_of_sale_app_data.from_dict(point_of_sale_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


