# OnChainWalletObjectData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**links** | [**List[OnChainWalletObjectLink]**](OnChainWalletObjectLink.md) | Links of this object | [optional] 
**type** | **str** | The type of wallet object | [optional] 
**id** | **str** | The identifier of the wallet object (unique per type, per wallet) | [optional] 

## Example

```python
from openapi_client.models.on_chain_wallet_object_data import OnChainWalletObjectData

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletObjectData from a JSON string
on_chain_wallet_object_data_instance = OnChainWalletObjectData.from_json(json)
# print the JSON string representation of the object
print OnChainWalletObjectData.to_json()

# convert the object into a dict
on_chain_wallet_object_data_dict = on_chain_wallet_object_data_instance.to_dict()
# create an instance of OnChainWalletObjectData from a dict
on_chain_wallet_object_data_form_dict = on_chain_wallet_object_data.from_dict(on_chain_wallet_object_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


