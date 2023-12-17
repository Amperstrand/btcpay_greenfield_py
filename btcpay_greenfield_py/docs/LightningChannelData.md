# LightningChannelData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_node** | **str** | The public key of the node (Node ID) | [optional] 
**is_public** | **bool** | Whether the node is public | [optional] 
**is_active** | **bool** | Whether the node is online | [optional] 
**capacity** | **str** | The capacity of the channel in millisatoshi | [optional] 
**local_balance** | **str** | The local balance of the channel in millisatoshi | [optional] 
**channel_point** | **str** |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lightning_channel_data import LightningChannelData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningChannelData from a JSON string
lightning_channel_data_instance = LightningChannelData.from_json(json)
# print the JSON string representation of the object
print LightningChannelData.to_json()

# convert the object into a dict
lightning_channel_data_dict = lightning_channel_data_instance.to_dict()
# create an instance of LightningChannelData from a dict
lightning_channel_data_form_dict = lightning_channel_data.from_dict(lightning_channel_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


