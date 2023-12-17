# LightningNodeInformationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_uris** | **List[str]** | Node URIs to connect to this node in the form &#x60;pubkey@endpoint[:port]&#x60; | [optional] 
**block_height** | **int** | The block height of the lightning node | [optional] 
**alias** | **str** | The alias of the lightning node | [optional] 
**color** | **str** | The color attribute of the lightning node | [optional] 
**version** | **str** | The version name of the lightning node | [optional] 
**peers_count** | **int** | The number of peers | [optional] 
**active_channels_count** | **int** | The number of active channels | [optional] 
**inactive_channels_count** | **int** | The number of inactive channels | [optional] 
**pending_channels_count** | **int** | The number of pending channels | [optional] 

## Example

```python
from openapi_client.models.lightning_node_information_data import LightningNodeInformationData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningNodeInformationData from a JSON string
lightning_node_information_data_instance = LightningNodeInformationData.from_json(json)
# print the JSON string representation of the object
print LightningNodeInformationData.to_json()

# convert the object into a dict
lightning_node_information_data_dict = lightning_node_information_data_instance.to_dict()
# create an instance of LightningNodeInformationData from a dict
lightning_node_information_data_form_dict = lightning_node_information_data.from_dict(lightning_node_information_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


