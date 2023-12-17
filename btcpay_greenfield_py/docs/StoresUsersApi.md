# btcpay_greenfield_py.StoresUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stores_add_store_user**](StoresUsersApi.md#stores_add_store_user) | **POST** /api/v1/stores/{storeId}/users | Add a store user
[**stores_get_store_users**](StoresUsersApi.md#stores_get_store_users) | **GET** /api/v1/stores/{storeId}/users | Get store users
[**stores_remove_store_user**](StoresUsersApi.md#stores_remove_store_user) | **DELETE** /api/v1/stores/{storeId}/users/{idOrEmail} | Remove Store User


# **stores_add_store_user**
> stores_add_store_user(store_id, store_user_data)

Add a store user

Add a store user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.store_user_data import StoreUserData
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
    api_instance = btcpay_greenfield_py.StoresUsersApi(api_client)
    store_id = 'store_id_example' # str | The store id
    store_user_data = btcpay_greenfield_py.StoreUserData() # StoreUserData | 

    try:
        # Add a store user
        api_instance.stores_add_store_user(store_id, store_user_data)
    except Exception as e:
        print("Exception when calling StoresUsersApi->stores_add_store_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **store_user_data** | [**StoreUserData**](StoreUserData.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user was added |  -  |
**400** | A list of errors that occurred when creating the store |  -  |
**403** | If you are authenticated but forbidden to add new stores |  -  |
**409** | Error code: &#x60;duplicate-store-user-role&#x60;. Removing this user would result in the store having no owner. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_get_store_users**
> List[StoreUserData] stores_get_store_users(store_id)

Get store users

View users of the specified store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.store_user_data import StoreUserData
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
    api_instance = btcpay_greenfield_py.StoresUsersApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store users
        api_response = api_instance.stores_get_store_users(store_id)
        print("The response of StoresUsersApi->stores_get_store_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresUsersApi->stores_get_store_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[StoreUserData]**](StoreUserData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified store users |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_remove_store_user**
> stores_remove_store_user(store_id, id_or_email)

Remove Store User

Removes the specified store user. If there is no other owner, this endpoint will fail.

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
    api_instance = btcpay_greenfield_py.StoresUsersApi(api_client)
    store_id = 'store_id_example' # str | The store
    id_or_email = 'id_or_email_example' # str | The user's id or email

    try:
        # Remove Store User
        api_instance.stores_remove_store_user(store_id, id_or_email)
    except Exception as e:
        print("Exception when calling StoresUsersApi->stores_remove_store_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store | 
 **id_or_email** | **str**| The user&#39;s id or email | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user has been removed |  -  |
**400** | A list of errors that occurred when removing the store |  -  |
**409** | Error code: &#x60;store-user-role-orphaned&#x60;. Removing this user would result in the store having no owner. |  -  |
**403** | If you are authenticated but forbidden to remove the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

