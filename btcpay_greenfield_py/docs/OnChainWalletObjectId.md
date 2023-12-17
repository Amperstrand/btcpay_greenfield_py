# OnChainWalletObjectId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of wallet object | [optional] 
**id** | **str** | The identifier of the wallet object (unique per type, per wallet) | [optional] 

## Example

```python
from openapi_client.models.on_chain_wallet_object_id import OnChainWalletObjectId

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletObjectId from a JSON string
on_chain_wallet_object_id_instance = OnChainWalletObjectId.from_json(json)
# print the JSON string representation of the object
print OnChainWalletObjectId.to_json()

# convert the object into a dict
on_chain_wallet_object_id_dict = on_chain_wallet_object_id_instance.to_dict()
# create an instance of OnChainWalletObjectId from a dict
on_chain_wallet_object_id_form_dict = on_chain_wallet_object_id.from_dict(on_chain_wallet_object_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


