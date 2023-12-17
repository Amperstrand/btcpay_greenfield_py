# OffchainBalanceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening** | **str** | The amount of current channel openings in millisatoshi | [optional] 
**local** | **str** | The amount that is available on the local end of active channels in millisatoshi | [optional] 
**remote** | **str** | The amount that is available on the remote end of active channels in millisatoshi | [optional] 
**closing** | **str** | The amount of current channel closings in millisatoshi | [optional] 

## Example

```python
from btcpay_greenfield_py.models.offchain_balance_data import OffchainBalanceData

# TODO update the JSON string below
json = "{}"
# create an instance of OffchainBalanceData from a JSON string
offchain_balance_data_instance = OffchainBalanceData.from_json(json)
# print the JSON string representation of the object
print OffchainBalanceData.to_json()

# convert the object into a dict
offchain_balance_data_dict = offchain_balance_data_instance.to_dict()
# create an instance of OffchainBalanceData from a dict
offchain_balance_data_form_dict = offchain_balance_data.from_dict(offchain_balance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


