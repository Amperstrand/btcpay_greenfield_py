# CreateCustodianAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique code of the customer&#39;s account with this custodian. The format depends on the custodian. | [optional] 
**store_id** | **str** | The store ID. | [optional] 
**custodian_code** | **str** | The code for the custodian. | [optional] 
**name** | **str** | The name of the custodian account. | [optional] 
**config** | **object** | The configuration of this custodian account. Specific contents depend on the custodian and your access permissions. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.create_custodian_account_request import CreateCustodianAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustodianAccountRequest from a JSON string
create_custodian_account_request_instance = CreateCustodianAccountRequest.from_json(json)
# print the JSON string representation of the object
print CreateCustodianAccountRequest.to_json()

# convert the object into a dict
create_custodian_account_request_dict = create_custodian_account_request_instance.to_dict()
# create an instance of CreateCustodianAccountRequest from a dict
create_custodian_account_request_form_dict = create_custodian_account_request.from_dict(create_custodian_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


