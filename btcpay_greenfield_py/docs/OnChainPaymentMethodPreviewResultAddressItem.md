# OnChainPaymentMethodPreviewResultAddressItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_path** | **str** | The key path relative to the account key path. | [optional] 
**address** | **str** | The address generated at the key path | [optional] 

## Example

```python
from openapi_client.models.on_chain_payment_method_preview_result_address_item import OnChainPaymentMethodPreviewResultAddressItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainPaymentMethodPreviewResultAddressItem from a JSON string
on_chain_payment_method_preview_result_address_item_instance = OnChainPaymentMethodPreviewResultAddressItem.from_json(json)
# print the JSON string representation of the object
print OnChainPaymentMethodPreviewResultAddressItem.to_json()

# convert the object into a dict
on_chain_payment_method_preview_result_address_item_dict = on_chain_payment_method_preview_result_address_item_instance.to_dict()
# create an instance of OnChainPaymentMethodPreviewResultAddressItem from a dict
on_chain_payment_method_preview_result_address_item_form_dict = on_chain_payment_method_preview_result_address_item.from_dict(on_chain_payment_method_preview_result_address_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


