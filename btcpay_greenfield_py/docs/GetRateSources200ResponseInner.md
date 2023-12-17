# GetRateSources200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the rate provider | [optional] 
**name** | **str** | The name of the rate provider | [optional] 

## Example

```python
from openapi_client.models.get_rate_sources200_response_inner import GetRateSources200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateSources200ResponseInner from a JSON string
get_rate_sources200_response_inner_instance = GetRateSources200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetRateSources200ResponseInner.to_json()

# convert the object into a dict
get_rate_sources200_response_inner_dict = get_rate_sources200_response_inner_instance.to_dict()
# create an instance of GetRateSources200ResponseInner from a dict
get_rate_sources200_response_inner_form_dict = get_rate_sources200_response_inner.from_dict(get_rate_sources200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


