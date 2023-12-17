# LockUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locked** | **bool** | Whether to lock or unlock the user | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lock_user_request import LockUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockUserRequest from a JSON string
lock_user_request_instance = LockUserRequest.from_json(json)
# print the JSON string representation of the object
print LockUserRequest.to_json()

# convert the object into a dict
lock_user_request_dict = lock_user_request_instance.to_dict()
# create an instance of LockUserRequest from a dict
lock_user_request_form_dict = lock_user_request.from_dict(lock_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


