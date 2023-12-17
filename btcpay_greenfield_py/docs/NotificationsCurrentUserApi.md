# openapi_client.NotificationsCurrentUserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_delete_notification**](NotificationsCurrentUserApi.md#notifications_delete_notification) | **DELETE** /api/v1/users/me/notifications/{id} | Remove Notification
[**notifications_get_notification**](NotificationsCurrentUserApi.md#notifications_get_notification) | **GET** /api/v1/users/me/notifications/{id} | Get notification
[**notifications_get_notifications**](NotificationsCurrentUserApi.md#notifications_get_notifications) | **GET** /api/v1/users/me/notifications | Get notifications
[**notifications_update_notification**](NotificationsCurrentUserApi.md#notifications_update_notification) | **PUT** /api/v1/users/me/notifications/{id} | Update notification


# **notifications_delete_notification**
> notifications_delete_notification(id)

Remove Notification

Removes the specified notification.

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
    api_instance = openapi_client.NotificationsCurrentUserApi(api_client)
    id = 'id_example' # str | The notification to remove

    try:
        # Remove Notification
        api_instance.notifications_delete_notification(id)
    except Exception as e:
        print("Exception when calling NotificationsCurrentUserApi->notifications_delete_notification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The notification to remove | 

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
**200** | The notification has been deleted |  -  |
**403** | If you are authenticated but forbidden to remove the specified notification |  -  |
**404** | The key is not found for this notification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_get_notification**
> NotificationData notifications_get_notification(id)

Get notification

View information about the specified notification

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.notification_data import NotificationData
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
    api_instance = openapi_client.NotificationsCurrentUserApi(api_client)
    id = 'id_example' # str | The notification to fetch

    try:
        # Get notification
        api_response = api_instance.notifications_get_notification(id)
        print("The response of NotificationsCurrentUserApi->notifications_get_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsCurrentUserApi->notifications_get_notification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The notification to fetch | 

### Return type

[**NotificationData**](NotificationData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified notification |  -  |
**403** | If you are authenticated but forbidden to view the specified notification |  -  |
**404** | The key is not found for this notification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_get_notifications**
> NotificationData notifications_get_notifications(take=take, skip=skip, seen=seen)

Get notifications

View current user's notifications

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.notification_data import NotificationData
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
    api_instance = openapi_client.NotificationsCurrentUserApi(api_client)
    take = 3.4 # float | Number of records returned in response (optional)
    skip = 3.4 # float | Number of records to skip (optional)
    seen = 'seen_example' # str | filter by seen notifications (optional)

    try:
        # Get notifications
        api_response = api_instance.notifications_get_notifications(take=take, skip=skip, seen=seen)
        print("The response of NotificationsCurrentUserApi->notifications_get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsCurrentUserApi->notifications_get_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**| Number of records returned in response | [optional] 
 **skip** | **float**| Number of records to skip | [optional] 
 **seen** | **str**| filter by seen notifications | [optional] 

### Return type

[**NotificationData**](NotificationData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of notifications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_update_notification**
> NotificationData notifications_update_notification(id, update_notification)

Update notification

Updates the notification

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.notification_data import NotificationData
from openapi_client.models.update_notification import UpdateNotification
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
    api_instance = openapi_client.NotificationsCurrentUserApi(api_client)
    id = 'id_example' # str | The notification to update
    update_notification = openapi_client.UpdateNotification() # UpdateNotification | 

    try:
        # Update notification
        api_response = api_instance.notifications_update_notification(id, update_notification)
        print("The response of NotificationsCurrentUserApi->notifications_update_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsCurrentUserApi->notifications_update_notification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The notification to update | 
 **update_notification** | [**UpdateNotification**](UpdateNotification.md)|  | 

### Return type

[**NotificationData**](NotificationData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated notification |  -  |
**403** | If you are authenticated but forbidden to update the specified notification |  -  |
**404** | The key is not found for this notification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

