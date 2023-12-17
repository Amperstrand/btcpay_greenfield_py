# PatchOnChainTransactionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Transaction comment | [optional] 
**labels** | **List[str]** | Transaction labels | [optional] 

## Example

```python
from openapi_client.models.patch_on_chain_transaction_request import PatchOnChainTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchOnChainTransactionRequest from a JSON string
patch_on_chain_transaction_request_instance = PatchOnChainTransactionRequest.from_json(json)
# print the JSON string representation of the object
print PatchOnChainTransactionRequest.to_json()

# convert the object into a dict
patch_on_chain_transaction_request_dict = patch_on_chain_transaction_request_instance.to_dict()
# create an instance of PatchOnChainTransactionRequest from a dict
patch_on_chain_transaction_request_form_dict = patch_on_chain_transaction_request.from_dict(patch_on_chain_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


