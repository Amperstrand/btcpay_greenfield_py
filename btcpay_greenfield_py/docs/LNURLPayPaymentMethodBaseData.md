# LNURLPayPaymentMethodBaseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_bech32_scheme** | **bool** | Whether to use [LUD-01](https://github.com/fiatjaf/lnurl-rfc/blob/luds/01.md)&#39;s bech32 format or to use [LUD-17](https://github.com/fiatjaf/lnurl-rfc/blob/luds/17.md) url formatting.  | [optional] 
**lud12_enabled** | **bool** | Allow comments to be passed on via lnurl. | [optional] 

## Example

```python
from openapi_client.models.lnurl_pay_payment_method_base_data import LNURLPayPaymentMethodBaseData

# TODO update the JSON string below
json = "{}"
# create an instance of LNURLPayPaymentMethodBaseData from a JSON string
lnurl_pay_payment_method_base_data_instance = LNURLPayPaymentMethodBaseData.from_json(json)
# print the JSON string representation of the object
print LNURLPayPaymentMethodBaseData.to_json()

# convert the object into a dict
lnurl_pay_payment_method_base_data_dict = lnurl_pay_payment_method_base_data_instance.to_dict()
# create an instance of LNURLPayPaymentMethodBaseData from a dict
lnurl_pay_payment_method_base_data_form_dict = lnurl_pay_payment_method_base_data.from_dict(lnurl_pay_payment_method_base_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


