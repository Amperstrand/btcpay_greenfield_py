# openapi_client.StoresPayoutsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_store_payout**](StoresPayoutsApi.md#get_store_payout) | **GET** /api/v1/stores/{storeId}/payouts/{payoutId} | Get Payout
[**payouts_create_payout_through_store**](StoresPayoutsApi.md#payouts_create_payout_through_store) | **POST** /api/v1/stores/{storeId}/payouts | Create Payout
[**pull_payments_approve_payout**](StoresPayoutsApi.md#pull_payments_approve_payout) | **POST** /api/v1/stores/{storeId}/payouts/{payoutId} | Approve Payout
[**pull_payments_cancel_payout**](StoresPayoutsApi.md#pull_payments_cancel_payout) | **DELETE** /api/v1/stores/{storeId}/payouts/{payoutId} | Cancel Payout
[**pull_payments_get_store_payouts**](StoresPayoutsApi.md#pull_payments_get_store_payouts) | **GET** /api/v1/stores/{storeId}/payouts | Get Store Payouts
[**pull_payments_mark_payout**](StoresPayoutsApi.md#pull_payments_mark_payout) | **POST** /api/v1/stores/{storeId}/payouts/{payoutId}/mark | Mark Payout
[**pull_payments_mark_payout_paid**](StoresPayoutsApi.md#pull_payments_mark_payout_paid) | **POST** /api/v1/stores/{storeId}/payouts/{payoutId}/mark-paid | Mark Payout as Paid


# **get_store_payout**
> PayoutData get_store_payout(payout_id, store_id)

Get Payout

Get payout

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.payout_data import PayoutData
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
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    payout_id = 'payout_id_example' # str | The ID of the payout
    store_id = 'store_id_example' # str | The ID of the store

    try:
        # Get Payout
        api_response = api_instance.get_store_payout(payout_id, store_id)
        print("The response of StoresPayoutsApi->get_store_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->get_store_payout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The ID of the payout | 
 **store_id** | **str**| The ID of the store | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific payout of a store |  -  |
**404** | Payout not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_create_payout_through_store**
> PayoutData payouts_create_payout_through_store(store_id, create_payout_through_store_request)

Create Payout

Create a new payout

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_payout_through_store_request import CreatePayoutThroughStoreRequest
from openapi_client.models.payout_data import PayoutData
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
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    store_id = 'store_id_example' # str | The ID of the store
    create_payout_through_store_request = openapi_client.CreatePayoutThroughStoreRequest() # CreatePayoutThroughStoreRequest | 

    try:
        # Create Payout
        api_response = api_instance.payouts_create_payout_through_store(store_id, create_payout_through_store_request)
        print("The response of StoresPayoutsApi->payouts_create_payout_through_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->payouts_create_payout_through_store: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **create_payout_through_store_request** | [**CreatePayoutThroughStoreRequest**](CreatePayoutThroughStoreRequest.md)|  | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new payout has been created |  -  |
**404** | store not found |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;duplicate-destination&#x60;, &#x60;expired&#x60;, &#x60;not-started&#x60;, &#x60;archived&#x60;, &#x60;overdraft&#x60;, &#x60;amount-too-low&#x60;, &#x60;payment-method-not-supported&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_approve_payout**
> PayoutData pull_payments_approve_payout(payout_id, store_id, pull_payments_approve_payout_request=pull_payments_approve_payout_request)

Approve Payout

Approve a payout

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.payout_data import PayoutData
from openapi_client.models.pull_payments_approve_payout_request import PullPaymentsApprovePayoutRequest
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
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    payout_id = 'payout_id_example' # str | The ID of the payout
    store_id = 'store_id_example' # str | The ID of the store
    pull_payments_approve_payout_request = openapi_client.PullPaymentsApprovePayoutRequest() # PullPaymentsApprovePayoutRequest |  (optional)

    try:
        # Approve Payout
        api_response = api_instance.pull_payments_approve_payout(payout_id, store_id, pull_payments_approve_payout_request=pull_payments_approve_payout_request)
        print("The response of StoresPayoutsApi->pull_payments_approve_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->pull_payments_approve_payout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The ID of the payout | 
 **store_id** | **str**| The ID of the store | 
 **pull_payments_approve_payout_request** | [**PullPaymentsApprovePayoutRequest**](PullPaymentsApprovePayoutRequest.md)|  | [optional] 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payout has been approved, transitioning to &#x60;AwaitingPayment&#x60; state. |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;rate-unavailable&#x60;, &#x60;invalid-state&#x60;, &#x60;amount-too-low&#x60;, &#x60;old-revision&#x60; |  -  |
**404** | The payout is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_cancel_payout**
> pull_payments_cancel_payout(payout_id, store_id)

Cancel Payout

Cancel the payout

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
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    payout_id = 'payout_id_example' # str | The ID of the payout
    store_id = 'store_id_example' # str | The ID of the store

    try:
        # Cancel Payout
        api_instance.pull_payments_cancel_payout(payout_id, store_id)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->pull_payments_cancel_payout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The ID of the payout | 
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
**200** | The payout has been cancelled |  -  |
**404** | The payout is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_store_payouts**
> List[PayoutData] pull_payments_get_store_payouts(store_id, include_cancelled=include_cancelled)

Get Store Payouts

Get payouts

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.payout_data import PayoutData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    store_id = 'store_id_example' # str | The ID of the store
    include_cancelled = False # bool | Whether this should list cancelled payouts (optional) (default to False)

    try:
        # Get Store Payouts
        api_response = api_instance.pull_payments_get_store_payouts(store_id, include_cancelled=include_cancelled)
        print("The response of StoresPayoutsApi->pull_payments_get_store_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->pull_payments_get_store_payouts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **include_cancelled** | **bool**| Whether this should list cancelled payouts | [optional] [default to False]

### Return type

[**List[PayoutData]**](PayoutData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payouts of the store |  -  |
**404** | Pull payment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_mark_payout**
> pull_payments_mark_payout(payout_id, store_id, pull_payments_mark_payout_request=pull_payments_mark_payout_request)

Mark Payout

Mark a payout with a state

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.pull_payments_mark_payout_request import PullPaymentsMarkPayoutRequest
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
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    payout_id = 'payout_id_example' # str | The ID of the payout
    store_id = 'store_id_example' # str | The ID of the store
    pull_payments_mark_payout_request = openapi_client.PullPaymentsMarkPayoutRequest() # PullPaymentsMarkPayoutRequest |  (optional)

    try:
        # Mark Payout
        api_instance.pull_payments_mark_payout(payout_id, store_id, pull_payments_mark_payout_request=pull_payments_mark_payout_request)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->pull_payments_mark_payout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The ID of the payout | 
 **store_id** | **str**| The ID of the store | 
 **pull_payments_mark_payout_request** | [**PullPaymentsMarkPayoutRequest**](PullPaymentsMarkPayoutRequest.md)|  | [optional] 

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
**200** | The payout has been set to the specified state |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;invalid-state&#x60; |  -  |
**404** | The payout is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_mark_payout_paid**
> pull_payments_mark_payout_paid(payout_id, store_id)

Mark Payout as Paid

Mark a payout as paid

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
    api_instance = openapi_client.StoresPayoutsApi(api_client)
    payout_id = 'payout_id_example' # str | The ID of the payout
    store_id = 'store_id_example' # str | The ID of the store

    try:
        # Mark Payout as Paid
        api_instance.pull_payments_mark_payout_paid(payout_id, store_id)
    except Exception as e:
        print("Exception when calling StoresPayoutsApi->pull_payments_mark_payout_paid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The ID of the payout | 
 **store_id** | **str**| The ID of the store | 

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
**200** | The payout has been marked paid, transitioning to &#x60;Completed&#x60; state. |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;invalid-state&#x60; |  -  |
**404** | The payout is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

