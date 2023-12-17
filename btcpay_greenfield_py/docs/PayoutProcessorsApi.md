# btcpay_greenfield_py.PayoutProcessorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payout_processors_get_payout_processors**](PayoutProcessorsApi.md#payout_processors_get_payout_processors) | **GET** /api/v1/payout-processors | Get payout processors


# **payout_processors_get_payout_processors**
> List[PayoutProcessorData] payout_processors_get_payout_processors()

Get payout processors

Get payout processors available in this instance

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
    api_instance = btcpay_greenfield_py.PayoutProcessorsApi(api_client)

    try:
        # Get payout processors
        api_response = api_instance.payout_processors_get_payout_processors()
        print("The response of PayoutProcessorsApi->payout_processors_get_payout_processors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutProcessorsApi->payout_processors_get_payout_processors: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**200** | available payout processors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

