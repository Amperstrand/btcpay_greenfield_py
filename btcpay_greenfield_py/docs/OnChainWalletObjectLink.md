# OnChainWalletObjectLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of wallet object | [optional] 
**id** | **str** | The identifier of the wallet object (unique per type, per wallet) | [optional] 
**link_data** | **Dict[str, object]** | The data of the link | [optional] 
**object_data** | **Dict[str, object]** | The data of the neighbour&#39;s node (&#x60;null&#x60; if there isn&#39;t any data or &#x60;includeNeighbourData&#x60; is &#x60;false&#x60;) | [optional] 

## Example

```python
from openapi_client.models.on_chain_wallet_object_link import OnChainWalletObjectLink

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletObjectLink from a JSON string
on_chain_wallet_object_link_instance = OnChainWalletObjectLink.from_json(json)
# print the JSON string representation of the object
print OnChainWalletObjectLink.to_json()

# convert the object into a dict
on_chain_wallet_object_link_dict = on_chain_wallet_object_link_instance.to_dict()
# create an instance of OnChainWalletObjectLink from a dict
on_chain_wallet_object_link_form_dict = on_chain_wallet_object_link.from_dict(on_chain_wallet_object_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


