# ApiKeysCreateApiKeyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the new API Key | [optional] 
**permissions** | **List[str]** | The permissions granted to this API Key (See API Key Authentication) | [optional] 

## Example

```python
from btcpay_greenfield_py.models.api_keys_create_api_key_request import ApiKeysCreateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeysCreateApiKeyRequest from a JSON string
api_keys_create_api_key_request_instance = ApiKeysCreateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print ApiKeysCreateApiKeyRequest.to_json()

# convert the object into a dict
api_keys_create_api_key_request_dict = api_keys_create_api_key_request_instance.to_dict()
# create an instance of ApiKeysCreateApiKeyRequest from a dict
api_keys_create_api_key_request_form_dict = api_keys_create_api_key_request.from_dict(api_keys_create_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


