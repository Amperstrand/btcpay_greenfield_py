# EmailData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the recipient | [optional] 
**subject** | **str** | Subject of the email | [optional] 
**body** | **str** | Body of the email to send as plain text. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.email_data import EmailData

# TODO update the JSON string below
json = "{}"
# create an instance of EmailData from a JSON string
email_data_instance = EmailData.from_json(json)
# print the JSON string representation of the object
print EmailData.to_json()

# convert the object into a dict
email_data_dict = email_data_instance.to_dict()
# create an instance of EmailData from a dict
email_data_form_dict = email_data.from_dict(email_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


