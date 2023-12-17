# WebhookDeliveryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the delivery | [optional] 
**timestamp** | **float** | A unix timestamp in seconds | [optional] 
**http_code** | **float** | HTTP code received by the remote service, if any. | [optional] 
**error_message** | **str** | User friendly error message, if any. | [optional] 
**status** | **str** | Whether the delivery failed or not (possible values are: &#x60;Failed&#x60;, &#x60;HttpError&#x60;, &#x60;HttpSuccess&#x60;) | [optional] 

## Example

```python
from btcpay_greenfield_py.models.webhook_delivery_data import WebhookDeliveryData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryData from a JSON string
webhook_delivery_data_instance = WebhookDeliveryData.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryData.to_json()

# convert the object into a dict
webhook_delivery_data_dict = webhook_delivery_data_instance.to_dict()
# create an instance of WebhookDeliveryData from a dict
webhook_delivery_data_form_dict = webhook_delivery_data.from_dict(webhook_delivery_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


