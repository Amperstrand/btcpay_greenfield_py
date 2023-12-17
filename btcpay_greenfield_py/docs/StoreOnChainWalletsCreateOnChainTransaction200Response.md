# StoreOnChainWalletsCreateOnChainTransaction200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** | The transaction id | [optional] 
**comment** | **str** | A comment linked to the transaction | [optional] 
**amount** | **decimal.Decimal** | The amount the wallet balance changed with this transaction | [optional] 
**block_hash** | **str** | The hash of the block that confirmed this transaction. Null if still unconfirmed. | [optional] 
**block_height** | **str** | The height of the block that confirmed this transaction. Null if still unconfirmed. | [optional] 
**confirmations** | **str** | The number of confirmations for this transaction | [optional] 
**timestamp** | **float** | A unix timestamp in seconds | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**labels** | [**List[LabelData]**](LabelData.md) | Labels linked to this transaction | [optional] 

## Example

```python
from btcpay_greenfield_py.models.store_on_chain_wallets_create_on_chain_transaction200_response import StoreOnChainWalletsCreateOnChainTransaction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoreOnChainWalletsCreateOnChainTransaction200Response from a JSON string
store_on_chain_wallets_create_on_chain_transaction200_response_instance = StoreOnChainWalletsCreateOnChainTransaction200Response.from_json(json)
# print the JSON string representation of the object
print StoreOnChainWalletsCreateOnChainTransaction200Response.to_json()

# convert the object into a dict
store_on_chain_wallets_create_on_chain_transaction200_response_dict = store_on_chain_wallets_create_on_chain_transaction200_response_instance.to_dict()
# create an instance of StoreOnChainWalletsCreateOnChainTransaction200Response from a dict
store_on_chain_wallets_create_on_chain_transaction200_response_form_dict = store_on_chain_wallets_create_on_chain_transaction200_response.from_dict(store_on_chain_wallets_create_on_chain_transaction200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


