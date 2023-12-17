# openapi_client.PullPaymentsManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pull_payments_archive_pull_payment**](PullPaymentsManagementApi.md#pull_payments_archive_pull_payment) | **DELETE** /api/v1/stores/{storeId}/pull-payments/{pullPaymentId} | Archive a pull payment
[**pull_payments_create_pull_payment**](PullPaymentsManagementApi.md#pull_payments_create_pull_payment) | **POST** /api/v1/stores/{storeId}/pull-payments | Create a new pull payment
[**pull_payments_get_pull_payments**](PullPaymentsManagementApi.md#pull_payments_get_pull_payments) | **GET** /api/v1/stores/{storeId}/pull-payments | Get store&#39;s pull payments


# **pull_payments_archive_pull_payment**
> pull_payments_archive_pull_payment(pull_payment_id, store_id)

Archive a pull payment

Archive this pull payment (Will cancel all payouts awaiting for payment)

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
    api_instance = openapi_client.PullPaymentsManagementApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
    store_id = 'store_id_example' # str | The ID of the store

    try:
        # Archive a pull payment
        api_instance.pull_payments_archive_pull_payment(pull_payment_id, store_id)
    except Exception as e:
        print("Exception when calling PullPaymentsManagementApi->pull_payments_archive_pull_payment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 
 **store_id** | **str**| The ID of the store | 

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
**200** | The pull payment has been archived |  -  |
**404** | The pull payment has not been found, or does not belong to this store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_create_pull_payment**
> PullPaymentData pull_payments_create_pull_payment(store_id, pull_payments_create_pull_payment_request=pull_payments_create_pull_payment_request)

Create a new pull payment

A pull payment allows its receiver to ask for payouts up to `amount` of `currency` every `period`.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.pull_payment_data import PullPaymentData
from openapi_client.models.pull_payments_create_pull_payment_request import PullPaymentsCreatePullPaymentRequest
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
    api_instance = openapi_client.PullPaymentsManagementApi(api_client)
    store_id = 'store_id_example' # str | The store ID
    pull_payments_create_pull_payment_request = openapi_client.PullPaymentsCreatePullPaymentRequest() # PullPaymentsCreatePullPaymentRequest |  (optional)

    try:
        # Create a new pull payment
        api_response = api_instance.pull_payments_create_pull_payment(store_id, pull_payments_create_pull_payment_request=pull_payments_create_pull_payment_request)
        print("The response of PullPaymentsManagementApi->pull_payments_create_pull_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsManagementApi->pull_payments_create_pull_payment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **pull_payments_create_pull_payment_request** | [**PullPaymentsCreatePullPaymentRequest**](PullPaymentsCreatePullPaymentRequest.md)|  | [optional] 

### Return type

[**PullPaymentData**](PullPaymentData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The create pull payment |  -  |
**422** | Unable to validate the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_pull_payments**
> List[PullPaymentData] pull_payments_get_pull_payments(store_id, include_archived=include_archived)

Get store's pull payments

Get the pull payments of a store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.pull_payment_data import PullPaymentData
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
    api_instance = openapi_client.PullPaymentsManagementApi(api_client)
    store_id = 'store_id_example' # str | The store ID
    include_archived = False # bool | Whether this should list archived pull payments (optional) (default to False)

    try:
        # Get store's pull payments
        api_response = api_instance.pull_payments_get_pull_payments(store_id, include_archived=include_archived)
        print("The response of PullPaymentsManagementApi->pull_payments_get_pull_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsManagementApi->pull_payments_get_pull_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **include_archived** | **bool**| Whether this should list archived pull payments | [optional] [default to False]

### Return type

[**List[PullPaymentData]**](PullPaymentData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pull payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

