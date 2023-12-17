# btcpay_greenfield_py.AppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_create_crowdfund_app**](AppsApi.md#apps_create_crowdfund_app) | **POST** /api/v1/stores/{storeId}/apps/crowdfund | Create a new Crowdfund app
[**apps_create_point_of_sale_app**](AppsApi.md#apps_create_point_of_sale_app) | **POST** /api/v1/stores/{storeId}/apps/pos | Create a new Point of Sale app
[**apps_delete_app**](AppsApi.md#apps_delete_app) | **DELETE** /api/v1/apps/{appId} | Delete app
[**apps_get_all_apps**](AppsApi.md#apps_get_all_apps) | **GET** /api/v1/apps | Get basic app data for all apps for all stores for a user
[**apps_get_all_apps_for_store**](AppsApi.md#apps_get_all_apps_for_store) | **GET** /api/v1/stores/{storeId}/apps | Get basic app data for all apps for a store
[**apps_get_app**](AppsApi.md#apps_get_app) | **GET** /api/v1/apps/{appId} | Get basic app data
[**apps_get_crowdfund_app**](AppsApi.md#apps_get_crowdfund_app) | **GET** /api/v1/apps/crowdfund/{appId} | Get crowdfund app data
[**apps_get_point_of_sale_app**](AppsApi.md#apps_get_point_of_sale_app) | **GET** /api/v1/apps/pos/{appId} | Get Point of Sale app data
[**apps_put_point_of_sale_app**](AppsApi.md#apps_put_point_of_sale_app) | **PUT** /api/v1/apps/pos/{appId} | Update a Point of Sale app


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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    store_id = 'store_id_example' # str | The store ID
    create_crowdfund_app_request = btcpay_greenfield_py.CreateCrowdfundAppRequest() # CreateCrowdfundAppRequest | 

    try:
        # Create a new Crowdfund app
        api_response = api_instance.apps_create_crowdfund_app(store_id, create_crowdfund_app_request)
        print("The response of AppsApi->apps_create_crowdfund_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_create_crowdfund_app: %s\n" % e)
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

# **apps_create_point_of_sale_app**
> PointOfSaleAppData apps_create_point_of_sale_app(store_id, create_point_of_sale_app_request)

Create a new Point of Sale app

Point of Sale app allows accepting payments for items in a virtual store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.create_point_of_sale_app_request import CreatePointOfSaleAppRequest
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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    store_id = 'store_id_example' # str | The store ID
    create_point_of_sale_app_request = btcpay_greenfield_py.CreatePointOfSaleAppRequest() # CreatePointOfSaleAppRequest | 

    try:
        # Create a new Point of Sale app
        api_response = api_instance.apps_create_point_of_sale_app(store_id, create_point_of_sale_app_request)
        print("The response of AppsApi->apps_create_point_of_sale_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_create_point_of_sale_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **create_point_of_sale_app_request** | [**CreatePointOfSaleAppRequest**](CreatePointOfSaleAppRequest.md)|  | 

### Return type

[**PointOfSaleAppData**](PointOfSaleAppData.md)

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

# **apps_delete_app**
> apps_delete_app(app_id)

Delete app

Deletes apps with specified ID

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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    app_id = 'app_id_example' # str | The app ID

    try:
        # Delete app
        api_instance.apps_delete_app(app_id)
    except Exception as e:
        print("Exception when calling AppsApi->apps_delete_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App was deleted |  -  |
**404** | App with specified ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_all_apps**
> List[BasicAppData] apps_get_all_apps()

Get basic app data for all apps for all stores for a user

Returns basic app data for all apps for all stores

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.basic_app_data import BasicAppData
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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)

    try:
        # Get basic app data for all apps for all stores for a user
        api_response = api_instance.apps_get_all_apps()
        print("The response of AppsApi->apps_get_all_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_get_all_apps: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[BasicAppData]**](BasicAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of basic app data object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_all_apps_for_store**
> List[BasicAppData] apps_get_all_apps_for_store(store_id)

Get basic app data for all apps for a store

Returns basic app data for all apps for a store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.basic_app_data import BasicAppData
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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    store_id = 'store_id_example' # str | The store ID

    try:
        # Get basic app data for all apps for a store
        api_response = api_instance.apps_get_all_apps_for_store(store_id)
        print("The response of AppsApi->apps_get_all_apps_for_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_get_all_apps_for_store: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 

### Return type

[**List[BasicAppData]**](BasicAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of basic app data object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_app**
> BasicAppData apps_get_app(app_id)

Get basic app data

Returns basic app data shared between all types of apps

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.basic_app_data import BasicAppData
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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    app_id = 'app_id_example' # str | The app ID

    try:
        # Get basic app data
        api_response = api_instance.apps_get_app(app_id)
        print("The response of AppsApi->apps_get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_get_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 

### Return type

[**BasicAppData**](BasicAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic app data |  -  |
**404** | App with specified ID was not found |  -  |

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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    app_id = 'app_id_example' # str | Crowdfund app ID

    try:
        # Get crowdfund app data
        api_response = api_instance.apps_get_crowdfund_app(app_id)
        print("The response of AppsApi->apps_get_crowdfund_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_get_crowdfund_app: %s\n" % e)
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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    app_id = 'app_id_example' # str | App ID

    try:
        # Get Point of Sale app data
        api_response = api_instance.apps_get_point_of_sale_app(app_id)
        print("The response of AppsApi->apps_get_point_of_sale_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_get_point_of_sale_app: %s\n" % e)
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

# **apps_put_point_of_sale_app**
> PointOfSaleAppData apps_put_point_of_sale_app(app_id, create_point_of_sale_app_request)

Update a Point of Sale app

Use this endpoint for updating the properties of a POS app

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.create_point_of_sale_app_request import CreatePointOfSaleAppRequest
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
    api_instance = btcpay_greenfield_py.AppsApi(api_client)
    app_id = 'app_id_example' # str | App ID
    create_point_of_sale_app_request = btcpay_greenfield_py.CreatePointOfSaleAppRequest() # CreatePointOfSaleAppRequest | 

    try:
        # Update a Point of Sale app
        api_response = api_instance.apps_put_point_of_sale_app(app_id, create_point_of_sale_app_request)
        print("The response of AppsApi->apps_put_point_of_sale_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->apps_put_point_of_sale_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **create_point_of_sale_app_request** | [**CreatePointOfSaleAppRequest**](CreatePointOfSaleAppRequest.md)|  | 

### Return type

[**PointOfSaleAppData**](PointOfSaleAppData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App details |  -  |
**422** | Unable to validate the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

