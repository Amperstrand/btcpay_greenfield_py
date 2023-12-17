# OnChainWalletUTXOData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A comment linked to this utxo | [optional] 
**amount** | **str** | the value of this utxo | [optional] 
**link** | **str** | a link to the configured blockchain explorer to view the utxo | [optional] 
**outpoint** | **str** | outpoint of this utxo | [optional] 
**timestamp** | **float** | A unix timestamp in seconds | [optional] 
**key_path** | **str** | the derivation path in relation to the HD account | [optional] 
**address** | **str** | The wallet address of this utxo | [optional] 
**confirmations** | **float** | The number of confirmations of this utxo | [optional] 
**labels** | [**List[LabelData]**](LabelData.md) | Labels linked to this transaction | [optional] 

## Example

```python
from btcpay_greenfield_py.models.on_chain_wallet_utxo_data import OnChainWalletUTXOData

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainWalletUTXOData from a JSON string
on_chain_wallet_utxo_data_instance = OnChainWalletUTXOData.from_json(json)
# print the JSON string representation of the object
print OnChainWalletUTXOData.to_json()

# convert the object into a dict
on_chain_wallet_utxo_data_dict = on_chain_wallet_utxo_data_instance.to_dict()
# create an instance of OnChainWalletUTXOData from a dict
on_chain_wallet_utxo_data_form_dict = on_chain_wallet_utxo_data.from_dict(on_chain_wallet_utxo_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


