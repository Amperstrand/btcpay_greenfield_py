# ReceiptOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | A public page will be accessible once the invoice is settled. If null or unspecified, it will fallback to the store&#39;s settings. (The default store settings is true) | [optional] 
**show_qr** | **bool** | Show the QR code of the receipt in the public receipt page. If null or unspecified, it will fallback to the store&#39;s settings. (The default store setting is true) | [optional] 
**show_payments** | **bool** | Show the payment list in the public receipt page. If null or unspecified, it will fallback to the store&#39;s settings. (The default store setting is true) | [optional] 

## Example

```python
from openapi_client.models.receipt_options import ReceiptOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptOptions from a JSON string
receipt_options_instance = ReceiptOptions.from_json(json)
# print the JSON string representation of the object
print ReceiptOptions.to_json()

# convert the object into a dict
receipt_options_dict = receipt_options_instance.to_dict()
# create an instance of ReceiptOptions from a dict
receipt_options_form_dict = receipt_options.from_dict(receipt_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


