# btcpay_greenfield_py.CustodiansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custodians_add_store_custodian_account**](CustodiansApi.md#custodians_add_store_custodian_account) | **POST** /api/v1/stores/{storeId}/custodian-accounts | Add a custodial account to a store.
[**custodians_delete_store_custodian_account**](CustodiansApi.md#custodians_delete_store_custodian_account) | **DELETE** /api/v1/stores/{storeId}/custodian-accounts/{accountId} | Delete store custodian account
[**custodians_get_store_custodian_account**](CustodiansApi.md#custodians_get_store_custodian_account) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId} | Get store custodian account
[**custodians_get_store_custodian_account_deposit_address**](CustodiansApi.md#custodians_get_store_custodian_account_deposit_address) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/addresses/{paymentMethod} | Get a deposit address for custodian
[**custodians_get_store_custodian_account_trade_quote**](CustodiansApi.md#custodians_get_store_custodian_account_trade_quote) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/trades/quote | Get quote for trading one asset for another
[**custodians_get_store_custodian_account_withdrawal_info**](CustodiansApi.md#custodians_get_store_custodian_account_withdrawal_info) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/withdrawals/{withdrawalId} | Get withdrawal info
[**custodians_get_store_custodian_accounts**](CustodiansApi.md#custodians_get_store_custodian_accounts) | **GET** /api/v1/stores/{storeId}/custodian-accounts | List store custodian accounts
[**custodians_get_supported_custodians**](CustodiansApi.md#custodians_get_supported_custodians) | **GET** /api/v1/custodians | List supported custodians
[**custodians_simulate_withdraw_from_store_custodian_account**](CustodiansApi.md#custodians_simulate_withdraw_from_store_custodian_account) | **POST** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/withdrawals/simulation | Simulate a withdrawal
[**custodians_store_custodian_account_trade_market**](CustodiansApi.md#custodians_store_custodian_account_trade_market) | **POST** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/trades/market | Trade one asset for another
[**custodians_update_store_custodian_account**](CustodiansApi.md#custodians_update_store_custodian_account) | **PUT** /api/v1/stores/{storeId}/custodian-accounts/{accountId} | Update custodial account
[**custodians_withdraw_from_store_custodian_account**](CustodiansApi.md#custodians_withdraw_from_store_custodian_account) | **POST** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/withdrawals | Withdraw to store wallet


# **custodians_add_store_custodian_account**
> CustodianAccountData custodians_add_store_custodian_account(store_id, create_custodian_account_request)

Add a custodial account to a store.

Add a custodial account to a store.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.create_custodian_account_request import CreateCustodianAccountRequest
from btcpay_greenfield_py.models.custodian_account_data import CustodianAccountData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    store_id = 'store_id_example' # str | The Store ID
    create_custodian_account_request = btcpay_greenfield_py.CreateCustodianAccountRequest() # CreateCustodianAccountRequest | 

    try:
        # Add a custodial account to a store.
        api_response = api_instance.custodians_add_store_custodian_account(store_id, create_custodian_account_request)
        print("The response of CustodiansApi->custodians_add_store_custodian_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_add_store_custodian_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **create_custodian_account_request** | [**CreateCustodianAccountRequest**](CreateCustodianAccountRequest.md)|  | 

### Return type

[**CustodianAccountData**](CustodianAccountData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the new custodian account |  -  |
**403** | If you are authenticated but forbidden to add new custodian account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_delete_store_custodian_account**
> custodians_delete_store_custodian_account(account_id, store_id)

Delete store custodian account

Deletes a custodial account

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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID
    store_id = 'store_id_example' # str | The Store ID

    try:
        # Delete store custodian account
        api_instance.custodians_delete_store_custodian_account(account_id, store_id)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_delete_store_custodian_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID | 
 **store_id** | **str**| The Store ID | 

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
**200** | Custodian account deleted |  -  |
**403** | If you are authenticated but forbidden to delete the custodian account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_store_custodian_account**
> CustodianAccountData custodians_get_store_custodian_account(account_id, store_id, asset_balances=asset_balances)

Get store custodian account

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.custodian_account_data import CustodianAccountData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID
    store_id = 'store_id_example' # str | The Store ID
    asset_balances = False # bool | Enable if you want the result to include the 'assetBalances' field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). (optional) (default to False)

    try:
        # Get store custodian account
        api_response = api_instance.custodians_get_store_custodian_account(account_id, store_id, asset_balances=asset_balances)
        print("The response of CustodiansApi->custodians_get_store_custodian_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_get_store_custodian_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID | 
 **store_id** | **str**| The Store ID | 
 **asset_balances** | **bool**| Enable if you want the result to include the &#39;assetBalances&#39; field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). | [optional] [default to False]

### Return type

[**CustodianAccountData**](CustodianAccountData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of custodian accounts for the store. |  -  |
**403** | If you are authenticated but forbidden to view the custodian account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_store_custodian_account_deposit_address**
> CustodiansGetStoreCustodianAccountDepositAddress200Response custodians_get_store_custodian_account_deposit_address(account_id, store_id, payment_method)

Get a deposit address for custodian

Get a new deposit address for the custodian using the specified payment method (network + crypto code).

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.custodians_get_store_custodian_account_deposit_address200_response import CustodiansGetStoreCustodianAccountDepositAddress200Response
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID.
    store_id = 'store_id_example' # str | The Store ID
    payment_method = 'payment_method_example' # str | The payment method to use for the deposit. Example: \"BTC-OnChain\" or \"BTC-Lightning\"

    try:
        # Get a deposit address for custodian
        api_response = api_instance.custodians_get_store_custodian_account_deposit_address(account_id, store_id, payment_method)
        print("The response of CustodiansApi->custodians_get_store_custodian_account_deposit_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_get_store_custodian_account_deposit_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID. | 
 **store_id** | **str**| The Store ID | 
 **payment_method** | **str**| The payment method to use for the deposit. Example: \&quot;BTC-OnChain\&quot; or \&quot;BTC-Lightning\&quot; | 

### Return type

[**CustodiansGetStoreCustodianAccountDepositAddress200Response**](CustodiansGetStoreCustodianAccountDepositAddress200Response.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deposit address |  -  |
**404** | The custodian does not support deposits using this payment method. |  -  |
**403** | If you are authenticated but forbidden to get the deposit address |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_store_custodian_account_trade_quote**
> QuoteResultData custodians_get_store_custodian_account_trade_quote(account_id, store_id, from_asset, to_asset)

Get quote for trading one asset for another

Get the current bid and ask price for converting one asset into another.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.quote_result_data import QuoteResultData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID.
    store_id = 'store_id_example' # str | The Store ID
    from_asset = 'from_asset_example' # str | The asset to convert.
    to_asset = 'to_asset_example' # str | The asset you want.

    try:
        # Get quote for trading one asset for another
        api_response = api_instance.custodians_get_store_custodian_account_trade_quote(account_id, store_id, from_asset, to_asset)
        print("The response of CustodiansApi->custodians_get_store_custodian_account_trade_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_get_store_custodian_account_trade_quote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID. | 
 **store_id** | **str**| The Store ID | 
 **from_asset** | **str**| The asset to convert. | 
 **to_asset** | **str**| The asset you want. | 

### Return type

[**QuoteResultData**](QuoteResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The quote for converting one asset to another. |  -  |
**404** | No tradable asset pair found for this trade. |  -  |
**403** | If you are authenticated but forbidden to create trades |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_store_custodian_account_withdrawal_info**
> WithdrawalResultData custodians_get_store_custodian_account_withdrawal_info(account_id, store_id, withdrawal_id)

Get withdrawal info

Get the details about a past withdrawal.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.withdrawal_result_data import WithdrawalResultData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID.
    store_id = 'store_id_example' # str | The Store ID
    withdrawal_id = 'withdrawal_id_example' # str | The Withdrawal ID.

    try:
        # Get withdrawal info
        api_response = api_instance.custodians_get_store_custodian_account_withdrawal_info(account_id, store_id, withdrawal_id)
        print("The response of CustodiansApi->custodians_get_store_custodian_account_withdrawal_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_get_store_custodian_account_withdrawal_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID. | 
 **store_id** | **str**| The Store ID | 
 **withdrawal_id** | **str**| The Withdrawal ID. | 

### Return type

[**WithdrawalResultData**](WithdrawalResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the withdrawal |  -  |
**404** | Withdrawal not found. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_store_custodian_accounts**
> List[CustodianAccountData] custodians_get_store_custodian_accounts(store_id, asset_balances=asset_balances)

List store custodian accounts

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.custodian_account_data import CustodianAccountData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    store_id = 'store_id_example' # str | The Store ID
    asset_balances = False # bool | Enable if you want the result to include the 'assetBalances' field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). (optional) (default to False)

    try:
        # List store custodian accounts
        api_response = api_instance.custodians_get_store_custodian_accounts(store_id, asset_balances=asset_balances)
        print("The response of CustodiansApi->custodians_get_store_custodian_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_get_store_custodian_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **asset_balances** | **bool**| Enable if you want the result to include the &#39;assetBalances&#39; field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). | [optional] [default to False]

### Return type

[**List[CustodianAccountData]**](CustodianAccountData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of custodian accounts for the store. |  -  |
**403** | If you are authenticated but forbidden to view the store&#39;s custodian accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_supported_custodians**
> List[CustodianData] custodians_get_supported_custodians()

List supported custodians

List all supported custodians for the BTCPay instance. You can install plugins to add more custodians.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.custodian_data import CustodianData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)

    try:
        # List supported custodians
        api_response = api_instance.custodians_get_supported_custodians()
        print("The response of CustodiansApi->custodians_get_supported_custodians:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_get_supported_custodians: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CustodianData]**](CustodianData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported custodians |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_simulate_withdraw_from_store_custodian_account**
> WithdrawalSimulationResultData custodians_simulate_withdraw_from_store_custodian_account(account_id, store_id, payment_method, qty, withdrawal_request_data)

Simulate a withdrawal

Get more information about a potential withdrawal including fees, minimum and maximum quantities for the given asset and quantity.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.withdrawal_request_data import WithdrawalRequestData
from btcpay_greenfield_py.models.withdrawal_simulation_result_data import WithdrawalSimulationResultData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID.
    store_id = 'store_id_example' # str | The Store ID
    payment_method = 'payment_method_example' # str | The payment method to be used for the withdrawal.
    qty = 3.4 # float | The quantity to simulate a withdrawal for.
    withdrawal_request_data = btcpay_greenfield_py.WithdrawalRequestData() # WithdrawalRequestData | 

    try:
        # Simulate a withdrawal
        api_response = api_instance.custodians_simulate_withdraw_from_store_custodian_account(account_id, store_id, payment_method, qty, withdrawal_request_data)
        print("The response of CustodiansApi->custodians_simulate_withdraw_from_store_custodian_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_simulate_withdraw_from_store_custodian_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID. | 
 **store_id** | **str**| The Store ID | 
 **payment_method** | **str**| The payment method to be used for the withdrawal. | 
 **qty** | **float**| The quantity to simulate a withdrawal for. | 
 **withdrawal_request_data** | [**WithdrawalRequestData**](WithdrawalRequestData.md)|  | 

### Return type

[**WithdrawalSimulationResultData**](WithdrawalSimulationResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a potential withdrawal including fees, minimum and maximum quantities. |  -  |
**400** | Withdrawal is not possible because you don&#39;t have this much in your account. |  -  |
**404** | Withdrawal is not possible for this payment method. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_store_custodian_account_trade_market**
> TradeResultData custodians_store_custodian_account_trade_market(account_id, store_id, trade_request_data=trade_request_data)

Trade one asset for another

Trade one asset for another using a market order (=instant purchase with instant result or failure). A suitable asset pair will automatically be selected. If no asset pair is available, the call will fail.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.trade_request_data import TradeRequestData
from btcpay_greenfield_py.models.trade_result_data import TradeResultData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID.
    store_id = 'store_id_example' # str | The Store ID
    trade_request_data = btcpay_greenfield_py.TradeRequestData() # TradeRequestData |  (optional)

    try:
        # Trade one asset for another
        api_response = api_instance.custodians_store_custodian_account_trade_market(account_id, store_id, trade_request_data=trade_request_data)
        print("The response of CustodiansApi->custodians_store_custodian_account_trade_market:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_store_custodian_account_trade_market: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID. | 
 **store_id** | **str**| The Store ID | 
 **trade_request_data** | [**TradeRequestData**](TradeRequestData.md)|  | [optional] 

### Return type

[**TradeResultData**](TradeResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the trade that was executed |  -  |
**404** | No tradable asset pair found for this trade. |  -  |
**403** | If you are authenticated but forbidden to create trades |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_update_store_custodian_account**
> CustodianAccountData custodians_update_store_custodian_account(account_id, store_id, create_custodian_account_request)

Update custodial account

Update custodial account

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.create_custodian_account_request import CreateCustodianAccountRequest
from btcpay_greenfield_py.models.custodian_account_data import CustodianAccountData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID
    store_id = 'store_id_example' # str | The Store ID
    create_custodian_account_request = btcpay_greenfield_py.CreateCustodianAccountRequest() # CreateCustodianAccountRequest | 

    try:
        # Update custodial account
        api_response = api_instance.custodians_update_store_custodian_account(account_id, store_id, create_custodian_account_request)
        print("The response of CustodiansApi->custodians_update_store_custodian_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_update_store_custodian_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID | 
 **store_id** | **str**| The Store ID | 
 **create_custodian_account_request** | [**CreateCustodianAccountRequest**](CreateCustodianAccountRequest.md)|  | 

### Return type

[**CustodianAccountData**](CustodianAccountData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated custodian account |  -  |
**403** | If you are authenticated but forbidden to modify new custodian account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_withdraw_from_store_custodian_account**
> WithdrawalResultData custodians_withdraw_from_store_custodian_account(account_id, store_id, withdrawal_request_data)

Withdraw to store wallet

Withdraw an asset to your store wallet.

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import btcpay_greenfield_py
from btcpay_greenfield_py.models.withdrawal_request_data import WithdrawalRequestData
from btcpay_greenfield_py.models.withdrawal_result_data import WithdrawalResultData
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
    api_instance = btcpay_greenfield_py.CustodiansApi(api_client)
    account_id = 'account_id_example' # str | The Custodian Account ID.
    store_id = 'store_id_example' # str | The Store ID
    withdrawal_request_data = btcpay_greenfield_py.WithdrawalRequestData() # WithdrawalRequestData | 

    try:
        # Withdraw to store wallet
        api_response = api_instance.custodians_withdraw_from_store_custodian_account(account_id, store_id, withdrawal_request_data)
        print("The response of CustodiansApi->custodians_withdraw_from_store_custodian_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustodiansApi->custodians_withdraw_from_store_custodian_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The Custodian Account ID. | 
 **store_id** | **str**| The Store ID | 
 **withdrawal_request_data** | [**WithdrawalRequestData**](WithdrawalRequestData.md)|  | 

### Return type

[**WithdrawalResultData**](WithdrawalResultData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the withdrawal that was executed |  -  |
**400** | Withdrawal is not possible because you don&#39;t have this much in your account. |  -  |
**404** | Withdrawal is not possible for this asset. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

