# TradeResultData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_asset** | **str** | The asset to trade. | [optional] 
**to_asset** | **str** | The asset you want. | [optional] 
**ledger_entries** | [**List[LedgerEntryData]**](LedgerEntryData.md) | The asset entries that were changed during the trade. This is an array of at least 2 items with the asset sold and the asset gained. It may also include ledger entries for the costs of the trade and possibly exchange tokens used. | [optional] 
**trade_id** | **str** | The unique ID of the trade used by the exchange. This ID can be used to get the details of this trade at a later time. | [optional] 
**account_id** | **str** | The unique ID of the custodian account used. | [optional] 
**custodian_code** | **str** | The code of the custodian used. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.trade_result_data import TradeResultData

# TODO update the JSON string below
json = "{}"
# create an instance of TradeResultData from a JSON string
trade_result_data_instance = TradeResultData.from_json(json)
# print the JSON string representation of the object
print TradeResultData.to_json()

# convert the object into a dict
trade_result_data_dict = trade_result_data_instance.to_dict()
# create an instance of TradeResultData from a dict
trade_result_data_form_dict = trade_result_data.from_dict(trade_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


