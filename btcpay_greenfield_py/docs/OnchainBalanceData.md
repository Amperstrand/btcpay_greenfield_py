# OnchainBalanceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **str** | The confirmed amount in satoshi | [optional] 
**unconfirmed** | **str** | The unconfirmed amount in satoshi | [optional] 
**reserved** | **str** | The reserved amount in satoshi | [optional] 

## Example

```python
from btcpay_greenfield_py.models.onchain_balance_data import OnchainBalanceData

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainBalanceData from a JSON string
onchain_balance_data_instance = OnchainBalanceData.from_json(json)
# print the JSON string representation of the object
print OnchainBalanceData.to_json()

# convert the object into a dict
onchain_balance_data_dict = onchain_balance_data_instance.to_dict()
# create an instance of OnchainBalanceData from a dict
onchain_balance_data_form_dict = onchain_balance_data.from_dict(onchain_balance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


