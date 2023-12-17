# openapi_client.StorePaymentMethodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_payment_methods_get_store_payment_methods**](StorePaymentMethodsApi.md#store_payment_methods_get_store_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods | Get store payment methods


# **store_payment_methods_get_store_payment_methods**
> List[GenericPaymentMethodData] store_payment_methods_get_store_payment_methods(store_id, enabled=enabled)

Get store payment methods

View information about the stores' configured payment methods

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.generic_payment_method_data import GenericPaymentMethodData
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
    api_instance = openapi_client.StorePaymentMethodsApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    enabled = True # bool | Fetch payment methods that are enabled/disabled only (optional)

    try:
        # Get store payment methods
        api_response = api_instance.store_payment_methods_get_store_payment_methods(store_id, enabled=enabled)
        print("The response of StorePaymentMethodsApi->store_payment_methods_get_store_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsApi->store_payment_methods_get_store_payment_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**List[GenericPaymentMethodData]**](GenericPaymentMethodData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of payment methods |  -  |
**401** | Missing authorization |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

