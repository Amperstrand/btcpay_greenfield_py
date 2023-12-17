# openapi_client.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_activate_payment_method**](InvoicesApi.md#invoices_activate_payment_method) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/payment-methods/{paymentMethod}/activate | Activate Payment Method
[**invoices_archive_invoice**](InvoicesApi.md#invoices_archive_invoice) | **DELETE** /api/v1/stores/{storeId}/invoices/{invoiceId} | Archive invoice
[**invoices_create_invoice**](InvoicesApi.md#invoices_create_invoice) | **POST** /api/v1/stores/{storeId}/invoices | Create a new invoice
[**invoices_get_invoice**](InvoicesApi.md#invoices_get_invoice) | **GET** /api/v1/stores/{storeId}/invoices/{invoiceId} | Get invoice
[**invoices_get_invoice_payment_methods**](InvoicesApi.md#invoices_get_invoice_payment_methods) | **GET** /api/v1/stores/{storeId}/invoices/{invoiceId}/payment-methods | Get invoice payment methods
[**invoices_get_invoices**](InvoicesApi.md#invoices_get_invoices) | **GET** /api/v1/stores/{storeId}/invoices | Get invoices
[**invoices_mark_invoice_status**](InvoicesApi.md#invoices_mark_invoice_status) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/status | Mark invoice status
[**invoices_refund**](InvoicesApi.md#invoices_refund) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/refund | Refund invoice
[**invoices_unarchive_invoice**](InvoicesApi.md#invoices_unarchive_invoice) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/unarchive | Unarchive invoice
[**invoices_update_invoice**](InvoicesApi.md#invoices_update_invoice) | **PUT** /api/v1/stores/{storeId}/invoices/{invoiceId} | Update invoice


# **invoices_activate_payment_method**
> invoices_activate_payment_method(invoice_id, payment_method, store_id)

Activate Payment Method

Activate an invoice payment method (if lazy payments mode is enabled)

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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to update
    payment_method = 'payment_method_example' # str | The payment method to activate
    store_id = 'store_id_example' # str | The store to query

    try:
        # Activate Payment Method
        api_instance.invoices_activate_payment_method(invoice_id, payment_method, store_id)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_activate_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to update | 
 **payment_method** | **str**| The payment method to activate | 
 **store_id** | **str**| The store to query | 

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
**200** |  |  -  |
**400** | A list of errors that occurred when updating the invoice |  -  |
**403** | If you are authenticated but forbidden to activate the invoice payment method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_archive_invoice**
> invoices_archive_invoice(invoice_id, store_id)

Archive invoice

Archives the specified invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to remove
    store_id = 'store_id_example' # str | The store the invoice belongs to

    try:
        # Archive invoice
        api_instance.invoices_archive_invoice(invoice_id, store_id)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_archive_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to remove | 
 **store_id** | **str**| The store the invoice belongs to | 

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
**200** | The invoice has been archived |  -  |
**400** | A list of errors that occurred when archiving the invoice |  -  |
**403** | If you are authenticated but forbidden to archive the specified invoice |  -  |
**404** | The key is not found for this invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_create_invoice**
> InvoiceData invoices_create_invoice(store_id, create_invoice_request)

Create a new invoice

Create a new invoice

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_invoice_request import CreateInvoiceRequest
from openapi_client.models.invoice_data import InvoiceData
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
    api_instance = openapi_client.InvoicesApi(api_client)
    store_id = 'store_id_example' # str | The store to query
    create_invoice_request = openapi_client.CreateInvoiceRequest() # CreateInvoiceRequest | 

    try:
        # Create a new invoice
        api_response = api_instance.invoices_create_invoice(store_id, create_invoice_request)
        print("The response of InvoicesApi->invoices_create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_create_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 
 **create_invoice_request** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)|  | 

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
**200** | Information about the new invoice |  -  |
**400** | A list of errors that occurred when creating the invoice |  -  |
**403** | If you are authenticated but forbidden to add new invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice**
> InvoiceData invoices_get_invoice(invoice_id, store_id)

Get invoice

View information about the specified invoice

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoice_data import InvoiceData
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get invoice
        api_response = api_instance.invoices_get_invoice(invoice_id, store_id)
        print("The response of InvoicesApi->invoices_get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified invoice |  -  |
**403** | If you are authenticated but forbidden to view the specified invoice |  -  |
**404** | The key is not found for this invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice_payment_methods**
> List[InvoicePaymentMethodDataModel] invoices_get_invoice_payment_methods(invoice_id, store_id, only_accounted_payments=only_accounted_payments)

Get invoice payment methods

View information about the specified invoice's payment methods

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoice_payment_method_data_model import InvoicePaymentMethodDataModel
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to fetch
    store_id = 'store_id_example' # str | The store to fetch
    only_accounted_payments = True # bool | If default or true, only returns payments which are accounted (in Bitcoin, this mean not returning RBF'd or double spent payments) (optional) (default to True)

    try:
        # Get invoice payment methods
        api_response = api_instance.invoices_get_invoice_payment_methods(invoice_id, store_id, only_accounted_payments=only_accounted_payments)
        print("The response of InvoicesApi->invoices_get_invoice_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice_payment_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to fetch | 
 **store_id** | **str**| The store to fetch | 
 **only_accounted_payments** | **bool**| If default or true, only returns payments which are accounted (in Bitcoin, this mean not returning RBF&#39;d or double spent payments) | [optional] [default to True]

### Return type

[**List[InvoicePaymentMethodDataModel]**](InvoicePaymentMethodDataModel.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified invoice payment methods data |  -  |
**403** | If you are authenticated but forbidden to view the specified invoice |  -  |
**404** | The key is not found for this invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoices**
> List[InvoiceData] invoices_get_invoices(store_id, order_id=order_id, text_search=text_search, status=status, end_date=end_date, take=take, skip=skip, start_date=start_date)

Get invoices

View information about the existing invoices

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoice_data import InvoiceData
from openapi_client.models.invoice_status import InvoiceStatus
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
    api_instance = openapi_client.InvoicesApi(api_client)
    store_id = 'store_id_example' # str | The store to query
    order_id = ['1000&orderId=1001&orderId=1002'] # List[str] | Array of OrderIds to fetch the invoices for (optional)
    text_search = 'text_search_example' # str | A term that can help locating specific invoices. (optional)
    status = openapi_client.InvoiceStatus() # InvoiceStatus | Array of statuses of invoices to be fetched (optional)
    end_date = 3.4 # float | End date of the period to retrieve invoices (optional)
    take = 3.4 # float | Number of records returned in response (optional)
    skip = 3.4 # float | Number of records to skip (optional)
    start_date = 3.4 # float | Start date of the period to retrieve invoices (optional)

    try:
        # Get invoices
        api_response = api_instance.invoices_get_invoices(store_id, order_id=order_id, text_search=text_search, status=status, end_date=end_date, take=take, skip=skip, start_date=start_date)
        print("The response of InvoicesApi->invoices_get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 
 **order_id** | [**List[str]**](str.md)| Array of OrderIds to fetch the invoices for | [optional] 
 **text_search** | **str**| A term that can help locating specific invoices. | [optional] 
 **status** | [**InvoiceStatus**](.md)| Array of statuses of invoices to be fetched | [optional] 
 **end_date** | **float**| End date of the period to retrieve invoices | [optional] 
 **take** | **float**| Number of records returned in response | [optional] 
 **skip** | **float**| Number of records to skip | [optional] 
 **start_date** | **float**| Start date of the period to retrieve invoices | [optional] 

### Return type

[**List[InvoiceData]**](InvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of invoices |  -  |
**401** | Missing authorization |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_mark_invoice_status**
> InvoiceData invoices_mark_invoice_status(invoice_id, store_id, mark_invoice_status_request)

Mark invoice status

Mark an invoice as invalid or settled.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoice_data import InvoiceData
from openapi_client.models.mark_invoice_status_request import MarkInvoiceStatusRequest
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to update
    store_id = 'store_id_example' # str | The store to query
    mark_invoice_status_request = openapi_client.MarkInvoiceStatusRequest() # MarkInvoiceStatusRequest | 

    try:
        # Mark invoice status
        api_response = api_instance.invoices_mark_invoice_status(invoice_id, store_id, mark_invoice_status_request)
        print("The response of InvoicesApi->invoices_mark_invoice_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_mark_invoice_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to update | 
 **store_id** | **str**| The store to query | 
 **mark_invoice_status_request** | [**MarkInvoiceStatusRequest**](MarkInvoiceStatusRequest.md)|  | 

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
**200** | The updated invoice |  -  |
**400** | A list of errors that occurred when updating the invoice |  -  |
**403** | If you are authenticated but forbidden to update the invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_refund**
> PullPaymentData invoices_refund(invoice_id, store_id, invoices_refund_request)

Refund invoice

Refund invoice

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoices_refund_request import InvoicesRefundRequest
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to refund
    store_id = 'store_id_example' # str | The store to query
    invoices_refund_request = openapi_client.InvoicesRefundRequest() # InvoicesRefundRequest | 

    try:
        # Refund invoice
        api_response = api_instance.invoices_refund(invoice_id, store_id, invoices_refund_request)
        print("The response of InvoicesApi->invoices_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_refund: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to refund | 
 **store_id** | **str**| The store to query | 
 **invoices_refund_request** | [**InvoicesRefundRequest**](InvoicesRefundRequest.md)|  | 

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
**200** | Pull payment for refunding the invoice |  -  |
**400** | A list of errors that occurred when refunding the invoice |  -  |
**403** | If you are authenticated but forbidden to refund the invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_unarchive_invoice**
> InvoiceData invoices_unarchive_invoice(invoice_id, store_id)

Unarchive invoice

Unarchive an invoice

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoice_data import InvoiceData
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to update
    store_id = 'store_id_example' # str | The store to query

    try:
        # Unarchive invoice
        api_response = api_instance.invoices_unarchive_invoice(invoice_id, store_id)
        print("The response of InvoicesApi->invoices_unarchive_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_unarchive_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to update | 
 **store_id** | **str**| The store to query | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unarchived invoice |  -  |
**400** | A list of errors that occurred when updating the invoice |  -  |
**403** | If you are authenticated but forbidden to update the invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_update_invoice**
> InvoiceData invoices_update_invoice(invoice_id, store_id, update_invoice_request)

Update invoice

Updates the specified invoice.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.invoice_data import InvoiceData
from openapi_client.models.update_invoice_request import UpdateInvoiceRequest
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice to update
    store_id = 'store_id_example' # str | The store the invoice belongs to
    update_invoice_request = openapi_client.UpdateInvoiceRequest() # UpdateInvoiceRequest | 

    try:
        # Update invoice
        api_response = api_instance.invoices_update_invoice(invoice_id, store_id, update_invoice_request)
        print("The response of InvoicesApi->invoices_update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_update_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice to update | 
 **store_id** | **str**| The store the invoice belongs to | 
 **update_invoice_request** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)|  | 

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
**200** | The invoice that has been updated |  -  |
**400** | A list of errors that occurred when updating the invoice |  -  |
**403** | If you are authenticated but forbidden to update the specified invoice |  -  |
**404** | The key is not found for this invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

