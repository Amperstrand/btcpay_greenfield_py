# EmailSettingsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | Smtp server host | [optional] 
**port** | **float** | Smtp server port | [optional] 
**login** | **str** | Smtp server username | [optional] 
**password** | **str** | Smtp server password | [optional] 
**var_from** | **str** | Email to send from | [optional] 
**from_display** | **str** | The name of the sender | [optional] 
**disable_certificate_check** | **bool** | Disable TLS certificate security checks | [optional] [default to False]

## Example

```python
from openapi_client.models.email_settings_data import EmailSettingsData

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSettingsData from a JSON string
email_settings_data_instance = EmailSettingsData.from_json(json)
# print the JSON string representation of the object
print EmailSettingsData.to_json()

# convert the object into a dict
email_settings_data_dict = email_settings_data_instance.to_dict()
# create an instance of EmailSettingsData from a dict
email_settings_data_form_dict = email_settings_data.from_dict(email_settings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


