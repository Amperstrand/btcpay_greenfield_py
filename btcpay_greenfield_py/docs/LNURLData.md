# LNURLData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lnurl_bech32** | **str** | Bech32 representation of LNURL | [optional] 
**lnurl_uri** | **str** | URI representation of LNURL | [optional] 

## Example

```python
from openapi_client.models.lnurl_data import LNURLData

# TODO update the JSON string below
json = "{}"
# create an instance of LNURLData from a JSON string
lnurl_data_instance = LNURLData.from_json(json)
# print the JSON string representation of the object
print LNURLData.to_json()

# convert the object into a dict
lnurl_data_dict = lnurl_data_instance.to_dict()
# create an instance of LNURLData from a dict
lnurl_data_form_dict = lnurl_data.from_dict(lnurl_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


