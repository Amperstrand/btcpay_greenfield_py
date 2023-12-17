# ApplicationUserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the user | [optional] 
**email** | **str** | The email of the user | [optional] 
**email_confirmed** | **bool** | True if the email has been confirmed by the user | [optional] 
**requires_email_confirmation** | **bool** | True if the email requires email confirmation to log in | [optional] 
**created** | **float** | A unix timestamp in seconds | [optional] 
**roles** | **List[str]** | The roles of the user | [optional] 

## Example

```python
from btcpay_greenfield_py.models.application_user_data import ApplicationUserData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUserData from a JSON string
application_user_data_instance = ApplicationUserData.from_json(json)
# print the JSON string representation of the object
print ApplicationUserData.to_json()

# convert the object into a dict
application_user_data_dict = application_user_data_instance.to_dict()
# create an instance of ApplicationUserData from a dict
application_user_data_form_dict = application_user_data.from_dict(application_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


