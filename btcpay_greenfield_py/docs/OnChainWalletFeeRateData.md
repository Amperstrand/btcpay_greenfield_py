# OnChainWalletFeeRateData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feerate** | **float** | The fee rate (sats per byte) based on the wallet&#39;s configured recommended block confirmation target | [optional] 

## Example

```python
from openapi_client.models.on_chain_wallet_fee_rate_data import OnChainWalletFeeRateData

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletFeeRateData from a JSON string
on_chain_wallet_fee_rate_data_instance = OnChainWalletFeeRateData.from_json(json)
# print the JSON string representation of the object
print OnChainWalletFeeRateData.to_json()

# convert the object into a dict
on_chain_wallet_fee_rate_data_dict = on_chain_wallet_fee_rate_data_instance.to_dict()
# create an instance of OnChainWalletFeeRateData from a dict
on_chain_wallet_fee_rate_data_form_dict = on_chain_wallet_fee_rate_data.from_dict(on_chain_wallet_fee_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


