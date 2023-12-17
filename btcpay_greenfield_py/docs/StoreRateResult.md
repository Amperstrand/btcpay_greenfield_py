# StoreRateResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Currency pair in the format of &#x60;BTC_USD&#x60; | [optional] 
**errors** | **List[str]** | Errors relating to this currency pair fetching based on your config | [optional] 
**rate** | **decimal.Decimal** | the rate fetched based on the currency pair | [optional] 

## Example

```python
from btcpay_greenfield_py.models.store_rate_result import StoreRateResult

# TODO update the JSON string below
json = "{}"
# create an instance of StoreRateResult from a JSON string
store_rate_result_instance = StoreRateResult.from_json(json)
# print the JSON string representation of the object
print StoreRateResult.to_json()

# convert the object into a dict
store_rate_result_dict = store_rate_result_instance.to_dict()
# create an instance of StoreRateResult from a dict
store_rate_result_form_dict = store_rate_result.from_dict(store_rate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


