# CreateOnChainTransactionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**List[CreateOnChainTransactionRequestDestination]**](CreateOnChainTransactionRequestDestination.md) | What and where to send money | [optional] 
**feerate** | **float** | Transaction fee. | [optional] 
**proceed_with_payjoin** | **bool** | Whether to attempt to do a BIP78 payjoin if one of the destinations is a BIP21 with payjoin enabled | [optional] [default to True]
**proceed_with_broadcast** | **bool** | Whether to broadcast the transaction after creating it or to simply return the transaction in hex format. | [optional] [default to True]
**no_change** | **bool** | Whether to send all the spent coins to the destinations (THIS CAN COST YOU SIGNIFICANT AMOUNTS OF MONEY, LEAVE FALSE UNLESS YOU KNOW WHAT YOU ARE DOING). | [optional] [default to False]
**rbf** | **bool** | Whether to enable RBF for the transaction. Leave blank to have it random (beneficial to privacy) | [optional] 
**exclude_unconfirmed** | **bool** | Whether to exclude unconfirmed UTXOs from the transaction. | [optional] [default to False]
**selected_inputs** | **List[str]** | Restrict the creation of the transactions from the outpoints provided ONLY (coin selection) | [optional] 

## Example

```python
from openapi_client.models.create_on_chain_transaction_request import CreateOnChainTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOnChainTransactionRequest from a JSON string
create_on_chain_transaction_request_instance = CreateOnChainTransactionRequest.from_json(json)
# print the JSON string representation of the object
print CreateOnChainTransactionRequest.to_json()

# convert the object into a dict
create_on_chain_transaction_request_dict = create_on_chain_transaction_request_instance.to_dict()
# create an instance of CreateOnChainTransactionRequest from a dict
create_on_chain_transaction_request_form_dict = create_on_chain_transaction_request.from_dict(create_on_chain_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


