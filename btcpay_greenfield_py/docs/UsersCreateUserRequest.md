# UsersCreateUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the new user | [optional] 
**password** | **str** | The password of the new user (if no password is set, an email will be sent to the user requiring him to set the password) | [optional] 
**is_administrator** | **bool** | Make this user administrator (only if you have the &#x60;unrestricted&#x60; permission of a server administrator) | [optional] [default to False]

## Example

```python
from openapi_client.models.users_create_user_request import UsersCreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateUserRequest from a JSON string
users_create_user_request_instance = UsersCreateUserRequest.from_json(json)
# print the JSON string representation of the object
print UsersCreateUserRequest.to_json()

# convert the object into a dict
users_create_user_request_dict = users_create_user_request_instance.to_dict()
# create an instance of UsersCreateUserRequest from a dict
users_create_user_request_form_dict = users_create_user_request.from_dict(users_create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


