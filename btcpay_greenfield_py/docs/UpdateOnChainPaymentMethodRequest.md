# UpdateOnChainPaymentMethodRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**derivation_scheme** | **str** | The derivation scheme | [optional] 
**label** | **str** | A label that will be shown in the UI | [optional] 
**account_key_path** | **str** | The wallet fingerprint followed by the keypath to derive the account key used for signing operation or creating PSBTs | [optional] 
**enabled** | **bool** | Whether the payment method is enabled | [optional] 

## Example

```python
from openapi_client.models.update_on_chain_payment_method_request import UpdateOnChainPaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOnChainPaymentMethodRequest from a JSON string
update_on_chain_payment_method_request_instance = UpdateOnChainPaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print UpdateOnChainPaymentMethodRequest.to_json()

# convert the object into a dict
update_on_chain_payment_method_request_dict = update_on_chain_payment_method_request_instance.to_dict()
# create an instance of UpdateOnChainPaymentMethodRequest from a dict
update_on_chain_payment_method_request_form_dict = update_on_chain_payment_method_request.from_dict(update_on_chain_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


