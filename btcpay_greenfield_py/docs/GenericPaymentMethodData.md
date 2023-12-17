# GenericPaymentMethodData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the payment method is enabled | [optional] 
**crypto_code** | **str** | The currency code of the payment method | [optional] 
**data** | [**GenericPaymentMethodDataData**](GenericPaymentMethodDataData.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.generic_payment_method_data import GenericPaymentMethodData

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPaymentMethodData from a JSON string
generic_payment_method_data_instance = GenericPaymentMethodData.from_json(json)
# print the JSON string representation of the object
print GenericPaymentMethodData.to_json()

# convert the object into a dict
generic_payment_method_data_dict = generic_payment_method_data_instance.to_dict()
# create an instance of GenericPaymentMethodData from a dict
generic_payment_method_data_form_dict = generic_payment_method_data.from_dict(generic_payment_method_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


