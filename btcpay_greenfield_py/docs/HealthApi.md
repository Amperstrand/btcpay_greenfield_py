# btcpay_greenfield_py.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get_health**](HealthApi.md#health_get_health) | **GET** /api/v1/health | Get health status


# **health_get_health**
> ApplicationHealthData health_get_health()

Get health status

Check the instance health status

### Example

```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.application_health_data import ApplicationHealthData
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
    api_instance = btcpay_greenfield_py.HealthApi(api_client)

    try:
        # Get health status
        api_response = api_instance.health_get_health()
        print("The response of HealthApi->health_get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_get_health: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationHealthData**](ApplicationHealthData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance is up |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

