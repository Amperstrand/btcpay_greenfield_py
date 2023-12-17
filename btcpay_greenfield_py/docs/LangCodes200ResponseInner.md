# LangCodes200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The language code | [optional] 
**current_language** | **str** | The language name | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lang_codes200_response_inner import LangCodes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of LangCodes200ResponseInner from a JSON string
lang_codes200_response_inner_instance = LangCodes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print LangCodes200ResponseInner.to_json()

# convert the object into a dict
lang_codes200_response_inner_dict = lang_codes200_response_inner_instance.to_dict()
# create an instance of LangCodes200ResponseInner from a dict
lang_codes200_response_inner_form_dict = lang_codes200_response_inner.from_dict(lang_codes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


