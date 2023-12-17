# OnChainWalletOverviewData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **decimal.Decimal** | The total current balance of the wallet | [optional] 
**unconfirmed_balance** | **decimal.Decimal** | The current unconfirmed balance of the wallet | [optional] 
**confirmed_balance** | **decimal.Decimal** | The current confirmed balance of the wallet | [optional] 

## Example

```python
from btcpay_greenfield_py.models.on_chain_wallet_overview_data import OnChainWalletOverviewData

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletOverviewData from a JSON string
on_chain_wallet_overview_data_instance = OnChainWalletOverviewData.from_json(json)
# print the JSON string representation of the object
print OnChainWalletOverviewData.to_json()

# convert the object into a dict
on_chain_wallet_overview_data_dict = on_chain_wallet_overview_data_instance.to_dict()
# create an instance of OnChainWalletOverviewData from a dict
on_chain_wallet_overview_data_form_dict = on_chain_wallet_overview_data.from_dict(on_chain_wallet_overview_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


