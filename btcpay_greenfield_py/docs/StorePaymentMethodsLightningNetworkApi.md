# btcpay_greenfield_py.StorePaymentMethodsLightningNetworkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_lightning_network_payment_methods_delete_lightning_network_payment_method**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_delete_lightning_network_payment_method) | **DELETE** /api/v1/stores/{storeId}/payment-methods/LightningNetwork/{cryptoCode} | Remove store Lightning Network payment method
[**store_lightning_network_payment_methods_get_lightning_network_payment_method**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_get_lightning_network_payment_method) | **GET** /api/v1/stores/{storeId}/payment-methods/LightningNetwork/{cryptoCode} | Get store Lightning Network payment method
[**store_lightning_network_payment_methods_get_lightning_network_payment_methods**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_get_lightning_network_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods/LightningNetwork | Get store Lightning Network payment methods
[**store_lightning_network_payment_methods_update_lightning_network_payment_method**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_update_lightning_network_payment_method) | **PUT** /api/v1/stores/{storeId}/payment-methods/LightningNetwork/{cryptoCode} | Update store Lightning Network payment method


# **store_lightning_network_payment_methods_delete_lightning_network_payment_method**
> store_lightning_network_payment_methods_delete_lightning_network_payment_method(crypto_code, store_id)

Remove store Lightning Network payment method

Removes the specified store payment method.

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
    api_instance = btcpay_greenfield_py.StorePaymentMethodsLightningNetworkApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to update
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Remove store Lightning Network payment method
        api_instance.store_lightning_network_payment_methods_delete_lightning_network_payment_method(crypto_code, store_id)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_delete_lightning_network_payment_method: %s\n" % e)
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

# **store_lightning_network_payment_methods_get_lightning_network_payment_method**
> LightningNetworkPaymentMethodData store_lightning_network_payment_methods_get_lightning_network_payment_method(crypto_code, store_id)

Get store Lightning Network payment method

View information about the specified payment method

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_network_payment_method_data import LightningNetworkPaymentMethodData
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
    api_instance = btcpay_greenfield_py.StorePaymentMethodsLightningNetworkApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store Lightning Network payment method
        api_response = api_instance.store_lightning_network_payment_methods_get_lightning_network_payment_method(crypto_code, store_id)
        print("The response of StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_get_lightning_network_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_get_lightning_network_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**LightningNetworkPaymentMethodData**](LightningNetworkPaymentMethodData.md)

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

# **store_lightning_network_payment_methods_get_lightning_network_payment_methods**
> List[LightningNetworkPaymentMethodData] store_lightning_network_payment_methods_get_lightning_network_payment_methods(store_id, enabled=enabled)

Get store Lightning Network payment methods

View information about the stores' configured Lightning Network payment methods

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_network_payment_method_data import LightningNetworkPaymentMethodData
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
    api_instance = btcpay_greenfield_py.StorePaymentMethodsLightningNetworkApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    enabled = True # bool | Fetch payment methods that are enabled/disabled only (optional)

    try:
        # Get store Lightning Network payment methods
        api_response = api_instance.store_lightning_network_payment_methods_get_lightning_network_payment_methods(store_id, enabled=enabled)
        print("The response of StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_get_lightning_network_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_get_lightning_network_payment_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**List[LightningNetworkPaymentMethodData]**](LightningNetworkPaymentMethodData.md)

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

# **store_lightning_network_payment_methods_update_lightning_network_payment_method**
> LightningNetworkPaymentMethodData store_lightning_network_payment_methods_update_lightning_network_payment_method(crypto_code, store_id, update_lightning_network_payment_method_request)

Update store Lightning Network payment method

Update the specified store's payment method

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_network_payment_method_data import LightningNetworkPaymentMethodData
from btcpay_greenfield_py.models.update_lightning_network_payment_method_request import UpdateLightningNetworkPaymentMethodRequest
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
    api_instance = btcpay_greenfield_py.StorePaymentMethodsLightningNetworkApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to update
    store_id = 'store_id_example' # str | The store to fetch
    update_lightning_network_payment_method_request = btcpay_greenfield_py.UpdateLightningNetworkPaymentMethodRequest() # UpdateLightningNetworkPaymentMethodRequest | 

    try:
        # Update store Lightning Network payment method
        api_response = api_instance.store_lightning_network_payment_methods_update_lightning_network_payment_method(crypto_code, store_id, update_lightning_network_payment_method_request)
        print("The response of StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_update_lightning_network_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_update_lightning_network_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to update | 
 **store_id** | **str**| The store to fetch | 
 **update_lightning_network_payment_method_request** | [**UpdateLightningNetworkPaymentMethodRequest**](UpdateLightningNetworkPaymentMethodRequest.md)|  | 

### Return type

[**LightningNetworkPaymentMethodData**](LightningNetworkPaymentMethodData.md)

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

