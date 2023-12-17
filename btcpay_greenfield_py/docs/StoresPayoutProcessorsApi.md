# btcpay_greenfield_py.StoresPayoutProcessorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method**](StoresPayoutProcessorsApi.md#greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method) | **GET** /api/v1/stores/{storeId}/payout-processors/LightningAutomatedPayoutSenderFactory/{paymentMethod} | Get configured store Lightning automated payout processors
[**greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory**](StoresPayoutProcessorsApi.md#greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory) | **GET** /api/v1/stores/{storeId}/payout-processors/LightningAutomatedPayoutSenderFactory | Get configured store Lightning automated payout processors
[**greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor**](StoresPayoutProcessorsApi.md#greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor) | **PUT** /api/v1/stores/{storeId}/payout-processors/LightningAutomatedPayoutSenderFactory/{paymentMethod} | Update configured store Lightning automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method) | **GET** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedPayoutSenderFactory/{paymentMethod} | Get configured store onchain automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory) | **GET** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedTransferSenderFactory | Get configured store onchain automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method) | **PUT** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedPayoutSenderFactory/{paymentMethod} | Update configured store onchain automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory) | **PUT** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedTransferSenderFactory | Update configured store onchain automated payout processors
[**store_payout_processors_get_store_payout_processors**](StoresPayoutProcessorsApi.md#store_payout_processors_get_store_payout_processors) | **GET** /api/v1/stores/{storeId}/payout-processors | Get store configured payout processors
[**store_payout_processors_remove_store_payout_processor**](StoresPayoutProcessorsApi.md#store_payout_processors_remove_store_payout_processor) | **DELETE** /api/v1/stores/{storeId}/payout-processors/{processor}/{paymentMethod} | Remove store configured payout processor


# **greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method**
> List[LightningAutomatedTransferSettings] greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method(payment_method, store_id)

Get configured store Lightning automated payout processors

Get configured store Lightning automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_automated_transfer_settings import LightningAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    payment_method = 'payment_method_example' # str | A specific payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get configured store Lightning automated payout processors
        api_response = api_instance.greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method(payment_method, store_id)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_for_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | **str**| A specific payment method to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[LightningAutomatedTransferSettings]**](LightningAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processors |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory**
> List[LightningAutomatedTransferSettings] greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory(store_id)

Get configured store Lightning automated payout processors

Get configured store Lightning automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_automated_transfer_settings import LightningAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get configured store Lightning automated payout processors
        api_response = api_instance.greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory(store_id)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_sender_factory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[LightningAutomatedTransferSettings]**](LightningAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processors |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor**
> LightningAutomatedTransferSettings greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor(payment_method, store_id, update_lightning_automated_transfer_settings)

Update configured store Lightning automated payout processors

Update configured store Lightning automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_automated_transfer_settings import LightningAutomatedTransferSettings
from btcpay_greenfield_py.models.update_lightning_automated_transfer_settings import UpdateLightningAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    payment_method = 'payment_method_example' # str | A specific payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    update_lightning_automated_transfer_settings = btcpay_greenfield_py.UpdateLightningAutomatedTransferSettings() # UpdateLightningAutomatedTransferSettings | 

    try:
        # Update configured store Lightning automated payout processors
        api_response = api_instance.greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor(payment_method, store_id, update_lightning_automated_transfer_settings)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | **str**| A specific payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **update_lightning_automated_transfer_settings** | [**UpdateLightningAutomatedTransferSettings**](UpdateLightningAutomatedTransferSettings.md)|  | 

### Return type

[**LightningAutomatedTransferSettings**](LightningAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processor |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method**
> List[OnChainAutomatedTransferSettings] greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method(payment_method, store_id)

Get configured store onchain automated payout processors

Get configured store onchain automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.on_chain_automated_transfer_settings import OnChainAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    payment_method = 'payment_method_example' # str | A specific payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get configured store onchain automated payout processors
        api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method(payment_method, store_id)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_for_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | **str**| A specific payment method to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[OnChainAutomatedTransferSettings]**](OnChainAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processors |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory**
> List[OnChainAutomatedTransferSettings] greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory(store_id)

Get configured store onchain automated payout processors

Get configured store onchain automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.on_chain_automated_transfer_settings import OnChainAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get configured store onchain automated payout processors
        api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory(store_id)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_transfer_sender_factory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[OnChainAutomatedTransferSettings]**](OnChainAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processors |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method**
> OnChainAutomatedTransferSettings greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method(payment_method, store_id, update_on_chain_automated_transfer_settings)

Update configured store onchain automated payout processors

Update configured store onchain automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.on_chain_automated_transfer_settings import OnChainAutomatedTransferSettings
from btcpay_greenfield_py.models.update_on_chain_automated_transfer_settings import UpdateOnChainAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    payment_method = 'payment_method_example' # str | A specific payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    update_on_chain_automated_transfer_settings = btcpay_greenfield_py.UpdateOnChainAutomatedTransferSettings() # UpdateOnChainAutomatedTransferSettings | 

    try:
        # Update configured store onchain automated payout processors
        api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method(payment_method, store_id, update_on_chain_automated_transfer_settings)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_for_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | **str**| A specific payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **update_on_chain_automated_transfer_settings** | [**UpdateOnChainAutomatedTransferSettings**](UpdateOnChainAutomatedTransferSettings.md)|  | 

### Return type

[**OnChainAutomatedTransferSettings**](OnChainAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processor |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory**
> OnChainAutomatedTransferSettings greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory(store_id, update_on_chain_automated_transfer_settings)

Update configured store onchain automated payout processors

Update configured store onchain automated payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.on_chain_automated_transfer_settings import OnChainAutomatedTransferSettings
from btcpay_greenfield_py.models.update_on_chain_automated_transfer_settings import UpdateOnChainAutomatedTransferSettings
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    update_on_chain_automated_transfer_settings = btcpay_greenfield_py.UpdateOnChainAutomatedTransferSettings() # UpdateOnChainAutomatedTransferSettings | 

    try:
        # Update configured store onchain automated payout processors
        api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory(store_id, update_on_chain_automated_transfer_settings)
        print("The response of StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_transfer_sender_factory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **update_on_chain_automated_transfer_settings** | [**UpdateOnChainAutomatedTransferSettings**](UpdateOnChainAutomatedTransferSettings.md)|  | 

### Return type

[**OnChainAutomatedTransferSettings**](OnChainAutomatedTransferSettings.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured processor |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_payout_processors_get_store_payout_processors**
> List[PayoutProcessorData] store_payout_processors_get_store_payout_processors(store_id)

Get store configured payout processors

Get store configured payout processors

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.payout_processor_data import PayoutProcessorData
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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store configured payout processors
        api_response = api_instance.store_payout_processors_get_store_payout_processors(store_id)
        print("The response of StoresPayoutProcessorsApi->store_payout_processors_get_store_payout_processors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->store_payout_processors_get_store_payout_processors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[PayoutProcessorData]**](PayoutProcessorData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configured payout processors |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_payout_processors_remove_store_payout_processor**
> store_payout_processors_remove_store_payout_processor(payment_method, processor, store_id)

Remove store configured payout processor

Remove store configured payout processor

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
    api_instance = btcpay_greenfield_py.StoresPayoutProcessorsApi(api_client)
    payment_method = 'payment_method_example' # str | The payment method
    processor = 'processor_example' # str | The processor
    store_id = 'store_id_example' # str | The store

    try:
        # Remove store configured payout processor
        api_instance.store_payout_processors_remove_store_payout_processor(payment_method, processor, store_id)
    except Exception as e:
        print("Exception when calling StoresPayoutProcessorsApi->store_payout_processors_remove_store_payout_processor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | **str**| The payment method | 
 **processor** | **str**| The processor | 
 **store_id** | **str**| The store | 

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
**200** | removed |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

