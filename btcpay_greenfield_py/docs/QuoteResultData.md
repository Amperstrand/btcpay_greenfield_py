# QuoteResultData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_asset** | **str** | The asset to trade. | [optional] 
**to_asset** | **str** | The asset you want. | [optional] 
**bid** | **decimal.Decimal** | The bid price. | [optional] 
**ask** | **decimal.Decimal** | The ask price | [optional] 

## Example

```python
from openapi_client.models.quote_result_data import QuoteResultData

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResultData from a JSON string
quote_result_data_instance = QuoteResultData.from_json(json)
# print the JSON string representation of the object
print QuoteResultData.to_json()

# convert the object into a dict
quote_result_data_dict = quote_result_data_instance.to_dict()
# create an instance of QuoteResultData from a dict
quote_result_data_form_dict = quote_result_data.from_dict(quote_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


