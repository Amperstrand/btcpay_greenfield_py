# LightningNetworkPaymentMethodData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** | The lightning connection string. Set to &#39;Internal Node&#39; to use the internal node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for some example) | [optional] 
**enabled** | **bool** | Whether the payment method is enabled | [optional] 
**crypto_code** | **str** | Crypto code of the payment method | [optional] 
**payment_method** | **str** | The payment method | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lightning_network_payment_method_data import LightningNetworkPaymentMethodData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningNetworkPaymentMethodData from a JSON string
lightning_network_payment_method_data_instance = LightningNetworkPaymentMethodData.from_json(json)
# print the JSON string representation of the object
print LightningNetworkPaymentMethodData.to_json()

# convert the object into a dict
lightning_network_payment_method_data_dict = lightning_network_payment_method_data_instance.to_dict()
# create an instance of LightningNetworkPaymentMethodData from a dict
lightning_network_payment_method_data_form_dict = lightning_network_payment_method_data.from_dict(lightning_network_payment_method_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


