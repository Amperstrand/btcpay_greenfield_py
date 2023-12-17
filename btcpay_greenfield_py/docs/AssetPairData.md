# AssetPairData

An asset pair we can trade.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pair** | **str** | The name of the asset pair. | [optional] 
**minimum_trade_qty** | **float** | The smallest amount we can buy or sell. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.asset_pair_data import AssetPairData

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPairData from a JSON string
asset_pair_data_instance = AssetPairData.from_json(json)
# print the JSON string representation of the object
print AssetPairData.to_json()

# convert the object into a dict
asset_pair_data_dict = asset_pair_data_instance.to_dict()
# create an instance of AssetPairData from a dict
asset_pair_data_form_dict = asset_pair_data.from_dict(asset_pair_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


