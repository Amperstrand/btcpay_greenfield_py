# ApplicationServerInfoData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | BTCPay Server version | [optional] 
**onion** | **str** | The Tor hostname | [optional] 
**supported_payment_methods** | **List[str]** | The payment methods this server supports | [optional] 
**fully_synched** | **bool** | True if the instance is fully synchronized, according to NBXplorer | [optional] 
**sync_status** | [**List[ApplicationServerInfoSyncStatusData]**](ApplicationServerInfoSyncStatusData.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.application_server_info_data import ApplicationServerInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationServerInfoData from a JSON string
application_server_info_data_instance = ApplicationServerInfoData.from_json(json)
# print the JSON string representation of the object
print ApplicationServerInfoData.to_json()

# convert the object into a dict
application_server_info_data_dict = application_server_info_data_instance.to_dict()
# create an instance of ApplicationServerInfoData from a dict
application_server_info_data_form_dict = application_server_info_data.from_dict(application_server_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


