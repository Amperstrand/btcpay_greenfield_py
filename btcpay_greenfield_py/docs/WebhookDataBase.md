# WebhookDataBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether this webhook is enabled or not | [optional] [default to True]
**automatic_redelivery** | **bool** | If true, BTCPay Server will retry to redeliver any failed delivery after 10 seconds, 1 minutes and up to 6 times after 10 minutes. | [optional] [default to True]
**url** | **str** | The endpoint where BTCPay Server will make the POST request with the webhook body | [optional] 
**authorized_events** | [**WebhookDataBaseAuthorizedEvents**](WebhookDataBaseAuthorizedEvents.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.webhook_data_base import WebhookDataBase

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDataBase from a JSON string
webhook_data_base_instance = WebhookDataBase.from_json(json)
# print the JSON string representation of the object
print WebhookDataBase.to_json()

# convert the object into a dict
webhook_data_base_dict = webhook_data_base_instance.to_dict()
# create an instance of WebhookDataBase from a dict
webhook_data_base_form_dict = webhook_data_base.from_dict(webhook_data_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


