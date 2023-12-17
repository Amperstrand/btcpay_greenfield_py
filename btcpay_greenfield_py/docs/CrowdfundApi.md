# btcpay_greenfield_py.CrowdfundApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_create_crowdfund_app**](CrowdfundApi.md#apps_create_crowdfund_app) | **POST** /api/v1/stores/{storeId}/apps/crowdfund | Create a new Crowdfund app
[**apps_get_crowdfund_app**](CrowdfundApi.md#apps_get_crowdfund_app) | **GET** /api/v1/apps/crowdfund/{appId} | Get crowdfund app data


# **apps_create_crowdfund_app**
> CrowdfundAppData apps_create_crowdfund_app(store_id, create_crowdfund_app_request)

Create a new Crowdfund app

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.create_crowdfund_app_request import CreateCrowdfundAppRequest
from btcpay_greenfield_py.models.crowdfund_app_data import CrowdfundAppData
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
    api_instance = btcpay_greenfield_py.CrowdfundApi(api_client)
    store_id = 'store_id_example' # str | The store ID
    create_crowdfund_app_request = btcpay_greenfield_py.CreateCrowdfundAppRequest() # CreateCrowdfundAppRequest | 

    try:
        # Create a new Crowdfund app
        api_response = api_instance.apps_create_crowdfund_app(store_id, create_crowdfund_app_request)
        print("The response of CrowdfundApi->apps_create_crowdfund_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrowdfundApi->apps_create_crowdfund_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **create_crowdfund_app_request** | [**CreateCrowdfundAppRequest**](CreateCrowdfundAppRequest.md)|  | 

### Return type

[**CrowdfundAppData**](CrowdfundAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created app details |  -  |
**422** | Unable to validate the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_crowdfund_app**
> CrowdfundAppData apps_get_crowdfund_app(app_id)

Get crowdfund app data

Returns crowdfund app data

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.crowdfund_app_data import CrowdfundAppData
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
    api_instance = btcpay_greenfield_py.CrowdfundApi(api_client)
    app_id = 'app_id_example' # str | Crowdfund app ID

    try:
        # Get crowdfund app data
        api_response = api_instance.apps_get_crowdfund_app(app_id)
        print("The response of CrowdfundApi->apps_get_crowdfund_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrowdfundApi->apps_get_crowdfund_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Crowdfund app ID | 

### Return type

[**CrowdfundAppData**](CrowdfundAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crowdfund app data |  -  |
**404** | Crowdfund app with specified ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

