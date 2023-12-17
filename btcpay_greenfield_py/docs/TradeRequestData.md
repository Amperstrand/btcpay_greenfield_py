# TradeRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_asset** | **str** | The asset to trade. | [optional] 
**to_asset** | **str** | The asset you want. | [optional] 
**qty** | [**TradeRequestDataQty**](TradeRequestDataQty.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.trade_request_data import TradeRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TradeRequestData from a JSON string
trade_request_data_instance = TradeRequestData.from_json(json)
# print the JSON string representation of the object
print TradeRequestData.to_json()

# convert the object into a dict
trade_request_data_dict = trade_request_data_instance.to_dict()
# create an instance of TradeRequestData from a dict
trade_request_data_form_dict = trade_request_data.from_dict(trade_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


