# StoreUserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The id of the user | [optional] 
**role** | **str** | The role of the user. Default roles are &#x60;Owner&#x60; and &#x60;Guest&#x60; | [optional] 

## Example

```python
from btcpay_greenfield_py.models.store_user_data import StoreUserData

# TODO update the JSON string below
json = "{}"
# create an instance of StoreUserData from a JSON string
store_user_data_instance = StoreUserData.from_json(json)
# print the JSON string representation of the object
print StoreUserData.to_json()

# convert the object into a dict
store_user_data_dict = store_user_data_instance.to_dict()
# create an instance of StoreUserData from a dict
store_user_data_form_dict = store_user_data.from_dict(store_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


