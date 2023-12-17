# CustodianData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique code of the custodian. | [optional] 
**label** | **str** | The name of the custodian. | [optional] 
**depositable_payment_methods** | **List[str]** | A list of payment methods (crypto code + network) you can deposit to the custodian. | [optional] 
**withdrawable_payment_methods** | **List[str]** | A list of payment methods (crypto code + network) you can withdraw from the custodian. | [optional] 
**tradable_asset_pairs** | [**List[AssetPairData]**](AssetPairData.md) | A list of tradable asset pair objects, or NULL if the custodian cannot trades/convert assets. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.custodian_data import CustodianData

# TODO update the JSON string below
json = "{}"
# create an instance of CustodianData from a JSON string
custodian_data_instance = CustodianData.from_json(json)
# print the JSON string representation of the object
print CustodianData.to_json()

# convert the object into a dict
custodian_data_dict = custodian_data_instance.to_dict()
# create an instance of CustodianData from a dict
custodian_data_form_dict = custodian_data.from_dict(custodian_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


