# openapi_client.StoresRatesConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stores_get_store_rate_configuration**](StoresRatesConfigApi.md#stores_get_store_rate_configuration) | **GET** /api/v1/stores/{storeId}/rates/configuration | Get store rate settings
[**stores_preview_store_rate_configuration**](StoresRatesConfigApi.md#stores_preview_store_rate_configuration) | **POST** /api/v1/stores/{storeId}/rates/configuration/preview | Preview rate configuration results
[**stores_update_store_rate_configuration**](StoresRatesConfigApi.md#stores_update_store_rate_configuration) | **PUT** /api/v1/stores/{storeId}/rates/configuration | Update store rate settings


# **stores_get_store_rate_configuration**
> StoreRateConfiguration stores_get_store_rate_configuration(store_id)

Get store rate settings

View rate settings of the specified store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.store_rate_configuration import StoreRateConfiguration
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
    api_instance = openapi_client.StoresRatesConfigApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store rate settings
        api_response = api_instance.stores_get_store_rate_configuration(store_id)
        print("The response of StoresRatesConfigApi->stores_get_store_rate_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresRatesConfigApi->stores_get_store_rate_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**StoreRateConfiguration**](StoreRateConfiguration.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified store rate settings |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_preview_store_rate_configuration**
> List[StoreRateResult] stores_preview_store_rate_configuration(store_id, store_rate_configuration, currency_pair=currency_pair)

Preview rate configuration results

Preview rate configuration results before you set it on the store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.store_rate_configuration import StoreRateConfiguration
from openapi_client.models.store_rate_result import StoreRateResult
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
    api_instance = openapi_client.StoresRatesConfigApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    store_rate_configuration = openapi_client.StoreRateConfiguration() # StoreRateConfiguration | 
    currency_pair = ['currency_pair_example'] # List[str] | The currency pairs to preview (optional)

    try:
        # Preview rate configuration results
        api_response = api_instance.stores_preview_store_rate_configuration(store_id, store_rate_configuration, currency_pair=currency_pair)
        print("The response of StoresRatesConfigApi->stores_preview_store_rate_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresRatesConfigApi->stores_preview_store_rate_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **store_rate_configuration** | [**StoreRateConfiguration**](StoreRateConfiguration.md)|  | 
 **currency_pair** | [**List[str]**](str.md)| The currency pairs to preview | [optional] 

### Return type

[**List[StoreRateResult]**](StoreRateResult.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The settings were executed and a preview was returned |  -  |
**400** | A list of errors that occurred when previewing the settings |  -  |
**403** | If you are authenticated but forbidden to modify the store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_update_store_rate_configuration**
> StoreRateConfiguration stores_update_store_rate_configuration(store_id, store_rate_configuration)

Update store rate settings

Update a store's rate settings

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.store_rate_configuration import StoreRateConfiguration
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
    api_instance = openapi_client.StoresRatesConfigApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    store_rate_configuration = openapi_client.StoreRateConfiguration() # StoreRateConfiguration | 

    try:
        # Update store rate settings
        api_response = api_instance.stores_update_store_rate_configuration(store_id, store_rate_configuration)
        print("The response of StoresRatesConfigApi->stores_update_store_rate_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresRatesConfigApi->stores_update_store_rate_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **store_rate_configuration** | [**StoreRateConfiguration**](StoreRateConfiguration.md)|  | 

### Return type

[**StoreRateConfiguration**](StoreRateConfiguration.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The settings were updated |  -  |
**400** | A list of errors that occurred when updating the settings |  -  |
**403** | If you are authenticated but forbidden to modify the store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

