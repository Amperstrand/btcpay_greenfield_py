# btcpay_greenfield_py.APIKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_keys_create_api_key**](APIKeysApi.md#api_keys_create_api_key) | **POST** /api/v1/api-keys | Create a new API Key
[**api_keys_create_user_api_key**](APIKeysApi.md#api_keys_create_user_api_key) | **POST** /api/v1/users/{idOrEmail}/api-keys | Create a new API Key for a user
[**api_keys_delete_api_key**](APIKeysApi.md#api_keys_delete_api_key) | **DELETE** /api/v1/api-keys/{apikey} | Revoke an API Key
[**api_keys_delete_current_api_key**](APIKeysApi.md#api_keys_delete_current_api_key) | **DELETE** /api/v1/api-keys/current | Revoke the current API Key
[**api_keys_delete_user_api_key**](APIKeysApi.md#api_keys_delete_user_api_key) | **DELETE** /api/v1/users/{idOrEmail}/api-keys/{apikey} | Revoke an API Key of target user
[**api_keys_get_current_api_key**](APIKeysApi.md#api_keys_get_current_api_key) | **GET** /api/v1/api-keys/current | Get the current API Key information


# **api_keys_create_api_key**
> ApiKeyData api_keys_create_api_key(api_keys_create_api_key_request=api_keys_create_api_key_request)

Create a new API Key

Create a new API Key

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.api_key_data import ApiKeyData
from btcpay_greenfield_py.models.api_keys_create_api_key_request import ApiKeysCreateApiKeyRequest
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
    api_instance = btcpay_greenfield_py.APIKeysApi(api_client)
    api_keys_create_api_key_request = btcpay_greenfield_py.ApiKeysCreateApiKeyRequest() # ApiKeysCreateApiKeyRequest |  (optional)

    try:
        # Create a new API Key
        api_response = api_instance.api_keys_create_api_key(api_keys_create_api_key_request=api_keys_create_api_key_request)
        print("The response of APIKeysApi->api_keys_create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_create_api_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_keys_create_api_key_request** | [**ApiKeysCreateApiKeyRequest**](ApiKeysCreateApiKeyRequest.md)|  | [optional] 

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the new api key |  -  |
**401** | Missing authorization |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_create_user_api_key**
> ApiKeyData api_keys_create_user_api_key(id_or_email, api_keys_create_api_key_request=api_keys_create_api_key_request)

Create a new API Key for a user

Create a new API Key for a user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.api_key_data import ApiKeyData
from btcpay_greenfield_py.models.api_keys_create_api_key_request import ApiKeysCreateApiKeyRequest
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
    api_instance = btcpay_greenfield_py.APIKeysApi(api_client)
    id_or_email = 'id_or_email_example' # str | The target user's id or email
    api_keys_create_api_key_request = btcpay_greenfield_py.ApiKeysCreateApiKeyRequest() # ApiKeysCreateApiKeyRequest |  (optional)

    try:
        # Create a new API Key for a user
        api_response = api_instance.api_keys_create_user_api_key(id_or_email, api_keys_create_api_key_request=api_keys_create_api_key_request)
        print("The response of APIKeysApi->api_keys_create_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_create_user_api_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_email** | **str**| The target user&#39;s id or email | 
 **api_keys_create_api_key_request** | [**ApiKeysCreateApiKeyRequest**](ApiKeysCreateApiKeyRequest.md)|  | [optional] 

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the new api key |  -  |
**401** | Missing authorization |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_delete_api_key**
> api_keys_delete_api_key(apikey)

Revoke an API Key

Revoke the current API key so that it cannot be used anymore

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
    api_instance = btcpay_greenfield_py.APIKeysApi(api_client)
    apikey = 'apikey_example' # str | The API Key to revoke

    try:
        # Revoke an API Key
        api_instance.api_keys_delete_api_key(apikey)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_delete_api_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| The API Key to revoke | 

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
**200** | The key has been deleted |  -  |
**404** | The key is not found for this user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_delete_current_api_key**
> ApiKeyData api_keys_delete_current_api_key()

Revoke the current API Key

Revoke the current API key so that it cannot be used anymore

### Example

* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.api_key_data import ApiKeyData
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

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.APIKeysApi(api_client)

    try:
        # Revoke the current API Key
        api_response = api_instance.api_keys_delete_current_api_key()
        print("The response of APIKeysApi->api_keys_delete_current_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_delete_current_api_key: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The key was revoked and is no longer usable |  -  |
**401** | Missing authorization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_delete_user_api_key**
> api_keys_delete_user_api_key(apikey, id_or_email)

Revoke an API Key of target user

Revoke the API key of a target user so that it cannot be used anymore

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
    api_instance = btcpay_greenfield_py.APIKeysApi(api_client)
    apikey = 'apikey_example' # str | The API Key to revoke
    id_or_email = 'id_or_email_example' # str | The target user's id or email

    try:
        # Revoke an API Key of target user
        api_instance.api_keys_delete_user_api_key(apikey, id_or_email)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_delete_user_api_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| The API Key to revoke | 
 **id_or_email** | **str**| The target user&#39;s id or email | 

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
**200** | The key has been deleted |  -  |
**404** | The key is not found for this user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_keys_get_current_api_key**
> ApiKeyData api_keys_get_current_api_key()

Get the current API Key information

View information about the current API key

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.api_key_data import ApiKeyData
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
    api_instance = btcpay_greenfield_py.APIKeysApi(api_client)

    try:
        # Get the current API Key information
        api_response = api_instance.api_keys_get_current_api_key()
        print("The response of APIKeysApi->api_keys_get_current_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_keys_get_current_api_key: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the current api key |  -  |
**401** | Missing authorization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

