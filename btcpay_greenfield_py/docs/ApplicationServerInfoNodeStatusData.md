# ApplicationServerInfoNodeStatusData

Detailed sync status of the internal full node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **int** | The height of the chain of header of the internal full node | [optional] 
**blocks** | **int** | The height of the latest validated block of the internal full node | [optional] 
**verification_progress** | **float** | The current synchronization progress | [optional] 

## Example

```python
from btcpay_greenfield_py.models.application_server_info_node_status_data import ApplicationServerInfoNodeStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationServerInfoNodeStatusData from a JSON string
application_server_info_node_status_data_instance = ApplicationServerInfoNodeStatusData.from_json(json)
# print the JSON string representation of the object
print ApplicationServerInfoNodeStatusData.to_json()

# convert the object into a dict
application_server_info_node_status_data_dict = application_server_info_node_status_data_instance.to_dict()
# create an instance of ApplicationServerInfoNodeStatusData from a dict
application_server_info_node_status_data_form_dict = application_server_info_node_status_data.from_dict(application_server_info_node_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


