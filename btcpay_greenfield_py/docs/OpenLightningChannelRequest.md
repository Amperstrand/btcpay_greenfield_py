# OpenLightningChannelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_uri** | **str** | Node URI in the form &#x60;pubkey@endpoint[:port]&#x60; | [optional] 
**channel_amount** | **str** | The amount to fund (in satoshi) | [optional] 
**fee_rate** | **float** | The amount to fund (in satoshi per byte) | [optional] 

## Example

```python
from btcpay_greenfield_py.models.open_lightning_channel_request import OpenLightningChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenLightningChannelRequest from a JSON string
open_lightning_channel_request_instance = OpenLightningChannelRequest.from_json(json)
# print the JSON string representation of the object
print OpenLightningChannelRequest.to_json()

# convert the object into a dict
open_lightning_channel_request_dict = open_lightning_channel_request_instance.to_dict()
# create an instance of OpenLightningChannelRequest from a dict
open_lightning_channel_request_form_dict = open_lightning_channel_request.from_dict(open_lightning_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


