# UpdateLightningNetworkPaymentMethodRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** | The lightning connection string. Set to &#39;Internal Node&#39; to use the internal node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for some example) | [optional] 
**enabled** | **bool** | Whether the payment method is enabled | [optional] 

## Example

```python
from openapi_client.models.update_lightning_network_payment_method_request import UpdateLightningNetworkPaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLightningNetworkPaymentMethodRequest from a JSON string
update_lightning_network_payment_method_request_instance = UpdateLightningNetworkPaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print UpdateLightningNetworkPaymentMethodRequest.to_json()

# convert the object into a dict
update_lightning_network_payment_method_request_dict = update_lightning_network_payment_method_request_instance.to_dict()
# create an instance of UpdateLightningNetworkPaymentMethodRequest from a dict
update_lightning_network_payment_method_request_form_dict = update_lightning_network_payment_method_request.from_dict(update_lightning_network_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


