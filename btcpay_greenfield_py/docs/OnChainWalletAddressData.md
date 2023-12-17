# OnChainWalletAddressData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The bitcoin address | [optional] 
**key_path** | **str** | the derivation path in relation to the HD account | [optional] 
**payment_link** | **str** | a bip21 payment link | [optional] 

## Example

```python
from btcpay_greenfield_py.models.on_chain_wallet_address_data import OnChainWalletAddressData

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletAddressData from a JSON string
on_chain_wallet_address_data_instance = OnChainWalletAddressData.from_json(json)
# print the JSON string representation of the object
print OnChainWalletAddressData.to_json()

# convert the object into a dict
on_chain_wallet_address_data_dict = on_chain_wallet_address_data_instance.to_dict()
# create an instance of OnChainWalletAddressData from a dict
on_chain_wallet_address_data_form_dict = on_chain_wallet_address_data.from_dict(on_chain_wallet_address_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


