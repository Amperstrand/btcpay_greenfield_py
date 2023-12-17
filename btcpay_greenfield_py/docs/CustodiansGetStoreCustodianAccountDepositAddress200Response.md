# CustodiansGetStoreCustodianAccountDepositAddress200Response

A bitcoin address belonging to the custodian

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_address** | **str** | The address to deposit your funds. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.custodians_get_store_custodian_account_deposit_address200_response import CustodiansGetStoreCustodianAccountDepositAddress200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustodiansGetStoreCustodianAccountDepositAddress200Response from a JSON string
custodians_get_store_custodian_account_deposit_address200_response_instance = CustodiansGetStoreCustodianAccountDepositAddress200Response.from_json(json)
# print the JSON string representation of the object
print CustodiansGetStoreCustodianAccountDepositAddress200Response.to_json()

# convert the object into a dict
custodians_get_store_custodian_account_deposit_address200_response_dict = custodians_get_store_custodian_account_deposit_address200_response_instance.to_dict()
# create an instance of CustodiansGetStoreCustodianAccountDepositAddress200Response from a dict
custodians_get_store_custodian_account_deposit_address200_response_form_dict = custodians_get_store_custodian_account_deposit_address200_response.from_dict(custodians_get_store_custodian_account_deposit_address200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


