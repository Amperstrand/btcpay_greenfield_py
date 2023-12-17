# BasicAppData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the app | [optional] 
**name** | **str** | Name given to the app when it was created | [optional] 
**store_id** | **str** | Id of the store to which the app belongs | [optional] 
**created** | **int** | UNIX timestamp for when the app was created | [optional] 
**app_type** | **str** | Type of the app which was created | [optional] 
**archived** | **bool** | If true, the app does not appear in the apps list by default. | [optional] [default to False]

## Example

```python
from openapi_client.models.basic_app_data import BasicAppData

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAppData from a JSON string
basic_app_data_instance = BasicAppData.from_json(json)
# print the JSON string representation of the object
print BasicAppData.to_json()

# convert the object into a dict
basic_app_data_dict = basic_app_data_instance.to_dict()
# create an instance of BasicAppData from a dict
basic_app_data_form_dict = basic_app_data.from_dict(basic_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


