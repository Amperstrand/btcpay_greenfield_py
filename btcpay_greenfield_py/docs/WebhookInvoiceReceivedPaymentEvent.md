# WebhookInvoiceReceivedPaymentEvent

Callback sent if the `type` is `InvoiceReceivedPayment`

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
**after_expiration** | **bool** | Whether this payment has been sent after expiration of the invoice | [optional] 
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 

## Example

```python
from openapi_client.models.webhook_invoice_received_payment_event import WebhookInvoiceReceivedPaymentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInvoiceReceivedPaymentEvent from a JSON string
webhook_invoice_received_payment_event_instance = WebhookInvoiceReceivedPaymentEvent.from_json(json)
# print the JSON string representation of the object
print WebhookInvoiceReceivedPaymentEvent.to_json()

# convert the object into a dict
webhook_invoice_received_payment_event_dict = webhook_invoice_received_payment_event_instance.to_dict()
# create an instance of WebhookInvoiceReceivedPaymentEvent from a dict
webhook_invoice_received_payment_event_form_dict = webhook_invoice_received_payment_event.from_dict(webhook_invoice_received_payment_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


