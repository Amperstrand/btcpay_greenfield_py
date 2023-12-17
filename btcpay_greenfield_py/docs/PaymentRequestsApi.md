# btcpay_greenfield_py.PaymentRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_requests_archive_payment_request**](PaymentRequestsApi.md#payment_requests_archive_payment_request) | **DELETE** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId} | Archive payment request
[**payment_requests_create_payment_request**](PaymentRequestsApi.md#payment_requests_create_payment_request) | **POST** /api/v1/stores/{storeId}/payment-requests | Create a new payment request
[**payment_requests_get_payment_request**](PaymentRequestsApi.md#payment_requests_get_payment_request) | **GET** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId} | Get payment request
[**payment_requests_get_payment_requests**](PaymentRequestsApi.md#payment_requests_get_payment_requests) | **GET** /api/v1/stores/{storeId}/payment-requests | Get payment requests
[**payment_requests_pay**](PaymentRequestsApi.md#payment_requests_pay) | **POST** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId}/pay | Create a new invoice for the payment request
[**payment_requests_update_payment_request**](PaymentRequestsApi.md#payment_requests_update_payment_request) | **PUT** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId} | Update payment request


# **payment_requests_archive_payment_request**
> payment_requests_archive_payment_request(payment_request_id, store_id)

Archive payment request

Archives the specified payment request.

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
    api_instance = btcpay_greenfield_py.PaymentRequestsApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | The payment request to remove
    store_id = 'store_id_example' # str | The store the payment request belongs to

    try:
        # Archive payment request
        api_instance.payment_requests_archive_payment_request(payment_request_id, store_id)
    except Exception as e:
        print("Exception when calling PaymentRequestsApi->payment_requests_archive_payment_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| The payment request to remove | 
 **store_id** | **str**| The store the payment request belongs to | 

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
**200** | The payment request has been archived |  -  |
**400** | A list of errors that occurred when archiving the payment request |  -  |
**403** | If you are authenticated but forbidden to archive the specified payment request |  -  |
**404** | The key is not found for this payment request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_create_payment_request**
> PaymentRequestData payment_requests_create_payment_request(store_id, payment_request_base_data)

Create a new payment request

Create a new payment request

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.payment_request_base_data import PaymentRequestBaseData
from btcpay_greenfield_py.models.payment_request_data import PaymentRequestData
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
    api_instance = btcpay_greenfield_py.PaymentRequestsApi(api_client)
    store_id = 'store_id_example' # str | The store to query
    payment_request_base_data = btcpay_greenfield_py.PaymentRequestBaseData() # PaymentRequestBaseData | 

    try:
        # Create a new payment request
        api_response = api_instance.payment_requests_create_payment_request(store_id, payment_request_base_data)
        print("The response of PaymentRequestsApi->payment_requests_create_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestsApi->payment_requests_create_payment_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 
 **payment_request_base_data** | [**PaymentRequestBaseData**](PaymentRequestBaseData.md)|  | 

### Return type

[**PaymentRequestData**](PaymentRequestData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the new payment request |  -  |
**400** | A list of errors that occurred when creating the payment request |  -  |
**403** | If you are authenticated but forbidden to add new payment requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_get_payment_request**
> PaymentRequestData payment_requests_get_payment_request(payment_request_id, store_id)

Get payment request

View information about the specified payment request

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.payment_request_data import PaymentRequestData
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
    api_instance = btcpay_greenfield_py.PaymentRequestsApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | The payment request to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get payment request
        api_response = api_instance.payment_requests_get_payment_request(payment_request_id, store_id)
        print("The response of PaymentRequestsApi->payment_requests_get_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestsApi->payment_requests_get_payment_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| The payment request to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**PaymentRequestData**](PaymentRequestData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified payment request |  -  |
**403** | If you are authenticated but forbidden to view the specified payment request |  -  |
**404** | The key is not found for this payment request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_get_payment_requests**
> List[PaymentRequestData] payment_requests_get_payment_requests(store_id)

Get payment requests

View information about the existing payment requests

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.payment_request_data import PaymentRequestData
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
    api_instance = btcpay_greenfield_py.PaymentRequestsApi(api_client)
    store_id = 'store_id_example' # str | The store to query

    try:
        # Get payment requests
        api_response = api_instance.payment_requests_get_payment_requests(store_id)
        print("The response of PaymentRequestsApi->payment_requests_get_payment_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestsApi->payment_requests_get_payment_requests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 

### Return type

[**List[PaymentRequestData]**](PaymentRequestData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of payment requests |  -  |
**401** | Missing authorization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_pay**
> InvoiceData payment_requests_pay(payment_request_id, store_id, payment_requests_pay_request=payment_requests_pay_request)

Create a new invoice for the payment request

Create a new invoice for the payment request, or reuse an existing one

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.invoice_data import InvoiceData
from btcpay_greenfield_py.models.payment_requests_pay_request import PaymentRequestsPayRequest
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
    api_instance = btcpay_greenfield_py.PaymentRequestsApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | The payment request to create
    store_id = 'store_id_example' # str | The store to fetch
    payment_requests_pay_request = btcpay_greenfield_py.PaymentRequestsPayRequest() # PaymentRequestsPayRequest | Invoice creation request (optional)

    try:
        # Create a new invoice for the payment request
        api_response = api_instance.payment_requests_pay(payment_request_id, store_id, payment_requests_pay_request=payment_requests_pay_request)
        print("The response of PaymentRequestsApi->payment_requests_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestsApi->payment_requests_pay: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| The payment request to create | 
 **store_id** | **str**| The store to fetch | 
 **payment_requests_pay_request** | [**PaymentRequestsPayRequest**](PaymentRequestsPayRequest.md)| Invoice creation request | [optional] 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new invoice |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;archived&#x60;, &#x60;already-paid&#x60;, &#x60;expired&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_update_payment_request**
> PaymentRequestData payment_requests_update_payment_request(payment_request_id, store_id, payment_request_base_data)

Update payment request

Update a payment request

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.payment_request_base_data import PaymentRequestBaseData
from btcpay_greenfield_py.models.payment_request_data import PaymentRequestData
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
    api_instance = btcpay_greenfield_py.PaymentRequestsApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | The payment request to update
    store_id = 'store_id_example' # str | The store to query
    payment_request_base_data = btcpay_greenfield_py.PaymentRequestBaseData() # PaymentRequestBaseData | 

    try:
        # Update payment request
        api_response = api_instance.payment_requests_update_payment_request(payment_request_id, store_id, payment_request_base_data)
        print("The response of PaymentRequestsApi->payment_requests_update_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRequestsApi->payment_requests_update_payment_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| The payment request to update | 
 **store_id** | **str**| The store to query | 
 **payment_request_base_data** | [**PaymentRequestBaseData**](PaymentRequestBaseData.md)|  | 

### Return type

[**PaymentRequestData**](PaymentRequestData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated payment request |  -  |
**400** | A list of errors that occurred when updating the payment request |  -  |
**403** | If you are authenticated but forbidden to update the payment request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

