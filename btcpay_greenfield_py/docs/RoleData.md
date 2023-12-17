# RoleData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The role&#39;s Id (Same as role if the role is created at server level, if the role is created at the store level the format is &#x60;STOREID::ROLE&#x60;) | [optional] 
**role** | **str** | The role&#39;s name | [optional] 
**permissions** | **List[str]** | The permissions attached to this role | [optional] 
**is_server_role** | **bool** | Whether this role is at the scope of the store or scope of the server | [optional] 

## Example

```python
from btcpay_greenfield_py.models.role_data import RoleData

# TODO update the JSON string below
json = "{}"
# create an instance of RoleData from a JSON string
role_data_instance = RoleData.from_json(json)
# print the JSON string representation of the object
print RoleData.to_json()

# convert the object into a dict
role_data_dict = role_data_instance.to_dict()
# create an instance of RoleData from a dict
role_data_form_dict = role_data.from_dict(role_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


