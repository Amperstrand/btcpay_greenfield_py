# btcpay_greenfield_py.LightningInternalNodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_lightning_node_api_connect_to_node**](LightningInternalNodeApi.md#internal_lightning_node_api_connect_to_node) | **POST** /api/v1/server/lightning/{cryptoCode}/connect | Connect to lightning node
[**internal_lightning_node_api_create_invoice**](LightningInternalNodeApi.md#internal_lightning_node_api_create_invoice) | **POST** /api/v1/server/lightning/{cryptoCode}/invoices | Create lightning invoice
[**internal_lightning_node_api_get_balance**](LightningInternalNodeApi.md#internal_lightning_node_api_get_balance) | **GET** /api/v1/server/lightning/{cryptoCode}/balance | Get node balance
[**internal_lightning_node_api_get_channels**](LightningInternalNodeApi.md#internal_lightning_node_api_get_channels) | **GET** /api/v1/server/lightning/{cryptoCode}/channels | Get channels
[**internal_lightning_node_api_get_deposit_address**](LightningInternalNodeApi.md#internal_lightning_node_api_get_deposit_address) | **POST** /api/v1/server/lightning/{cryptoCode}/address | Get deposit address
[**internal_lightning_node_api_get_info**](LightningInternalNodeApi.md#internal_lightning_node_api_get_info) | **GET** /api/v1/server/lightning/{cryptoCode}/info | Get node information
[**internal_lightning_node_api_get_invoice**](LightningInternalNodeApi.md#internal_lightning_node_api_get_invoice) | **GET** /api/v1/server/lightning/{cryptoCode}/invoices/{id} | Get invoice
[**internal_lightning_node_api_get_invoices**](LightningInternalNodeApi.md#internal_lightning_node_api_get_invoices) | **GET** /api/v1/server/lightning/{cryptoCode}/invoices | Get invoices
[**internal_lightning_node_api_get_payment**](LightningInternalNodeApi.md#internal_lightning_node_api_get_payment) | **GET** /api/v1/server/lightning/{cryptoCode}/payments/{paymentHash} | Get payment
[**internal_lightning_node_api_get_payments**](LightningInternalNodeApi.md#internal_lightning_node_api_get_payments) | **GET** /api/v1/server/lightning/{cryptoCode}/payments | Get payments
[**internal_lightning_node_api_open_channel**](LightningInternalNodeApi.md#internal_lightning_node_api_open_channel) | **POST** /api/v1/server/lightning/{cryptoCode}/channels | Open channel
[**internal_lightning_node_api_pay_invoice**](LightningInternalNodeApi.md#internal_lightning_node_api_pay_invoice) | **POST** /api/v1/server/lightning/{cryptoCode}/invoices/pay | Pay Lightning Invoice


# **internal_lightning_node_api_connect_to_node**
> internal_lightning_node_api_connect_to_node(crypto_code, connect_to_node_request)

Connect to lightning node

Connect to another lightning node.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.connect_to_node_request import ConnectToNodeRequest
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    connect_to_node_request = btcpay_greenfield_py.ConnectToNodeRequest() # ConnectToNodeRequest | 

    try:
        # Connect to lightning node
        api_instance.internal_lightning_node_api_connect_to_node(crypto_code, connect_to_node_request)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_connect_to_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **connect_to_node_request** | [**ConnectToNodeRequest**](ConnectToNodeRequest.md)|  | 

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
**200** | Successfully connected |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;could-not-connect&#x60; |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_create_invoice**
> LightningInvoiceData internal_lightning_node_api_create_invoice(crypto_code, create_lightning_invoice_request)

Create lightning invoice

Create a lightning invoice.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.create_lightning_invoice_request import CreateLightningInvoiceRequest
from btcpay_greenfield_py.models.lightning_invoice_data import LightningInvoiceData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    create_lightning_invoice_request = btcpay_greenfield_py.CreateLightningInvoiceRequest() # CreateLightningInvoiceRequest | 

    try:
        # Create lightning invoice
        api_response = api_instance.internal_lightning_node_api_create_invoice(crypto_code, create_lightning_invoice_request)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_create_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **create_lightning_invoice_request** | [**CreateLightningInvoiceRequest**](CreateLightningInvoiceRequest.md)|  | 

### Return type

[**LightningInvoiceData**](LightningInvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created |  -  |
**400** | Wellknown error codes are: &#x60;invoice-error&#x60; |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_balance**
> LightningNodeBalanceData internal_lightning_node_api_get_balance(crypto_code)

Get node balance

View balance of the lightning node

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_node_balance_data import LightningNodeBalanceData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query

    try:
        # Get node balance
        api_response = api_instance.internal_lightning_node_api_get_balance(crypto_code)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_balance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**LightningNodeBalanceData**](LightningNodeBalanceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lightning node balance for on-chain and off-chain funds |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_channels**
> List[LightningChannelData] internal_lightning_node_api_get_channels(crypto_code)

Get channels

View information about the current channels of the lightning node

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_channel_data import LightningChannelData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query

    try:
        # Get channels
        api_response = api_instance.internal_lightning_node_api_get_channels(crypto_code)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_channels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**List[LightningChannelData]**](LightningChannelData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of channels |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_deposit_address**
> str internal_lightning_node_api_get_deposit_address(crypto_code)

Get deposit address

Get an on-chain deposit address for the lightning node 

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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query

    try:
        # Get deposit address
        api_response = api_instance.internal_lightning_node_api_get_deposit_address(crypto_code)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_deposit_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_deposit_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

**str**

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deposit address |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_info**
> LightningNodeInformationData internal_lightning_node_api_get_info(crypto_code)

Get node information

View information about the lightning node

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_node_information_data import LightningNodeInformationData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query

    try:
        # Get node information
        api_response = api_instance.internal_lightning_node_api_get_info(crypto_code)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**LightningNodeInformationData**](LightningNodeInformationData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lightning node information such as reachable nodeinfos |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_invoice**
> LightningInvoiceData internal_lightning_node_api_get_invoice(crypto_code, id)

Get invoice

View information about the requested lightning invoice

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_invoice_data import LightningInvoiceData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    id = 'id_example' # str | The id of the lightning invoice.

    try:
        # Get invoice
        api_response = api_instance.internal_lightning_node_api_get_invoice(crypto_code, id)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **id** | **str**| The id of the lightning invoice. | 

### Return type

[**LightningInvoiceData**](LightningInvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lightning invoice data |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration or the specified invoice was not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_invoices**
> List[LightningInvoiceData] internal_lightning_node_api_get_invoices(crypto_code, pending_only=pending_only, offset_index=offset_index)

Get invoices

View information about the lightning invoices

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_invoice_data import LightningInvoiceData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    pending_only = False # bool | Limit to pending invoices only (optional) (default to False)
    offset_index = 0 # float | The index of an invoice that will be used as the start of the list (optional) (default to 0)

    try:
        # Get invoices
        api_response = api_instance.internal_lightning_node_api_get_invoices(crypto_code, pending_only=pending_only, offset_index=offset_index)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_invoices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **pending_only** | **bool**| Limit to pending invoices only | [optional] [default to False]
 **offset_index** | **float**| The index of an invoice that will be used as the start of the list | [optional] [default to 0]

### Return type

[**List[LightningInvoiceData]**](LightningInvoiceData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lightning invoice data |  -  |
**401** | Missing authorization |  -  |
**503** | Unable to access the lightning node |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_payment**
> LightningPaymentData internal_lightning_node_api_get_payment(crypto_code, payment_hash)

Get payment

View information about the requested lightning payment

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_payment_data import LightningPaymentData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    payment_hash = 'payment_hash_example' # str | The payment hash of the lightning payment.

    try:
        # Get payment
        api_response = api_instance.internal_lightning_node_api_get_payment(crypto_code, payment_hash)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_payment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **payment_hash** | **str**| The payment hash of the lightning payment. | 

### Return type

[**LightningPaymentData**](LightningPaymentData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lightning payment data |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration or the specified invoice was not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_payments**
> List[LightningPaymentData] internal_lightning_node_api_get_payments(crypto_code, include_pending=include_pending, offset_index=offset_index)

Get payments

View information about the lightning payments

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_payment_data import LightningPaymentData
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    include_pending = False # bool | Also include pending payments (optional) (default to False)
    offset_index = 0 # float | The index of a payment that will be used as the start of the list (optional) (default to 0)

    try:
        # Get payments
        api_response = api_instance.internal_lightning_node_api_get_payments(crypto_code, include_pending=include_pending, offset_index=offset_index)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_get_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **include_pending** | **bool**| Also include pending payments | [optional] [default to False]
 **offset_index** | **float**| The index of a payment that will be used as the start of the list | [optional] [default to 0]

### Return type

[**List[LightningPaymentData]**](LightningPaymentData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lightning payment data |  -  |
**401** | Missing authorization |  -  |
**503** | Unable to access the lightning node |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_open_channel**
> internal_lightning_node_api_open_channel(crypto_code, open_lightning_channel_request)

Open channel

Open a channel with another lightning node. You should connect to that node first.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.open_lightning_channel_request import OpenLightningChannelRequest
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    open_lightning_channel_request = btcpay_greenfield_py.OpenLightningChannelRequest() # OpenLightningChannelRequest | 

    try:
        # Open channel
        api_instance.internal_lightning_node_api_open_channel(crypto_code, open_lightning_channel_request)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_open_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **open_lightning_channel_request** | [**OpenLightningChannelRequest**](OpenLightningChannelRequest.md)|  | 

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
**200** | Successfully opened |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;channel-already-exists&#x60;, &#x60;cannot-afford-funding&#x60;, &#x60;need-more-confirmations&#x60;, &#x60;peer-not-connected&#x60; |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_pay_invoice**
> LightningPaymentData internal_lightning_node_api_pay_invoice(crypto_code, pay_lightning_invoice_request)

Pay Lightning Invoice

Pay a lightning invoice. In case the payment response times out, the status will be reported as pending and the final status can be resolved using the [Get payment](#operation/InternalLightningNodeApi_GetPayment) endpoint. The default wait time for payment responses is 30 seconds — it might take longer if multiple routes are tried or a hold invoice is getting paid.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lightning_payment_data import LightningPaymentData
from btcpay_greenfield_py.models.pay_lightning_invoice_request import PayLightningInvoiceRequest
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
    api_instance = btcpay_greenfield_py.LightningInternalNodeApi(api_client)
    crypto_code = 'BTC' # str | The cryptoCode of the lightning-node to query
    pay_lightning_invoice_request = btcpay_greenfield_py.PayLightningInvoiceRequest() # PayLightningInvoiceRequest | 

    try:
        # Pay Lightning Invoice
        api_response = api_instance.internal_lightning_node_api_pay_invoice(crypto_code, pay_lightning_invoice_request)
        print("The response of LightningInternalNodeApi->internal_lightning_node_api_pay_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_pay_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **pay_lightning_invoice_request** | [**PayLightningInvoiceRequest**](PayLightningInvoiceRequest.md)|  | 

### Return type

[**LightningPaymentData**](LightningPaymentData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully paid |  -  |
**202** | Payment initiated |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;could-not-find-route&#x60;, &#x60;generic-error&#x60; |  -  |
**503** | Unable to access the lightning node |  -  |
**404** | The lightning node configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

