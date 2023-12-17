# OnChainPaymentMethodData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**derivation_scheme** | **str** | The derivation scheme | [optional] 
**label** | **str** | A label that will be shown in the UI | [optional] 
**account_key_path** | **str** | The wallet fingerprint followed by the keypath to derive the account key used for signing operation or creating PSBTs | [optional] 
**crypto_code** | **str** | Crypto code of the payment method | [optional] 
**enabled** | **bool** | Whether the payment method is enabled | [optional] 
**payment_method** | **str** | The payment method | [optional] 

## Example

```python
from btcpay_greenfield_py.models.on_chain_payment_method_data import OnChainPaymentMethodData

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainPaymentMethodData from a JSON string
on_chain_payment_method_data_instance = OnChainPaymentMethodData.from_json(json)
# print the JSON string representation of the object
print OnChainPaymentMethodData.to_json()

# convert the object into a dict
on_chain_payment_method_data_dict = on_chain_payment_method_data_instance.to_dict()
# create an instance of OnChainPaymentMethodData from a dict
on_chain_payment_method_data_form_dict = on_chain_payment_method_data.from_dict(on_chain_payment_method_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


