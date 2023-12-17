# btcpay_greenfield_py.StoresRatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stores_get_store_rates**](StoresRatesApi.md#stores_get_store_rates) | **GET** /api/v1/stores/{storeId}/rates | Get rates


# **stores_get_store_rates**
> List[StoreRateResult] stores_get_store_rates(store_id, currency_pair=currency_pair)

Get rates

Get rates on the store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.store_rate_result import StoreRateResult
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
    api_instance = btcpay_greenfield_py.StoresRatesApi(api_client)
    store_id = 'store_id_example' # str | The store to fetch
    currency_pair = ['[\"BTC_USD\",\"BTC_EUR\"]'] # List[str] | The currency pairs to fetch rates for (optional)

    try:
        # Get rates
        api_response = api_instance.stores_get_store_rates(store_id, currency_pair=currency_pair)
        print("The response of StoresRatesApi->stores_get_store_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresRatesApi->stores_get_store_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **currency_pair** | [**List[str]**](str.md)| The currency pairs to fetch rates for | [optional] 

### Return type

[**List[StoreRateResult]**](StoreRateResult.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The settings were executed and a preview was returned |  -  |
**400** | A list of errors that occurred when previewing the settings |  -  |
**403** | If you are authenticated but forbidden to modify the store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

