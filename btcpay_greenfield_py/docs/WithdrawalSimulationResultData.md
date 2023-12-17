# WithdrawalSimulationResultData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | The asset that is being withdrawn. | [optional] 
**payment_method** | **str** | The payment method that is used (crypto code + network). | [optional] 
**ledger_entries** | [**List[LedgerEntryData]**](LedgerEntryData.md) | The asset entries that would be changed if this were a real withdrawal. The first item is always the withdrawal itself. It could also includes ledger entries for the costs and may include credits or exchange tokens to give a discount. | [optional] 
**account_id** | **str** | The unique ID of the custodian account used. | [optional] 
**custodian_code** | **str** | The code of the custodian used. | [optional] 
**min_qty** | **decimal.Decimal** | The minimum amount to withdraw | [optional] 
**max_qty** | **decimal.Decimal** | The maximum amount to withdraw | [optional] 

## Example

```python
from btcpay_greenfield_py.models.withdrawal_simulation_result_data import WithdrawalSimulationResultData

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalSimulationResultData from a JSON string
withdrawal_simulation_result_data_instance = WithdrawalSimulationResultData.from_json(json)
# print the JSON string representation of the object
print WithdrawalSimulationResultData.to_json()

# convert the object into a dict
withdrawal_simulation_result_data_dict = withdrawal_simulation_result_data_instance.to_dict()
# create an instance of WithdrawalSimulationResultData from a dict
withdrawal_simulation_result_data_form_dict = withdrawal_simulation_result_data.from_dict(withdrawal_simulation_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


