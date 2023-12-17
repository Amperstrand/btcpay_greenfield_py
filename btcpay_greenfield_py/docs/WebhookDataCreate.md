# WebhookDataCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether this webhook is enabled or not | [optional] [default to True]
**automatic_redelivery** | **bool** | If true, BTCPay Server will retry to redeliver any failed delivery after 10 seconds, 1 minutes and up to 6 times after 10 minutes. | [optional] [default to True]
**url** | **str** | The endpoint where BTCPay Server will make the POST request with the webhook body | [optional] 
**authorized_events** | [**WebhookDataBaseAuthorizedEvents**](WebhookDataBaseAuthorizedEvents.md) |  | [optional] 
**secret** | **str** | Must be used by the callback receiver to ensure the delivery comes from BTCPay Server. BTCPay Server includes the &#x60;BTCPay-Sig&#x60; HTTP header, whose format is &#x60;sha256&#x3D;HMAC256(UTF8(webhook&#39;s secret), body)&#x60;. The pattern to authenticate the webhook is similar to [how to secure webhooks in Github](https://docs.github.com/webhooks/securing/). If left out, null, or empty, the secret will be auto-generated. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.webhook_data_create import WebhookDataCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDataCreate from a JSON string
webhook_data_create_instance = WebhookDataCreate.from_json(json)
# print the JSON string representation of the object
print WebhookDataCreate.to_json()

# convert the object into a dict
webhook_data_create_dict = webhook_data_create_instance.to_dict()
# create an instance of WebhookDataCreate from a dict
webhook_data_create_form_dict = webhook_data_create.from_dict(webhook_data_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


