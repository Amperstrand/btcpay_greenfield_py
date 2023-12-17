# CustodianAccountData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique code of the customer&#39;s account with this custodian. The format depends on the custodian. | [optional] 
**store_id** | **str** | The store ID. | [optional] 
**custodian_code** | **str** | The code for the custodian. | [optional] 
**name** | **str** | The name of the custodian account. | [optional] 
**asset_balances** | [**List[AssetBalanceData]**](AssetBalanceData.md) | A real-time loaded list of all assets (fiat and crypto) on this custodian and the quantity held in the account. Assets with qty 0 can be omitted. | [optional] 
**config** | **object** | The configuration of this custodian account. Specific contents depend on the custodian and your access permissions. | [optional] 

## Example

```python
from openapi_client.models.custodian_account_data import CustodianAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of CustodianAccountData from a JSON string
custodian_account_data_instance = CustodianAccountData.from_json(json)
# print the JSON string representation of the object
print CustodianAccountData.to_json()

# convert the object into a dict
custodian_account_data_dict = custodian_account_data_instance.to_dict()
# create an instance of CustodianAccountData from a dict
custodian_account_data_form_dict = custodian_account_data.from_dict(custodian_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


