# AddOnChainWalletObjectLinkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | The data of the link | [optional] 
**type** | **str** | The type of wallet object | [optional] 
**id** | **str** | The identifier of the wallet object (unique per type, per wallet) | [optional] 

## Example

```python
from openapi_client.models.add_on_chain_wallet_object_link_request import AddOnChainWalletObjectLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnChainWalletObjectLinkRequest from a JSON string
add_on_chain_wallet_object_link_request_instance = AddOnChainWalletObjectLinkRequest.from_json(json)
# print the JSON string representation of the object
print AddOnChainWalletObjectLinkRequest.to_json()

# convert the object into a dict
add_on_chain_wallet_object_link_request_dict = add_on_chain_wallet_object_link_request_instance.to_dict()
# create an instance of AddOnChainWalletObjectLinkRequest from a dict
add_on_chain_wallet_object_link_request_form_dict = add_on_chain_wallet_object_link_request.from_dict(add_on_chain_wallet_object_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


