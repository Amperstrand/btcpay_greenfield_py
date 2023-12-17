# ApiKeyData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The API Key to use for API Key Authentication | [optional] 
**label** | **str** | The label given by the user to this API Key | [optional] 
**permissions** | **List[str]** | The permissions associated to this API Key (can be scoped to a specific store) | [optional] 

## Example

```python
from btcpay_greenfield_py.models.api_key_data import ApiKeyData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyData from a JSON string
api_key_data_instance = ApiKeyData.from_json(json)
# print the JSON string representation of the object
print ApiKeyData.to_json()

# convert the object into a dict
api_key_data_dict = api_key_data_instance.to_dict()
# create an instance of ApiKeyData from a dict
api_key_data_form_dict = api_key_data.from_dict(api_key_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


