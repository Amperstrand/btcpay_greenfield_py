# GenericPaymentMethodDataData

Associated dynamic data based on payment method type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** | The lightning connection string. Set to &#39;Internal Node&#39; to use the internal node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for some example) | [optional] 
**derivation_scheme** | **str** | The derivation scheme | [optional] 
**label** | **str** | A label that will be shown in the UI | [optional] 
**account_key_path** | **str** | The wallet fingerprint followed by the keypath to derive the account key used for signing operation or creating PSBTs | [optional] 

## Example

```python
from openapi_client.models.generic_payment_method_data_data import GenericPaymentMethodDataData

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPaymentMethodDataData from a JSON string
generic_payment_method_data_data_instance = GenericPaymentMethodDataData.from_json(json)
# print the JSON string representation of the object
print GenericPaymentMethodDataData.to_json()

# convert the object into a dict
generic_payment_method_data_data_dict = generic_payment_method_data_data_instance.to_dict()
# create an instance of GenericPaymentMethodDataData from a dict
generic_payment_method_data_data_form_dict = generic_payment_method_data_data.from_dict(generic_payment_method_data_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


