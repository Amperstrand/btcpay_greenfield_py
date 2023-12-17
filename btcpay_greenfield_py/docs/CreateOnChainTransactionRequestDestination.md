# CreateOnChainTransactionRequestDestination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | A wallet address or a BIP21 payment link | [optional] 
**amount** | **decimal.Decimal** | The amount to send. If &#x60;destination&#x60; is a BIP21 link, the amount must be the same or null. | [optional] 
**subtract_from_amount** | **bool** | Whether to subtract the transaction fee from the provided amount. This makes the receiver receive less, or in other words: he or she pays the transaction fee. Also useful if you want to clear out your wallet. Must be false if &#x60;destination&#x60; is a BIP21 link | [optional] 

## Example

```python
from btcpay_greenfield_py.models.create_on_chain_transaction_request_destination import CreateOnChainTransactionRequestDestination

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOnChainTransactionRequestDestination from a JSON string
create_on_chain_transaction_request_destination_instance = CreateOnChainTransactionRequestDestination.from_json(json)
# print the JSON string representation of the object
print CreateOnChainTransactionRequestDestination.to_json()

# convert the object into a dict
create_on_chain_transaction_request_destination_dict = create_on_chain_transaction_request_destination_instance.to_dict()
# create an instance of CreateOnChainTransactionRequestDestination from a dict
create_on_chain_transaction_request_destination_form_dict = create_on_chain_transaction_request_destination.from_dict(create_on_chain_transaction_request_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


