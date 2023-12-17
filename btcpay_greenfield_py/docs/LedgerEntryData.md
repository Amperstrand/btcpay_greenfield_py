# LedgerEntryData

A single ledger entry meaning an asset and qty has changed (increased or decreased).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | An asset. | [optional] 
**qty** | **decimal.Decimal** | The quantity changed of the asset. Can be positive or negative. | [optional] 
**type** | **str** | Trade, Fee or Withdrawal | [optional] 

## Example

```python
from btcpay_greenfield_py.models.ledger_entry_data import LedgerEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerEntryData from a JSON string
ledger_entry_data_instance = LedgerEntryData.from_json(json)
# print the JSON string representation of the object
print LedgerEntryData.to_json()

# convert the object into a dict
ledger_entry_data_dict = ledger_entry_data_instance.to_dict()
# create an instance of LedgerEntryData from a dict
ledger_entry_data_form_dict = ledger_entry_data.from_dict(ledger_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


