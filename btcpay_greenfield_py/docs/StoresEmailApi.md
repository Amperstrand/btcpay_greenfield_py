# btcpay_greenfield_py.StoresEmailApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stores_get_store_email_settings**](StoresEmailApi.md#stores_get_store_email_settings) | **GET** /api/v1/stores/{storeId}/email | Get store email settings
[**stores_send_store_email**](StoresEmailApi.md#stores_send_store_email) | **POST** /api/v1/stores/{storeId}/email/send | Send an email for a store
[**stores_update_store_email_settings**](StoresEmailApi.md#stores_update_store_email_settings) | **PUT** /api/v1/stores/{storeId}/email | Update store email settings


# **stores_get_store_email_settings**
> EmailSettingsData stores_get_store_email_settings(store_id)

Get store email settings

View email settings of the specified store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.email_settings_data import EmailSettingsData
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
    api_instance = btcpay_greenfield_py.StoresEmailApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store email settings
        api_response = api_instance.stores_get_store_email_settings(store_id)
        print("The response of StoresEmailApi->stores_get_store_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresEmailApi->stores_get_store_email_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**EmailSettingsData**](EmailSettingsData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified store email settings |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_send_store_email**
> stores_send_store_email(store_id, email_data)

Send an email for a store

Send an email using the store's SMTP server

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.email_data import EmailData
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
    api_instance = btcpay_greenfield_py.StoresEmailApi(api_client)
    store_id = 'store_id_example' # str | The store to send the email from
    email_data = btcpay_greenfield_py.EmailData() # EmailData | 

    try:
        # Send an email for a store
        api_instance.stores_send_store_email(store_id, email_data)
    except Exception as e:
        print("Exception when calling StoresEmailApi->stores_send_store_email: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to send the email from | 
 **email_data** | [**EmailData**](EmailData.md)|  | 

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
**200** | The email was sent (scheduled) successfully |  -  |
**400** | The store&#39;s SMTP is not configured |  -  |
**403** | If you are authenticated but forbidden to add new stores |  -  |
**404** | The store was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_update_store_email_settings**
> EmailSettingsData stores_update_store_email_settings(store_id, email_settings_data)

Update store email settings

Update a store's email settings

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.email_settings_data import EmailSettingsData
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
    api_instance = btcpay_greenfield_py.StoresEmailApi(api_client)
    store_id = 'store_id_example' # str | The store to update
    email_settings_data = btcpay_greenfield_py.EmailSettingsData() # EmailSettingsData | 

    try:
        # Update store email settings
        api_response = api_instance.stores_update_store_email_settings(store_id, email_settings_data)
        print("The response of StoresEmailApi->stores_update_store_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresEmailApi->stores_update_store_email_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to update | 
 **email_settings_data** | [**EmailSettingsData**](EmailSettingsData.md)|  | 

### Return type

[**EmailSettingsData**](EmailSettingsData.md)

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

