# UpdateNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen** | **bool** | Sets the notification as seen/unseen. If left null, sets it to the opposite value | [optional] 

## Example

```python
from openapi_client.models.update_notification import UpdateNotification

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotification from a JSON string
update_notification_instance = UpdateNotification.from_json(json)
# print the JSON string representation of the object
print UpdateNotification.to_json()

# convert the object into a dict
update_notification_dict = update_notification_instance.to_dict()
# create an instance of UpdateNotification from a dict
update_notification_form_dict = update_notification.from_dict(update_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


