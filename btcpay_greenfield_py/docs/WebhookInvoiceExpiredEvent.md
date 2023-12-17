# WebhookInvoiceExpiredEvent

Callback sent if the `type` is `InvoiceExpired`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | The delivery id of the webhook | [optional] 
**webhook_id** | **str** | The id of the webhook | [optional] 
**original_delivery_id** | **str** | If this delivery is a redelivery, the is the delivery id of the original delivery. | [optional] 
**is_redelivery** | **bool** | True if this delivery is a redelivery | [optional] 
**type** | **str** | The type of this event, current available are &#x60;InvoiceCreated&#x60;, &#x60;InvoiceReceivedPayment&#x60;, &#x60;InvoiceProcessing&#x60;, &#x60;InvoiceExpired&#x60;, &#x60;InvoiceSettled&#x60;, &#x60;InvoiceInvalid&#x60;, and &#x60;InvoicePaymentSettled&#x60;. | [optional] 
**timestamp** | **float** | A unix timestamp in seconds | [optional] 
**store_id** | **str** | The store id of the invoice&#39;s event | [optional] 
**invoice_id** | **str** | The invoice id of the invoice&#39;s event | [optional] 
**metadata** | **object** | User-supplied metadata added to the invoice at the time of its creation | [optional] 
**partially_paid** | **bool** | Whether the invoice received some payments before being expired. | [optional] 

## Example

```python
from openapi_client.models.webhook_invoice_expired_event import WebhookInvoiceExpiredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInvoiceExpiredEvent from a JSON string
webhook_invoice_expired_event_instance = WebhookInvoiceExpiredEvent.from_json(json)
# print the JSON string representation of the object
print WebhookInvoiceExpiredEvent.to_json()

# convert the object into a dict
webhook_invoice_expired_event_dict = webhook_invoice_expired_event_instance.to_dict()
# create an instance of WebhookInvoiceExpiredEvent from a dict
webhook_invoice_expired_event_form_dict = webhook_invoice_expired_event.from_dict(webhook_invoice_expired_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


