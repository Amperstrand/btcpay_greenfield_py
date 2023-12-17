# NotificationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the notification | [optional] 
**identifier** | **str** | The identifier of the notification | [optional] 
**type** | **str** | The type of the notification | [optional] 
**body** | **str** | The html body of the notifications | [optional] 
**link** | **str** | The link of the notification | [optional] 
**created_time** | **float** | A unix timestamp in seconds | [optional] 
**seen** | **bool** | If the notification has been seen by the user | [optional] 

## Example

```python
from btcpay_greenfield_py.models.notification_data import NotificationData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationData from a JSON string
notification_data_instance = NotificationData.from_json(json)
# print the JSON string representation of the object
print NotificationData.to_json()

# convert the object into a dict
notification_data_dict = notification_data_instance.to_dict()
# create an instance of NotificationData from a dict
notification_data_form_dict = notification_data.from_dict(notification_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


