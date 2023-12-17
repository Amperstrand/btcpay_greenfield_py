# CreatePointOfSaleAppRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | The name of the app (shown in admin UI) | [optional] 
**title** | **str** | The title of the app (shown to the user) | [optional] 
**description** | **str** | The description of the app | [optional] 
**template** | **str** | Template for items available in the app | [optional] 
**default_view** | **str** | Template for items available in the app | [optional] 
**currency** | **str** | Currency to use for the app. Defaults to the currency used by the store if not specified | [optional] 
**show_custom_amount** | **bool** | Whether to include a special item in the store which allows user to input a custom payment amount | [optional] [default to False]
**show_discount** | **bool** | Whether to allow user to input a discount amount. Applies to Cart view only. Not recommended for customer self-checkout | [optional] [default to True]
**enable_tips** | **bool** | Whether to allow user to input a tip amount. Applies to Cart and Light views only | [optional] [default to True]
**custom_amount_pay_button_text** | **str** | Payment button text which appears for items which allow user to input a custom amount | [optional] [default to 'Pay']
**fixed_amount_pay_button_text** | **str** | Payment button text which appears for items which have a fixed price | [optional] [default to 'Buy for {PRICE_HERE}']
**tip_text** | **str** | Prompt which appears next to the tip amount field if tipping is enabled | [optional] [default to 'Do you want to leave a tip?']
**custom_css_link** | **str** | Link to a custom CSS stylesheet to be used in the app | [optional] 
**embedded_css** | **str** | Custom CSS to embed into the app | [optional] 
**notification_url** | **str** | Callback notification url to POST to once when invoice is paid for and once when there are enough blockchain confirmations | [optional] 
**redirect_url** | **str** | URL to redirect user to once invoice is paid | [optional] 
**redirect_automatically** | **bool** | Whether to redirect user to redirect URL automatically once invoice is paid. Defaults to what is set in the store settings | [optional] 
**requires_refund_email** | **bool** | Whether refund email is required when paying the invoice. Defaults to what is set in the store settings | [optional] 
**checkout_type** | [**CheckoutType**](CheckoutType.md) |  | [optional] 
**form_id** | **str** | Form ID to request customer data | [optional] 

## Example

```python
from openapi_client.models.create_point_of_sale_app_request import CreatePointOfSaleAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePointOfSaleAppRequest from a JSON string
create_point_of_sale_app_request_instance = CreatePointOfSaleAppRequest.from_json(json)
# print the JSON string representation of the object
print CreatePointOfSaleAppRequest.to_json()

# convert the object into a dict
create_point_of_sale_app_request_dict = create_point_of_sale_app_request_instance.to_dict()
# create an instance of CreatePointOfSaleAppRequest from a dict
create_point_of_sale_app_request_form_dict = create_point_of_sale_app_request.from_dict(create_point_of_sale_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


