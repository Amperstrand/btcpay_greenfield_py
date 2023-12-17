# LightningNodeBalanceDataOnchain

On-chain balance of the Lightning node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **str** | The confirmed amount in satoshi | [optional] 
**unconfirmed** | **str** | The unconfirmed amount in satoshi | [optional] 
**reserved** | **str** | The reserved amount in satoshi | [optional] 

## Example

```python
from openapi_client.models.lightning_node_balance_data_onchain import LightningNodeBalanceDataOnchain

# TODO update the JSON string below
json = "{}"
# create an instance of LightningNodeBalanceDataOnchain from a JSON string
lightning_node_balance_data_onchain_instance = LightningNodeBalanceDataOnchain.from_json(json)
# print the JSON string representation of the object
print LightningNodeBalanceDataOnchain.to_json()

# convert the object into a dict
lightning_node_balance_data_onchain_dict = lightning_node_balance_data_onchain_instance.to_dict()
# create an instance of LightningNodeBalanceDataOnchain from a dict
lightning_node_balance_data_onchain_form_dict = lightning_node_balance_data_onchain.from_dict(lightning_node_balance_data_onchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


