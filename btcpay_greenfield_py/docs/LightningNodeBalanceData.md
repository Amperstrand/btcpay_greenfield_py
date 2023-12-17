# LightningNodeBalanceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onchain** | [**LightningNodeBalanceDataOnchain**](LightningNodeBalanceDataOnchain.md) |  | [optional] 
**offchain** | [**LightningNodeBalanceDataOffchain**](LightningNodeBalanceDataOffchain.md) |  | [optional] 

## Example

```python
from openapi_client.models.lightning_node_balance_data import LightningNodeBalanceData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningNodeBalanceData from a JSON string
lightning_node_balance_data_instance = LightningNodeBalanceData.from_json(json)
# print the JSON string representation of the object
print LightningNodeBalanceData.to_json()

# convert the object into a dict
lightning_node_balance_data_dict = lightning_node_balance_data_instance.to_dict()
# create an instance of LightningNodeBalanceData from a dict
lightning_node_balance_data_form_dict = lightning_node_balance_data.from_dict(lightning_node_balance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


