# LightningNodeBalanceDataOffchain

Off-chain balance of the Lightning node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening** | **str** | The amount of current channel openings in millisatoshi | [optional] 
**local** | **str** | The amount that is available on the local end of active channels in millisatoshi | [optional] 
**remote** | **str** | The amount that is available on the remote end of active channels in millisatoshi | [optional] 
**closing** | **str** | The amount of current channel closings in millisatoshi | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lightning_node_balance_data_offchain import LightningNodeBalanceDataOffchain

# TODO update the JSON string below
json = "{}"
# create an instance of LightningNodeBalanceDataOffchain from a JSON string
lightning_node_balance_data_offchain_instance = LightningNodeBalanceDataOffchain.from_json(json)
# print the JSON string representation of the object
print LightningNodeBalanceDataOffchain.to_json()

# convert the object into a dict
lightning_node_balance_data_offchain_dict = lightning_node_balance_data_offchain_instance.to_dict()
# create an instance of LightningNodeBalanceDataOffchain from a dict
lightning_node_balance_data_offchain_form_dict = lightning_node_balance_data_offchain.from_dict(lightning_node_balance_data_offchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


