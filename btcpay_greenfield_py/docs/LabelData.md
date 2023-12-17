# LabelData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of label | [optional] 
**text** | **str** | Information about this label | [optional] 

## Example

```python
from openapi_client.models.label_data import LabelData

# TODO update the JSON string below
json = "{}"
# create an instance of LabelData from a JSON string
label_data_instance = LabelData.from_json(json)
# print the JSON string representation of the object
print LabelData.to_json()

# convert the object into a dict
label_data_dict = label_data_instance.to_dict()
# create an instance of LabelData from a dict
label_data_form_dict = label_data.from_dict(label_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


