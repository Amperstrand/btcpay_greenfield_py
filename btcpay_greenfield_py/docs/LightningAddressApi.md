# openapi_client.LightningAddressApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_lightning_addresses_add_or_update_store_lightning_address**](LightningAddressApi.md#store_lightning_addresses_add_or_update_store_lightning_address) | **POST** /api/v1/stores/{storeId}/lightning-addresses/{username} | Add or update store configured lightning address
[**store_lightning_addresses_get_store_lightning_address**](LightningAddressApi.md#store_lightning_addresses_get_store_lightning_address) | **GET** /api/v1/stores/{storeId}/lightning-addresses/{username} | Get store configured lightning address
[**store_lightning_addresses_get_store_lightning_addresses**](LightningAddressApi.md#store_lightning_addresses_get_store_lightning_addresses) | **GET** /api/v1/stores/{storeId}/lightning-addresses | Get store configured lightning addresses
[**store_lightning_addresses_remove_store_lightning_address**](LightningAddressApi.md#store_lightning_addresses_remove_store_lightning_address) | **DELETE** /api/v1/stores/{storeId}/lightning-addresses/{username} | Remove configured lightning address


# **store_lightning_addresses_add_or_update_store_lightning_address**
> LightningAddressData store_lightning_addresses_add_or_update_store_lightning_address(store_id, username, lightning_address_data)

Add or update store configured lightning address

Add or update store configured lightning address

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.lightning_address_data import LightningAddressData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LightningAddressApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    username = 'username_example' # str | the lightning address username
    lightning_address_data = openapi_client.LightningAddressData() # LightningAddressData | 

    try:
        # Add or update store configured lightning address
        api_response = api_instance.store_lightning_addresses_add_or_update_store_lightning_address(store_id, username, lightning_address_data)
        print("The response of LightningAddressApi->store_lightning_addresses_add_or_update_store_lightning_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningAddressApi->store_lightning_addresses_add_or_update_store_lightning_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **username** | **str**| the lightning address username | 
 **lightning_address_data** | [**LightningAddressData**](LightningAddressData.md)|  | 

### Return type

[**LightningAddressData**](LightningAddressData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The lightning address configured in the store |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_addresses_get_store_lightning_address**
> LightningAddressData store_lightning_addresses_get_store_lightning_address(username, store_id)

Get store configured lightning address

Get store configured lightning address

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.lightning_address_data import LightningAddressData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LightningAddressApi(api_client)
    username = 'username_example' # str | The lightning address username
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store configured lightning address
        api_response = api_instance.store_lightning_addresses_get_store_lightning_address(username, store_id)
        print("The response of LightningAddressApi->store_lightning_addresses_get_store_lightning_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningAddressApi->store_lightning_addresses_get_store_lightning_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The lightning address username | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**LightningAddressData**](LightningAddressData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The lightning address configured in the store |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_addresses_get_store_lightning_addresses**
> List[LightningAddressData] store_lightning_addresses_get_store_lightning_addresses(store_id)

Get store configured lightning addresses

Get store configured lightning addresses

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.lightning_address_data import LightningAddressData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LightningAddressApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store configured lightning addresses
        api_response = api_instance.store_lightning_addresses_get_store_lightning_addresses(store_id)
        print("The response of LightningAddressApi->store_lightning_addresses_get_store_lightning_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningAddressApi->store_lightning_addresses_get_store_lightning_addresses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[LightningAddressData]**](LightningAddressData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The lightning addresses configured in the store |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_addresses_remove_store_lightning_address**
> store_lightning_addresses_remove_store_lightning_address(username, store_id)

Remove configured lightning address

Remove store configured lightning address

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LightningAddressApi(api_client)
    username = 'username_example' # str | The lightning address username
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Remove configured lightning address
        api_instance.store_lightning_addresses_remove_store_lightning_address(username, store_id)
    except Exception as e:
        print("Exception when calling LightningAddressApi->store_lightning_addresses_remove_store_lightning_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The lightning address username | 
 **store_id** | **str**| The store to fetch | 

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
**200** | Lightning address removed |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

