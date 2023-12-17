# btcpay_greenfield_py.MiscelleneousApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate_sources**](MiscelleneousApi.md#get_rate_sources) | **GET** /misc/rate-sources | Get available rate sources
[**invoice_checkout**](MiscelleneousApi.md#invoice_checkout) | **GET** /i/{invoiceId} | Invoice checkout
[**lang_codes**](MiscelleneousApi.md#lang_codes) | **GET** /misc/lang | Language codes
[**permissions_metadata**](MiscelleneousApi.md#permissions_metadata) | **GET** /misc/permissions | Permissions metadata


# **get_rate_sources**
> List[GetRateSources200ResponseInner] get_rate_sources()

Get available rate sources

View available rate providers that you can use in stores

### Example

```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.get_rate_sources200_response_inner import GetRateSources200ResponseInner
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.MiscelleneousApi(api_client)

    try:
        # Get available rate sources
        api_response = api_instance.get_rate_sources()
        print("The response of MiscelleneousApi->get_rate_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscelleneousApi->get_rate_sources: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[GetRateSources200ResponseInner]**](GetRateSources200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rate providers array |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_checkout**
> invoice_checkout(invoice_id, lang=lang)

Invoice checkout

View the checkout page of an invoice

### Example

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


# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.MiscelleneousApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice id
    lang = 'lang_example' # str | The preferred language of the checkout page. You can use \"auto\" to use the language of the customer's browser or see the list of language codes with [this operation](#operation/langCodes). (optional)

    try:
        # Invoice checkout
        api_instance.invoice_checkout(invoice_id, lang=lang)
    except Exception as e:
        print("Exception when calling MiscelleneousApi->invoice_checkout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice id | 
 **lang** | **str**| The preferred language of the checkout page. You can use \&quot;auto\&quot; to use the language of the customer&#39;s browser or see the list of language codes with [this operation](#operation/langCodes). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The checkout page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lang_codes**
> List[LangCodes200ResponseInner] lang_codes()

Language codes

The supported language codes

### Example

```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.lang_codes200_response_inner import LangCodes200ResponseInner
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.MiscelleneousApi(api_client)

    try:
        # Language codes
        api_response = api_instance.lang_codes()
        print("The response of MiscelleneousApi->lang_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscelleneousApi->lang_codes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LangCodes200ResponseInner]**](LangCodes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The supported language codes |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_metadata**
> List[PermissionsMetadata200ResponseInner] permissions_metadata()

Permissions metadata

The metadata of available permissions

### Example

```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.permissions_metadata200_response_inner import PermissionsMetadata200ResponseInner
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = btcpay_greenfield_py.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.MiscelleneousApi(api_client)

    try:
        # Permissions metadata
        api_response = api_instance.permissions_metadata()
        print("The response of MiscelleneousApi->permissions_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscelleneousApi->permissions_metadata: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[PermissionsMetadata200ResponseInner]**](PermissionsMetadata200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata of available permissions |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

