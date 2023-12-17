# openapi_client.PullPaymentsPublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pull_payments_create_payout**](PullPaymentsPublicApi.md#pull_payments_create_payout) | **POST** /api/v1/pull-payments/{pullPaymentId}/payouts | Create Payout
[**pull_payments_get_payout**](PullPaymentsPublicApi.md#pull_payments_get_payout) | **GET** /api/v1/pull-payments/{pullPaymentId}/payouts/{payoutId} | Get Payout
[**pull_payments_get_payouts**](PullPaymentsPublicApi.md#pull_payments_get_payouts) | **GET** /api/v1/pull-payments/{pullPaymentId}/payouts | Get Payouts
[**pull_payments_get_pull_payment**](PullPaymentsPublicApi.md#pull_payments_get_pull_payment) | **GET** /api/v1/pull-payments/{pullPaymentId} | Get Pull Payment
[**pull_payments_get_pull_payment_lnurl**](PullPaymentsPublicApi.md#pull_payments_get_pull_payment_lnurl) | **GET** /api/v1/pull-payments/{pullPaymentId}/lnurl | Get Pull Payment LNURL details


# **pull_payments_create_payout**
> PayoutData pull_payments_create_payout(pull_payment_id, create_payout_request)

Create Payout

Create a new payout

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_payout_request import CreatePayoutRequest
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
    api_instance = openapi_client.PullPaymentsPublicApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
    create_payout_request = openapi_client.CreatePayoutRequest() # CreatePayoutRequest | 

    try:
        # Create Payout
        api_response = api_instance.pull_payments_create_payout(pull_payment_id, create_payout_request)
        print("The response of PullPaymentsPublicApi->pull_payments_create_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsPublicApi->pull_payments_create_payout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 
 **create_payout_request** | [**CreatePayoutRequest**](CreatePayoutRequest.md)|  | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new payout has been created |  -  |
**404** | Pull payment not found |  -  |
**422** | Unable to validate the request |  -  |
**400** | Wellknown error codes are: &#x60;duplicate-destination&#x60;, &#x60;expired&#x60;, &#x60;not-started&#x60;, &#x60;archived&#x60;, &#x60;overdraft&#x60;, &#x60;amount-too-low&#x60;, &#x60;payment-method-not-supported&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_payout**
> PayoutData pull_payments_get_payout(pull_payment_id, payout_id)

Get Payout

Get payout

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
    api_instance = openapi_client.PullPaymentsPublicApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
    payout_id = 'payout_id_example' # str | The ID of the pull payment payout

    try:
        # Get Payout
        api_response = api_instance.pull_payments_get_payout(pull_payment_id, payout_id)
        print("The response of PullPaymentsPublicApi->pull_payments_get_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsPublicApi->pull_payments_get_payout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 
 **payout_id** | **str**| The ID of the pull payment payout | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific payout of a pull payment |  -  |
**404** | Pull payment payout not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_payouts**
> List[PayoutData] pull_payments_get_payouts(pull_payment_id, include_cancelled=include_cancelled)

Get Payouts

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
    api_instance = openapi_client.PullPaymentsPublicApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
    include_cancelled = False # bool | Whether this should list cancelled payouts (optional) (default to False)

    try:
        # Get Payouts
        api_response = api_instance.pull_payments_get_payouts(pull_payment_id, include_cancelled=include_cancelled)
        print("The response of PullPaymentsPublicApi->pull_payments_get_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsPublicApi->pull_payments_get_payouts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 
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
**200** | The payouts of the pull payment |  -  |
**404** | Pull payment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_pull_payment**
> PullPaymentData pull_payments_get_pull_payment(pull_payment_id)

Get Pull Payment

Get a pull payment

### Example

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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PullPaymentsPublicApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment

    try:
        # Get Pull Payment
        api_response = api_instance.pull_payments_get_pull_payment(pull_payment_id)
        print("The response of PullPaymentsPublicApi->pull_payments_get_pull_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsPublicApi->pull_payments_get_pull_payment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 

### Return type

[**PullPaymentData**](PullPaymentData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the pull payment |  -  |
**404** | Pull payment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_pull_payment_lnurl**
> LNURLData pull_payments_get_pull_payment_lnurl(pull_payment_id)

Get Pull Payment LNURL details

Get Pull Payment LNURL details

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.lnurl_data import LNURLData
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
    api_instance = openapi_client.PullPaymentsPublicApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment

    try:
        # Get Pull Payment LNURL details
        api_response = api_instance.pull_payments_get_pull_payment_lnurl(pull_payment_id)
        print("The response of PullPaymentsPublicApi->pull_payments_get_pull_payment_lnurl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsPublicApi->pull_payments_get_pull_payment_lnurl: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 

### Return type

[**LNURLData**](LNURLData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pull payment LNURL details |  -  |
**404** | Pull payment not found |  -  |
**400** | Pull payment found but does not support LNURL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

