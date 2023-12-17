# btcpay_greenfield_py.PointOfSaleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_get_point_of_sale_app**](PointOfSaleApi.md#apps_get_point_of_sale_app) | **GET** /api/v1/apps/pos/{appId} | Get Point of Sale app data


# **apps_get_point_of_sale_app**
> PointOfSaleAppData apps_get_point_of_sale_app(app_id)

Get Point of Sale app data

Returns POS app data

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.point_of_sale_app_data import PointOfSaleAppData
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
    api_instance = btcpay_greenfield_py.PointOfSaleApi(api_client)
    app_id = 'app_id_example' # str | App ID

    try:
        # Get Point of Sale app data
        api_response = api_instance.apps_get_point_of_sale_app(app_id)
        print("The response of PointOfSaleApi->apps_get_point_of_sale_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSaleApi->apps_get_point_of_sale_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 

### Return type

[**PointOfSaleAppData**](PointOfSaleAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POS app data |  -  |
**404** | POS app with specified ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

