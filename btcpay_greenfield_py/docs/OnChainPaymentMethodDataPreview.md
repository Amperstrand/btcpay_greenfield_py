# OnChainPaymentMethodDataPreview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**derivation_scheme** | **str** | The derivation scheme | [optional] 
**label** | **str** | A label that will be shown in the UI | [optional] 
**account_key_path** | **str** | The wallet fingerprint followed by the keypath to derive the account key used for signing operation or creating PSBTs | [optional] 
**crypto_code** | **str** | Crypto code of the payment method | [optional] 

## Example

```python
from btcpay_greenfield_py.models.on_chain_payment_method_data_preview import OnChainPaymentMethodDataPreview

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainPaymentMethodDataPreview from a JSON string
on_chain_payment_method_data_preview_instance = OnChainPaymentMethodDataPreview.from_json(json)
# print the JSON string representation of the object
print OnChainPaymentMethodDataPreview.to_json()

# convert the object into a dict
on_chain_payment_method_data_preview_dict = on_chain_payment_method_data_preview_instance.to_dict()
# create an instance of OnChainPaymentMethodDataPreview from a dict
on_chain_payment_method_data_preview_form_dict = on_chain_payment_method_data_preview.from_dict(on_chain_payment_method_data_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


