# openapi_client.StorePaymentMethodsOnChainApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_on_chain_payment_methods_delete_on_chain_payment_method**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_delete_on_chain_payment_method) | **DELETE** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode} | Remove store on-chain payment method
[**store_on_chain_payment_methods_generate_on_chain_wallet**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_generate_on_chain_wallet) | **POST** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/generate | Generate store on-chain wallet
[**store_on_chain_payment_methods_get_on_chain_payment_method**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_get_on_chain_payment_method) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode} | Get store on-chain payment method
[**store_on_chain_payment_methods_get_on_chain_payment_method_preview**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_get_on_chain_payment_method_preview) | **GET** /api/v1/stores/{storeId}/payment-methods/OnChain/{cryptoCode}/preview | Preview store on-chain payment method addresses
[**store_on_chain_payment_methods_get_on_chain_payment_methods**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_get_on_chain_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods/OnChain | Get store on-chain payment methods
[**store_on_chain_payment_methods_poston_chain_payment_method_preview**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_poston_chain_payment_method_preview) | **POST** /api/v1/stores/{storeId}/payment-methods/OnChain/{cryptoCode}/preview | Preview proposed store on-chain payment method addresses
[**store_on_chain_payment_methods_update_on_chain_payment_method**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_update_on_chain_payment_method) | **PUT** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode} | Update store on-chain payment method


# **store_on_chain_payment_methods_delete_on_chain_payment_method**
> store_on_chain_payment_methods_delete_on_chain_payment_method(crypto_code, store_id)

Remove store on-chain payment method

Removes the specified store payment method.

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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to update
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Remove store on-chain payment method
        api_instance.store_on_chain_payment_methods_delete_on_chain_payment_method(crypto_code, store_id)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_delete_on_chain_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to update | 
 **store_id** | **str**| The store to fetch | 

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
**200** | The payment method has been removed |  -  |
**400** | A list of errors that occurred when removing the payment method |  -  |
**403** | If you are authenticated but forbidden to remove the specified payment method |  -  |
**404** | The key is not found for this store/payment-method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_generate_on_chain_wallet**
> OnChainPaymentMethodDataWithSensitiveData store_on_chain_payment_methods_generate_on_chain_wallet(crypto_code, store_id, generate_on_chain_wallet_request)

Generate store on-chain wallet

