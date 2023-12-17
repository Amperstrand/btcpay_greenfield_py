# WebhookDataBaseAuthorizedEvents

Which event should be received by this endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**everything** | **bool** | If true, the endpoint will receive all events related to the store. | [optional] [default to True]
**specific_events** | **List[str]** | If &#x60;everything&#x60; is false, the specific events that the endpoint is interested in. Current events are: &#x60;InvoiceCreated&#x60;, &#x60;InvoiceReceivedPayment&#x60;, &#x60;InvoiceProcessing&#x60;, &#x60;InvoiceExpired&#x60;, &#x60;InvoiceSettled&#x60;, &#x60;InvoiceInvalid&#x60;. | [optional] 

## Example

```python
from openapi_client.models.webhook_data_base_authorized_events import WebhookDataBaseAuthorizedEvents

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDataBaseAuthorizedEvents from a JSON string
webhook_data_base_authorized_events_instance = WebhookDataBaseAuthorizedEvents.from_json(json)
# print the JSON string representation of the object
print WebhookDataBaseAuthorizedEvents.to_json()

# convert the object into a dict
webhook_data_base_authorized_events_dict = webhook_data_base_authorized_events_instance.to_dict()
# create an instance of WebhookDataBaseAuthorizedEvents from a dict
webhook_data_base_authorized_events_form_dict = webhook_data_base_authorized_events.from_dict(webhook_data_base_authorized_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


