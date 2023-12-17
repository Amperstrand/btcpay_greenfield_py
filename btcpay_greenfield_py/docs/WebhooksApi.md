# openapi_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create_webhook**](WebhooksApi.md#webhooks_create_webhook) | **POST** /api/v1/stores/{storeId}/webhooks | Create a new webhook
[**webhooks_delete_webhook**](WebhooksApi.md#webhooks_delete_webhook) | **DELETE** /api/v1/stores/{storeId}/webhooks/{webhookId} | Delete a webhook
[**webhooks_get_webhook**](WebhooksApi.md#webhooks_get_webhook) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId} | Get a webhook of a store
[**webhooks_get_webhook_deliveries**](WebhooksApi.md#webhooks_get_webhook_deliveries) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries | Get latest deliveries
[**webhooks_get_webhook_delivery**](WebhooksApi.md#webhooks_get_webhook_delivery) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries/{deliveryId} | Get a webhook delivery
[**webhooks_get_webhook_delivery_requests**](WebhooksApi.md#webhooks_get_webhook_delivery_requests) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries/{deliveryId}/request | Get the delivery&#39;s request
[**webhooks_get_webhooks**](WebhooksApi.md#webhooks_get_webhooks) | **GET** /api/v1/stores/{storeId}/webhooks | Get webhooks of a store
[**webhooks_redeliver_webhook_delivery**](WebhooksApi.md#webhooks_redeliver_webhook_delivery) | **POST** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries/{deliveryId}/redeliver | Redeliver the delivery
[**webhooks_update_webhook**](WebhooksApi.md#webhooks_update_webhook) | **PUT** /api/v1/stores/{storeId}/webhooks/{webhookId} | Update a webhook


# **webhooks_create_webhook**
> WebhookDataCreateResult webhooks_create_webhook(store_id, webhook_data_create)

Create a new webhook

Create a new webhook

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_data_create import WebhookDataCreate
from openapi_client.models.webhook_data_create_result import WebhookDataCreateResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    store_id = 'store_id_example' # str | The store id
    webhook_data_create = openapi_client.WebhookDataCreate() # WebhookDataCreate | 

    try:
        # Create a new webhook
        api_response = api_instance.webhooks_create_webhook(store_id, webhook_data_create)
        print("The response of WebhooksApi->webhooks_create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_create_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_data_create** | [**WebhookDataCreate**](WebhookDataCreate.md)|  | 

### Return type

[**WebhookDataCreateResult**](WebhookDataCreateResult.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the new webhook |  -  |
**400** | A list of errors that occurred when creating the webhook |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_delete_webhook**
> webhooks_delete_webhook(store_id, webhook_id)

Delete a webhook

Delete a webhook

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id

    try:
        # Delete a webhook
        api_instance.webhooks_delete_webhook(store_id, webhook_id)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_delete_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

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
**200** | The webhook has been deleted |  -  |
**404** | The webhook does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_webhook**
> WebhookData webhooks_get_webhook(store_id, webhook_id)

Get a webhook of a store

View webhook of a store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_data import WebhookData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id

    try:
        # Get a webhook of a store
        api_response = api_instance.webhooks_get_webhook(store_id, webhook_id)
        print("The response of WebhooksApi->webhooks_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_get_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

### Return type

[**WebhookData**](WebhookData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A webhook |  -  |
**404** | The webhook has not been found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_webhook_deliveries**
> List[WebhookDeliveryData] webhooks_get_webhook_deliveries(store_id, webhook_id, count=count)

Get latest deliveries

List the latest deliveries to the webhook, ordered from the most recent

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_delivery_data import WebhookDeliveryData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id
    count = 'count_example' # str | The number of latest deliveries to fetch (optional)

    try:
        # Get latest deliveries
        api_response = api_instance.webhooks_get_webhook_deliveries(store_id, webhook_id, count=count)
        print("The response of WebhooksApi->webhooks_get_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_get_webhook_deliveries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 
 **count** | **str**| The number of latest deliveries to fetch | [optional] 

### Return type

[**List[WebhookDeliveryData]**](WebhookDeliveryData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of deliveries |  -  |
**404** | The key is not found for this list of deliveries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_webhook_delivery**
> WebhookDeliveryData webhooks_get_webhook_delivery(delivery_id, store_id, webhook_id)

Get a webhook delivery

Information about a webhook delivery

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_delivery_data import WebhookDeliveryData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    delivery_id = 'delivery_id_example' # str | The id of the delivery
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id

    try:
        # Get a webhook delivery
        api_response = api_instance.webhooks_get_webhook_delivery(delivery_id, store_id, webhook_id)
        print("The response of WebhooksApi->webhooks_get_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_get_webhook_delivery: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**| The id of the delivery | 
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

### Return type

[**WebhookDeliveryData**](WebhookDeliveryData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a delivery |  -  |
**404** | The delivery does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_webhook_delivery_requests**
> Dict[str, object] webhooks_get_webhook_delivery_requests(delivery_id, store_id, webhook_id)

Get the delivery's request

The delivery's JSON request sent to the endpoint

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    delivery_id = 'delivery_id_example' # str | The id of the delivery
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id

    try:
        # Get the delivery's request
        api_response = api_instance.webhooks_get_webhook_delivery_requests(delivery_id, store_id, webhook_id)
        print("The response of WebhooksApi->webhooks_get_webhook_delivery_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_get_webhook_delivery_requests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**| The id of the delivery | 
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

### Return type

**Dict[str, object]**

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delivery&#39;s JSON Request |  -  |
**404** | The delivery does not exists. |  -  |
**409** | &#x60;webhookdelivery-pruned&#x60;: This webhook delivery has been pruned, so it can&#39;t be redelivered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_webhooks**
> List[WebhookData] webhooks_get_webhooks(store_id)

Get webhooks of a store

View webhooks of a store

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_data import WebhookData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    store_id = 'store_id_example' # str | The store id

    try:
        # Get webhooks of a store
        api_response = api_instance.webhooks_get_webhooks(store_id)
        print("The response of WebhooksApi->webhooks_get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_get_webhooks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 

### Return type

[**List[WebhookData]**](WebhookData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of webhooks |  -  |
**404** | The key is not found for this list of webhooks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_redeliver_webhook_delivery**
> str webhooks_redeliver_webhook_delivery(delivery_id, store_id, webhook_id)

Redeliver the delivery

Redeliver the delivery

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    delivery_id = 'delivery_id_example' # str | The id of the delivery
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id

    try:
        # Redeliver the delivery
        api_response = api_instance.webhooks_redeliver_webhook_delivery(delivery_id, store_id, webhook_id)
        print("The response of WebhooksApi->webhooks_redeliver_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_redeliver_webhook_delivery: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**| The id of the delivery | 
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

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
**200** | The new delivery id being broadcasted. (Broadcast happen asynchronously with this call) |  -  |
**404** | The delivery does not exists. |  -  |
**409** | &#x60;webhookdelivery-pruned&#x60;: This webhook delivery has been pruned, so it can&#39;t be redelivered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update_webhook**
> WebhookData webhooks_update_webhook(store_id, webhook_id, webhook_data_update)

Update a webhook

Update a webhook

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_data import WebhookData
from openapi_client.models.webhook_data_update import WebhookDataUpdate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: API_Key
configuration.api_key['API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    store_id = 'store_id_example' # str | The store id
    webhook_id = 'webhook_id_example' # str | The webhook id
    webhook_data_update = openapi_client.WebhookDataUpdate() # WebhookDataUpdate | 

    try:
        # Update a webhook
        api_response = api_instance.webhooks_update_webhook(store_id, webhook_id, webhook_data_update)
        print("The response of WebhooksApi->webhooks_update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_update_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 
 **webhook_data_update** | [**WebhookDataUpdate**](WebhookDataUpdate.md)|  | 

### Return type

[**WebhookData**](WebhookData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the updated webhook |  -  |
**400** | A list of errors that occurred when creating the webhook |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

