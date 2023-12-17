# AssetBalanceData

An asset and it's qty.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | An asset. | [optional] 
**qty** | **decimal.Decimal** | The quantity changed of the asset. Can be positive or negative. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.asset_balance_data import AssetBalanceData

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBalanceData from a JSON string
asset_balance_data_instance = AssetBalanceData.from_json(json)
# print the JSON string representation of the object
print AssetBalanceData.to_json()

# convert the object into a dict
asset_balance_data_dict = asset_balance_data_instance.to_dict()
# create an instance of AssetBalanceData from a dict
asset_balance_data_form_dict = asset_balance_data.from_dict(asset_balance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


