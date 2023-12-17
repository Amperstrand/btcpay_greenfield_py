# btcpay_greenfield_py.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create_user**](UsersApi.md#users_create_user) | **POST** /api/v1/users | Create user
[**users_delete_current_user**](UsersApi.md#users_delete_current_user) | **DELETE** /api/v1/users/me | Deletes user profile
[**users_delete_user**](UsersApi.md#users_delete_user) | **DELETE** /api/v1/users/{idOrEmail} | Delete user
[**users_get_current_user**](UsersApi.md#users_get_current_user) | **GET** /api/v1/users/me | Get current user information
[**users_get_user**](UsersApi.md#users_get_user) | **GET** /api/v1/users/{idOrEmail} | Get user by ID or Email
[**users_get_users**](UsersApi.md#users_get_users) | **GET** /api/v1/users | Get all users
[**users_toggle_user_lock**](UsersApi.md#users_toggle_user_lock) | **POST** /api/v1/users/{idOrEmail}/lock | Toggle user


# **users_create_user**
> ApplicationUserData users_create_user(users_create_user_request)

Create user

Create a new user.  This operation can be called without authentication in any of this cases: * There is not any administrator yet on the server, * The subscriptions are not disabled in the server's policies.  If the first administrator is created by this call, subscriptions are automatically disabled.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.application_user_data import ApplicationUserData
from btcpay_greenfield_py.models.users_create_user_request import UsersCreateUserRequest
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)
    users_create_user_request = btcpay_greenfield_py.UsersCreateUserRequest() # UsersCreateUserRequest | 

    try:
        # Create user
        api_response = api_instance.users_create_user(users_create_user_request)
        print("The response of UsersApi->users_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_create_user_request** | [**UsersCreateUserRequest**](UsersCreateUserRequest.md)|  | 

### Return type

[**ApplicationUserData**](ApplicationUserData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information about the new user |  -  |
**400** | A list of errors that occurred when creating the user |  -  |
**401** | If you need to authenticate for this endpoint (ie. the server settings policies lock subscriptions and that an admin already exists) |  -  |
**403** | If you are authenticated but forbidden to create a new user (ie. you don&#39;t have the &#x60;unrestricted&#x60; permission on a server administrator or if you are not administrator and registrations are disabled in the server&#39;s policies) |  -  |
**429** | DDoS protection if you are creating more than 2 accounts every minutes (non-admin only) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_current_user**
> users_delete_current_user()

Deletes user profile

Deletes user profile and associated user data for user making the request

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)

    try:
        # Deletes user profile
        api_instance.users_delete_current_user()
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_current_user: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User and associated data deleted successfully |  -  |
**404** | The user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_user**
> users_delete_user(id_or_email)

Delete user

Delete a user.  Must be an admin to perform this operation.  Attempting to delete the only admin user will not succeed.  All data associated with the user will be deleted as well if the operation succeeds.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)
    id_or_email = 'id_or_email_example' # str | The ID or email of the user to be deleted

    try:
        # Delete user
        api_instance.users_delete_user(id_or_email)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_email** | **str**| The ID or email of the user to be deleted | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User has been successfully deleted |  -  |
**401** | Missing authorization for deleting the user |  -  |
**403** | Authorized but forbidden to delete the user. Can happen if you attempt to delete the only admin user. |  -  |
**404** | User with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_current_user**
> ApplicationUserData users_get_current_user()

Get current user information

View information about the current user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.application_user_data import ApplicationUserData
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)

    try:
        # Get current user information
        api_response = api_instance.users_get_current_user()
        print("The response of UsersApi->users_get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_current_user: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationUserData**](ApplicationUserData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the current user |  -  |
**404** | The user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user**
> users_get_user(id_or_email)

Get user by ID or Email

Get 1 user by ID or Email.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)
    id_or_email = 'id_or_email_example' # str | The ID or email of the user to load

    try:
        # Get user by ID or Email
        api_instance.users_get_user(id_or_email)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_email** | **str**| The ID or email of the user to load | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User found |  -  |
**401** | Missing authorization for loading the user |  -  |
**403** | Authorized but forbidden to load the user. You have the wrong API permissions. |  -  |
**404** | No user found with this ID or email |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_users**
> users_get_users()

Get all users

Load all users that exist.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)

    try:
        # Get all users
        api_instance.users_get_users()
    except Exception as e:
        print("Exception when calling UsersApi->users_get_users: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users found |  -  |
**401** | Missing authorization for loading the users |  -  |
**403** | Authorized but forbidden to load the users. You have the wrong API permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_toggle_user_lock**
> users_toggle_user_lock(id_or_email, lock_user_request=lock_user_request)

Toggle user

Lock or unlock a user.  Must be an admin to perform this operation.  Attempting to lock the only admin user will not succeed.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lock_user_request import LockUserRequest
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = btcpay_greenfield_py.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.UsersApi(api_client)
    id_or_email = 'id_or_email_example' # str | The ID of the user to be un/locked
    lock_user_request = btcpay_greenfield_py.LockUserRequest() # LockUserRequest |  (optional)

    try:
        # Toggle user
        api_instance.users_toggle_user_lock(id_or_email, lock_user_request=lock_user_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_toggle_user_lock: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_email** | **str**| The ID of the user to be un/locked | 
 **lock_user_request** | [**LockUserRequest**](LockUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User has been successfully toggled |  -  |
**401** | Missing authorization for deleting the user |  -  |
**403** | Authorized but forbidden to disable  the user. Can happen if you attempt to disable the only admin user. |  -  |
**404** | User with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

