# WithdrawalResultData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | The asset that is being withdrawn. | [optional] 
**payment_method** | **str** | The payment method that is used (crypto code + network). | [optional] 
**ledger_entries** | [**List[LedgerEntryData]**](LedgerEntryData.md) | The asset entries that were changed during the withdrawal. The first item is always the withdrawal itself. It could also includes ledger entries for the costs and may include credits or exchange tokens to give a discount. | [optional] 
**withdrawal_id** | **str** | The unique ID of the withdrawal used by the exchange. | [optional] 
**account_id** | **str** | The unique ID of the custodian account used. | [optional] 
**custodian_code** | **str** | The code of the custodian used. | [optional] 
**status** | **str** | The status of the withdrawal: &#39;Queued&#39;, &#39;Complete&#39;, &#39;Failed&#39; or &#39;Unknown&#39;. | [optional] 
**transaction_id** | **str** | The transaction ID on the blockchain once the withdrawal has been executed. | [optional] 
**target_address** | **str** | The address where the funds were sent to once the withdrawal has been executed. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.withdrawal_result_data import WithdrawalResultData

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalResultData from a JSON string
withdrawal_result_data_instance = WithdrawalResultData.from_json(json)
# print the JSON string representation of the object
print WithdrawalResultData.to_json()

# convert the object into a dict
withdrawal_result_data_dict = withdrawal_result_data_instance.to_dict()
# create an instance of WithdrawalResultData from a dict
withdrawal_result_data_form_dict = withdrawal_result_data.from_dict(withdrawal_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