Generate a wallet and update the specified store's payment method to it

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.generate_on_chain_wallet_request import GenerateOnChainWalletRequest
from openapi_client.models.on_chain_payment_method_data_with_sensitive_data import OnChainPaymentMethodDataWithSensitiveData
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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to update
    store_id = 'store_id_example' # str | The store to fetch
    generate_on_chain_wallet_request = openapi_client.GenerateOnChainWalletRequest() # GenerateOnChainWalletRequest | 

    try:
        # Generate store on-chain wallet
        api_response = api_instance.store_on_chain_payment_methods_generate_on_chain_wallet(crypto_code, store_id, generate_on_chain_wallet_request)
        print("The response of StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_generate_on_chain_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_generate_on_chain_wallet: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to update | 
 **store_id** | **str**| The store to fetch | 
 **generate_on_chain_wallet_request** | [**GenerateOnChainWalletRequest**](GenerateOnChainWalletRequest.md)|  | 

### Return type

[**OnChainPaymentMethodDataWithSensitiveData**](OnChainPaymentMethodDataWithSensitiveData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated specified payment method with the generated wallet |  -  |
**400** | A list of errors that occurred when updating the store payment method |  -  |
**403** | If you are authenticated but forbidden to update the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_get_on_chain_payment_method**
> OnChainPaymentMethodData store_on_chain_payment_methods_get_on_chain_payment_method(crypto_code, store_id)

Get store on-chain payment method

View information about the specified payment method

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_payment_method_data import OnChainPaymentMethodData
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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store on-chain payment method
        api_response = api_instance.store_on_chain_payment_methods_get_on_chain_payment_method(crypto_code, store_id)
        print("The response of StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**OnChainPaymentMethodData**](OnChainPaymentMethodData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified payment method |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/payment method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_get_on_chain_payment_method_preview**
> OnChainPaymentMethodPreviewResultData store_on_chain_payment_methods_get_on_chain_payment_method_preview(crypto_code, store_id, offset=offset, amount=amount)

Preview store on-chain payment method addresses

View addresses of the current payment method of the store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_payment_method_preview_result_data import OnChainPaymentMethodPreviewResultData
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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    offset = 3.4 # float | From which index to fetch the addresses (optional)
    amount = 3.4 # float | Number of addresses to preview (optional)

    try:
        # Preview store on-chain payment method addresses
        api_response = api_instance.store_on_chain_payment_methods_get_on_chain_payment_method_preview(crypto_code, store_id, offset=offset, amount=amount)
        print("The response of StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_method_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_method_preview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **offset** | **float**| From which index to fetch the addresses | [optional] 
 **amount** | **float**| Number of addresses to preview | [optional] 

### Return type

[**OnChainPaymentMethodPreviewResultData**](OnChainPaymentMethodPreviewResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified payment method addresses |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/payment method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_get_on_chain_payment_methods**
> List[OnChainPaymentMethodData] store_on_chain_payment_methods_get_on_chain_payment_methods(store_id, enabled=enabled)

Get store on-chain payment methods

View information about the stores' configured on-chain payment methods

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_payment_method_data import OnChainPaymentMethodData
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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    enabled = True # bool | Fetch payment methods that are enabled/disabled only (optional)

    try:
        # Get store on-chain payment methods
        api_response = api_instance.store_on_chain_payment_methods_get_on_chain_payment_methods(store_id, enabled=enabled)
        print("The response of StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**List[OnChainPaymentMethodData]**](OnChainPaymentMethodData.md)

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

# **store_on_chain_payment_methods_poston_chain_payment_method_preview**
> OnChainPaymentMethodPreviewResultData store_on_chain_payment_methods_poston_chain_payment_method_preview(crypto_code, store_id, store_on_chain_payment_methods_poston_chain_payment_method_preview_request, offset=offset, amount=amount)

Preview proposed store on-chain payment method addresses

View addresses of a proposed payment method of the store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_payment_method_preview_result_data import OnChainPaymentMethodPreviewResultData
from openapi_client.models.store_on_chain_payment_methods_poston_chain_payment_method_preview_request import StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewRequest
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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    store_on_chain_payment_methods_poston_chain_payment_method_preview_request = openapi_client.StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewRequest() # StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewRequest | 
    offset = 3.4 # float | From which index to fetch the addresses (optional)
    amount = 3.4 # float | Number of addresses to preview (optional)

    try:
        # Preview proposed store on-chain payment method addresses
        api_response = api_instance.store_on_chain_payment_methods_poston_chain_payment_method_preview(crypto_code, store_id, store_on_chain_payment_methods_poston_chain_payment_method_preview_request, offset=offset, amount=amount)
        print("The response of StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_poston_chain_payment_method_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_poston_chain_payment_method_preview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **store_on_chain_payment_methods_poston_chain_payment_method_preview_request** | [**StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewRequest**](StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewRequest.md)|  | 
 **offset** | **float**| From which index to fetch the addresses | [optional] 
 **amount** | **float**| Number of addresses to preview | [optional] 

### Return type

[**OnChainPaymentMethodPreviewResultData**](OnChainPaymentMethodPreviewResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified payment method addresses |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_update_on_chain_payment_method**
> OnChainPaymentMethodData store_on_chain_payment_methods_update_on_chain_payment_method(crypto_code, store_id, update_on_chain_payment_method_request)

Update store on-chain payment method

Update the specified store's payment method

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_payment_method_data import OnChainPaymentMethodData
from openapi_client.models.update_on_chain_payment_method_request import UpdateOnChainPaymentMethodRequest
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
    api_instance = openapi_client.StorePaymentMethodsOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to update
    store_id = 'store_id_example' # str | The store to fetch
    update_on_chain_payment_method_request = openapi_client.UpdateOnChainPaymentMethodRequest() # UpdateOnChainPaymentMethodRequest | 

    try:
        # Update store on-chain payment method
        api_response = api_instance.store_on_chain_payment_methods_update_on_chain_payment_method(crypto_code, store_id, update_on_chain_payment_method_request)
        print("The response of StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_update_on_chain_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_update_on_chain_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to update | 
 **store_id** | **str**| The store to fetch | 
 **update_on_chain_payment_method_request** | [**UpdateOnChainPaymentMethodRequest**](UpdateOnChainPaymentMethodRequest.md)|  | 

### Return type

[**OnChainPaymentMethodData**](OnChainPaymentMethodData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated specified payment method |  -  |
**400** | A list of errors that occurred when updating the store payment method |  -  |
**403** | If you are authenticated but forbidden to update the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

