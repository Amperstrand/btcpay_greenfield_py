# ApplicationServerInfoSyncStatusData

Detailed sync status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_code** | **str** | The CryptoCode of the crypto currency (eg. BTC) | [optional] 
**node_information** | [**ApplicationServerInfoNodeStatusData**](ApplicationServerInfoNodeStatusData.md) |  | [optional] 
**chain_height** | **int** | The height of the chain of header of the internal indexer | [optional] 
**sync_height** | **float** | The height of the latest indexed block of the internal indexer | [optional] 
**available** | **bool** | True if the full node and the indexer are fully synchronized | [optional] 

## Example

```python
from btcpay_greenfield_py.models.application_server_info_sync_status_data import ApplicationServerInfoSyncStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationServerInfoSyncStatusData from a JSON string
application_server_info_sync_status_data_instance = ApplicationServerInfoSyncStatusData.from_json(json)
# print the JSON string representation of the object
print ApplicationServerInfoSyncStatusData.to_json()

# convert the object into a dict
application_server_info_sync_status_data_dict = application_server_info_sync_status_data_instance.to_dict()
# create an instance of ApplicationServerInfoSyncStatusData from a dict
application_server_info_sync_status_data_form_dict = application_server_info_sync_status_data.from_dict(application_server_info_sync_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


