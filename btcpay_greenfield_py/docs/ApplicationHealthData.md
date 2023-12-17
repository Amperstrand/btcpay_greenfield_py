# ApplicationHealthData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**synchronized** | **bool** | True if the instance is fully synchronized, according to NBXplorer | [optional] 

## Example

```python
from openapi_client.models.application_health_data import ApplicationHealthData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationHealthData from a JSON string
application_health_data_instance = ApplicationHealthData.from_json(json)
# print the JSON string representation of the object
print ApplicationHealthData.to_json()

# convert the object into a dict
application_health_data_dict = application_health_data_instance.to_dict()
# create an instance of ApplicationHealthData from a dict
application_health_data_form_dict = application_health_data.from_dict(application_health_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


