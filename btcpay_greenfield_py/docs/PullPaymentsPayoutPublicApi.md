# openapi_client.PullPaymentsPayoutPublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pull_payments_get_payout**](PullPaymentsPayoutPublicApi.md#pull_payments_get_payout) | **GET** /api/v1/pull-payments/{pullPaymentId}/payouts/{payoutId} | Get Payout


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
    api_instance = openapi_client.PullPaymentsPayoutPublicApi(api_client)
    pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
    payout_id = 'payout_id_example' # str | The ID of the pull payment payout

    try:
        # Get Payout
        api_response = api_instance.pull_payments_get_payout(pull_payment_id, payout_id)
        print("The response of PullPaymentsPayoutPublicApi->pull_payments_get_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullPaymentsPayoutPublicApi->pull_payments_get_payout: %s\n" % e)
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

