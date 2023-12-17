# btcpay_greenfield_py.AuthorizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_keys_authorize**](AuthorizationApi.md#api_keys_authorize) | **GET** /api-keys/authorize | Authorize User


# **api_keys_authorize**
> api_keys_authorize(permissions=permissions, strict=strict, application_identifier=application_identifier, selective_stores=selective_stores, application_name=application_name, redirect=redirect)

Authorize User

Redirect the browser to this endpoint to request the user to generate an api-key with specific permissions

### Example

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


# Enter a context with an instance of the API client
with btcpay_greenfield_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = btcpay_greenfield_py.AuthorizationApi(api_client)
    permissions = ['permissions_example'] # List[str] | The permissions to request. (See API Key authentication) (optional)
    strict = True # bool | If permissions are specified, and strict is set to false, it will allow the user to reject some of permissions the application is requesting. (optional) (default to True)
    application_identifier = 'application_identifier_example' # str | If specified, BTCPay Server will check if there is an existing API key associated with the user that also has this application identifier, redirect host AND the permissions required match(takes selectiveStores and strict into account). `applicationIdentifier` is ignored if redirect is not specified. (optional)
    selective_stores = False # bool | If the application is requesting the CanModifyStoreSettings permission and selectiveStores is set to true, this allows the user to only grant permissions to selected stores under the user's control. (optional) (default to False)
    application_name = 'application_name_example' # str | The name of your application (optional)
    redirect = 'redirect_example' # str | The url to redirect to after the user consents, with the query parameters appended to it: permissions, user-id, api-key. If not specified, user is redirected to their API Key list. (optional)

    try:
        # Authorize User
        api_instance.api_keys_authorize(permissions=permissions, strict=strict, application_identifier=application_identifier, selective_stores=selective_stores, application_name=application_name, redirect=redirect)
    except Exception as e:
        print("Exception when calling AuthorizationApi->api_keys_authorize: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions** | [**List[str]**](str.md)| The permissions to request. (See API Key authentication) | [optional] 
 **strict** | **bool**| If permissions are specified, and strict is set to false, it will allow the user to reject some of permissions the application is requesting. | [optional] [default to True]
 **application_identifier** | **str**| If specified, BTCPay Server will check if there is an existing API key associated with the user that also has this application identifier, redirect host AND the permissions required match(takes selectiveStores and strict into account). &#x60;applicationIdentifier&#x60; is ignored if redirect is not specified. | [optional] 
 **selective_stores** | **bool**| If the application is requesting the CanModifyStoreSettings permission and selectiveStores is set to true, this allows the user to only grant permissions to selected stores under the user&#39;s control. | [optional] [default to False]
 **application_name** | **str**| The name of your application | [optional] 
 **redirect** | **str**| The url to redirect to after the user consents, with the query parameters appended to it: permissions, user-id, api-key. If not specified, user is redirected to their API Key list. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A HTML form that a user can use to confirm permissions to grant |  -  |
**307** | Makes browser do an HTTP POST request to the specified url in &#x60;redirect&#x60; with a JSON body consisting of &#x60;apiKey&#x60; (the api key created or matched), &#x60;permissions&#x60; (the permissions the user consented to), and &#x60;userId&#x60; (the id of the user that consented) upon consent |  -  |
**401** | Missing authorization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

