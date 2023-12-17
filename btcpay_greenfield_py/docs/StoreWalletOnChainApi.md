# openapi_client.StoreWalletOnChainApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_on_chain_wallets_add_or_update_on_chain_wallet_link**](StoreWalletOnChainApi.md#store_on_chain_wallets_add_or_update_on_chain_wallet_link) | **POST** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/objects/{objectType}/{objectId}/links | Add/Update store on-chain wallet object link
[**store_on_chain_wallets_add_or_update_on_chain_wallet_objects**](StoreWalletOnChainApi.md#store_on_chain_wallets_add_or_update_on_chain_wallet_objects) | **POST** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/objects | Add/Update store on-chain wallet objects
[**store_on_chain_wallets_create_on_chain_transaction**](StoreWalletOnChainApi.md#store_on_chain_wallets_create_on_chain_transaction) | **POST** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions | Create store on-chain wallet transaction
[**store_on_chain_wallets_get_on_chain_fee_rate**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_fee_rate) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/feerate | Get store on-chain wallet fee rate
[**store_on_chain_wallets_get_on_chain_wallet_object**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_object) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/objects/{objectType}/{objectId} | Get store on-chain wallet object
[**store_on_chain_wallets_get_on_chain_wallet_objects**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_objects) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/objects | Get store on-chain wallet objects
[**store_on_chain_wallets_get_on_chain_wallet_receive_address**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_receive_address) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/address | Get store on-chain wallet address
[**store_on_chain_wallets_get_on_chain_wallet_transaction**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_transaction) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions/{transactionId} | Get store on-chain wallet transaction
[**store_on_chain_wallets_get_on_chain_wallet_utxos**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_utxos) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/utxos | Get store on-chain wallet UTXOS
[**store_on_chain_wallets_patch_on_chain_wallet_transaction**](StoreWalletOnChainApi.md#store_on_chain_wallets_patch_on_chain_wallet_transaction) | **PATCH** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions/{transactionId} | Patch store on-chain wallet transaction info
[**store_on_chain_wallets_remove_on_chain_wallet_link**](StoreWalletOnChainApi.md#store_on_chain_wallets_remove_on_chain_wallet_link) | **DELETE** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/objects/{objectType}/{objectId}/links/{linkType}/{linkId} | Remove store on-chain wallet object links
[**store_on_chain_wallets_remove_on_chain_wallet_object**](StoreWalletOnChainApi.md#store_on_chain_wallets_remove_on_chain_wallet_object) | **DELETE** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/objects/{objectType}/{objectId} | Remove store on-chain wallet objects
[**store_on_chain_wallets_show_on_chain_wallet_overview**](StoreWalletOnChainApi.md#store_on_chain_wallets_show_on_chain_wallet_overview) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet | Get store on-chain wallet overview
[**store_on_chain_wallets_show_on_chain_wallet_transactions**](StoreWalletOnChainApi.md#store_on_chain_wallets_show_on_chain_wallet_transactions) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions | Get store on-chain wallet transactions
[**store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address**](StoreWalletOnChainApi.md#store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address) | **DELETE** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/address | UnReserve last store on-chain wallet address


# **store_on_chain_wallets_add_or_update_on_chain_wallet_link**
> store_on_chain_wallets_add_or_update_on_chain_wallet_link(crypto_code, object_id, object_type, store_id, add_on_chain_wallet_object_link_request)

Add/Update store on-chain wallet object link

Add/Update wallet object link

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.add_on_chain_wallet_object_link_request import AddOnChainWalletObjectLinkRequest
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    object_id = 'abc392...' # str | The object id to fetch
    object_type = 'tx' # str | The object type to fetch
    store_id = 'store_id_example' # str | The store to fetch
    add_on_chain_wallet_object_link_request = openapi_client.AddOnChainWalletObjectLinkRequest() # AddOnChainWalletObjectLinkRequest | 

    try:
        # Add/Update store on-chain wallet object link
        api_instance.store_on_chain_wallets_add_or_update_on_chain_wallet_link(crypto_code, object_id, object_type, store_id, add_on_chain_wallet_object_link_request)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_add_or_update_on_chain_wallet_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **object_id** | **str**| The object id to fetch | 
 **object_type** | **str**| The object type to fetch | 
 **store_id** | **str**| The store to fetch | 
 **add_on_chain_wallet_object_link_request** | [**AddOnChainWalletObjectLinkRequest**](AddOnChainWalletObjectLinkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | action completed |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_add_or_update_on_chain_wallet_objects**
> OnChainWalletObjectData store_on_chain_wallets_add_or_update_on_chain_wallet_objects(crypto_code, store_id, on_chain_wallet_object_data)

Add/Update store on-chain wallet objects

Add/Update wallet objects

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_object_data import OnChainWalletObjectData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    on_chain_wallet_object_data = openapi_client.OnChainWalletObjectData() # OnChainWalletObjectData | 

    try:
        # Add/Update store on-chain wallet objects
        api_response = api_instance.store_on_chain_wallets_add_or_update_on_chain_wallet_objects(crypto_code, store_id, on_chain_wallet_object_data)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_add_or_update_on_chain_wallet_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_add_or_update_on_chain_wallet_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **on_chain_wallet_object_data** | [**OnChainWalletObjectData**](OnChainWalletObjectData.md)|  | 

### Return type

[**OnChainWalletObjectData**](OnChainWalletObjectData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wallet object&#39;s data and its links |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_create_on_chain_transaction**
> StoreOnChainWalletsCreateOnChainTransaction200Response store_on_chain_wallets_create_on_chain_transaction(crypto_code, store_id, create_on_chain_transaction_request)

Create store on-chain wallet transaction

Create store on-chain wallet transaction

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_on_chain_transaction_request import CreateOnChainTransactionRequest
from openapi_client.models.store_on_chain_wallets_create_on_chain_transaction200_response import StoreOnChainWalletsCreateOnChainTransaction200Response
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the wallet
    store_id = 'store_id_example' # str | The store to fetch
    create_on_chain_transaction_request = openapi_client.CreateOnChainTransactionRequest() # CreateOnChainTransactionRequest | 

    try:
        # Create store on-chain wallet transaction
        api_response = api_instance.store_on_chain_wallets_create_on_chain_transaction(crypto_code, store_id, create_on_chain_transaction_request)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_create_on_chain_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_create_on_chain_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the wallet | 
 **store_id** | **str**| The store to fetch | 
 **create_on_chain_transaction_request** | [**CreateOnChainTransactionRequest**](CreateOnChainTransactionRequest.md)|  | 

### Return type

[**StoreOnChainWalletsCreateOnChainTransaction200Response**](StoreOnChainWalletsCreateOnChainTransaction200Response.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the tx |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_fee_rate**
> OnChainWalletFeeRateData store_on_chain_wallets_get_on_chain_fee_rate(crypto_code, store_id, block_target=block_target)

Get store on-chain wallet fee rate

Get wallet onchain fee rate

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_fee_rate_data import OnChainWalletFeeRateData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    block_target = 3.4 # float | The number of blocks away you are willing to target for confirmation. Defaults to the wallet's configured `RecommendedFeeBlockTarget` (optional)

    try:
        # Get store on-chain wallet fee rate
        api_response = api_instance.store_on_chain_wallets_get_on_chain_fee_rate(crypto_code, store_id, block_target=block_target)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_fee_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_fee_rate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **block_target** | **float**| The number of blocks away you are willing to target for confirmation. Defaults to the wallet&#39;s configured &#x60;RecommendedFeeBlockTarget&#x60; | [optional] 

### Return type

[**OnChainWalletFeeRateData**](OnChainWalletFeeRateData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fee rate |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_object**
> OnChainWalletObjectData store_on_chain_wallets_get_on_chain_wallet_object(crypto_code, object_id, object_type, store_id, include_neighbour_data=include_neighbour_data)

Get store on-chain wallet object

View wallet object

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_object_data import OnChainWalletObjectData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    object_id = 'abc392...' # str | The object id to fetch
    object_type = 'tx' # str | The object type to fetch
    store_id = 'store_id_example' # str | The store to fetch
    include_neighbour_data = True # bool | Whether or not you should include neighbour's node data in the result (ie, `links.objectData`) (optional) (default to True)

    try:
        # Get store on-chain wallet object
        api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_object(crypto_code, object_id, object_type, store_id, include_neighbour_data=include_neighbour_data)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **object_id** | **str**| The object id to fetch | 
 **object_type** | **str**| The object type to fetch | 
 **store_id** | **str**| The store to fetch | 
 **include_neighbour_data** | **bool**| Whether or not you should include neighbour&#39;s node data in the result (ie, &#x60;links.objectData&#x60;) | [optional] [default to True]

### Return type

[**OnChainWalletObjectData**](OnChainWalletObjectData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wallet object&#39;s data and its links |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_objects**
> List[OnChainWalletObjectData] store_on_chain_wallets_get_on_chain_wallet_objects(crypto_code, store_id, ids=ids, type=type, include_neighbour_data=include_neighbour_data)

Get store on-chain wallet objects

View wallet objects

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_object_data import OnChainWalletObjectData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    ids = ['03abcde...'] # List[str] | The ids of objects to fetch, if used, type should be specified (optional)
    type = 'tx' # str | The type of object to fetch (optional)
    include_neighbour_data = True # bool | Whether or not you should include neighbour's node data in the result (ie, `links.objectData`) (optional) (default to True)

    try:
        # Get store on-chain wallet objects
        api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_objects(crypto_code, store_id, ids=ids, type=type, include_neighbour_data=include_neighbour_data)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **ids** | [**List[str]**](str.md)| The ids of objects to fetch, if used, type should be specified | [optional] 
 **type** | **str**| The type of object to fetch | [optional] 
 **include_neighbour_data** | **bool**| Whether or not you should include neighbour&#39;s node data in the result (ie, &#x60;links.objectData&#x60;) | [optional] [default to True]

### Return type

[**List[OnChainWalletObjectData]**](OnChainWalletObjectData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Selected objects and their links |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_receive_address**
> OnChainWalletAddressData store_on_chain_wallets_get_on_chain_wallet_receive_address(crypto_code, store_id, force_generate=force_generate)

Get store on-chain wallet address

Get or generate address for wallet

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_address_data import OnChainWalletAddressData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch
    force_generate = False # bool | Whether to generate a new address for this request even if the previous one was not used (optional) (default to False)

    try:
        # Get store on-chain wallet address
        api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_receive_address(crypto_code, store_id, force_generate=force_generate)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_receive_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_receive_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 
 **force_generate** | **bool**| Whether to generate a new address for this request even if the previous one was not used | [optional] [default to False]

### Return type

[**OnChainWalletAddressData**](OnChainWalletAddressData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reserved address |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_transaction**
> OnChainWalletTransactionData store_on_chain_wallets_get_on_chain_wallet_transaction(crypto_code, store_id, transaction_id)

Get store on-chain wallet transaction

Get store on-chain wallet transaction

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_transaction_data import OnChainWalletTransactionData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the wallet to fetch
    store_id = 'store_id_example' # str | The store to fetch
    transaction_id = 'transaction_id_example' # str | The transaction id to fetch

    try:
        # Get store on-chain wallet transaction
        api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_transaction(crypto_code, store_id, transaction_id)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **store_id** | **str**| The store to fetch | 
 **transaction_id** | **str**| The transaction id to fetch | 

### Return type

[**OnChainWalletTransactionData**](OnChainWalletTransactionData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transaction |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_utxos**
> List[OnChainWalletUTXOData] store_on_chain_wallets_get_on_chain_wallet_utxos(crypto_code, store_id)

Get store on-chain wallet UTXOS

Get store on-chain wallet utxos

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_utxo_data import OnChainWalletUTXOData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the wallet to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store on-chain wallet UTXOS
        api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_utxos(crypto_code, store_id)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_utxos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_utxos: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**List[OnChainWalletUTXOData]**](OnChainWalletUTXOData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | utxo list |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_patch_on_chain_wallet_transaction**
> OnChainWalletTransactionData store_on_chain_wallets_patch_on_chain_wallet_transaction(crypto_code, store_id, transaction_id, patch_on_chain_transaction_request, force=force)

Patch store on-chain wallet transaction info

Patch store on-chain wallet transaction info

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_transaction_data import OnChainWalletTransactionData
from openapi_client.models.patch_on_chain_transaction_request import PatchOnChainTransactionRequest
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the wallet to fetch
    store_id = 'store_id_example' # str | The store to fetch
    transaction_id = 'transaction_id_example' # str | The transaction id to fetch
    patch_on_chain_transaction_request = openapi_client.PatchOnChainTransactionRequest() # PatchOnChainTransactionRequest | 
    force = 'force_example' # str | Whether to update the label/comments even if the transaction does not yet exist (optional)

    try:
        # Patch store on-chain wallet transaction info
        api_response = api_instance.store_on_chain_wallets_patch_on_chain_wallet_transaction(crypto_code, store_id, transaction_id, patch_on_chain_transaction_request, force=force)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_patch_on_chain_wallet_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_patch_on_chain_wallet_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **store_id** | **str**| The store to fetch | 
 **transaction_id** | **str**| The transaction id to fetch | 
 **patch_on_chain_transaction_request** | [**PatchOnChainTransactionRequest**](PatchOnChainTransactionRequest.md)|  | 
 **force** | **str**| Whether to update the label/comments even if the transaction does not yet exist | [optional] 

### Return type

[**OnChainWalletTransactionData**](OnChainWalletTransactionData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transaction |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_remove_on_chain_wallet_link**
> store_on_chain_wallets_remove_on_chain_wallet_link(crypto_code, link_id, object_id, link_type, object_type, store_id)

Remove store on-chain wallet object links

Remove wallet object link

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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    link_id = 'abc392...' # str | The object id of the linked neighbour
    object_id = 'abc392...' # str | The object id to fetch
    link_type = 'tx' # str | The object type of the linked neighbour
    object_type = 'tx' # str | The object type to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Remove store on-chain wallet object links
        api_instance.store_on_chain_wallets_remove_on_chain_wallet_link(crypto_code, link_id, object_id, link_type, object_type, store_id)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_remove_on_chain_wallet_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **link_id** | **str**| The object id of the linked neighbour | 
 **object_id** | **str**| The object id to fetch | 
 **link_type** | **str**| The object type of the linked neighbour | 
 **object_type** | **str**| The object type to fetch | 
 **store_id** | **str**| The store to fetch | 

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
**200** | successful removal of filtered object link |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_remove_on_chain_wallet_object**
> store_on_chain_wallets_remove_on_chain_wallet_object(crypto_code, object_id, object_type, store_id)

Remove store on-chain wallet objects

Remove wallet object

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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    object_id = 'abc392...' # str | The object id to fetch
    object_type = 'tx' # str | The object type to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Remove store on-chain wallet objects
        api_instance.store_on_chain_wallets_remove_on_chain_wallet_object(crypto_code, object_id, object_type, store_id)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_remove_on_chain_wallet_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **object_id** | **str**| The object id to fetch | 
 **object_type** | **str**| The object type to fetch | 
 **store_id** | **str**| The store to fetch | 

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
**200** | successful removal of filtered object |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_show_on_chain_wallet_overview**
> OnChainWalletOverviewData store_on_chain_wallets_show_on_chain_wallet_overview(crypto_code, store_id)

Get store on-chain wallet overview

View information about the specified wallet

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_overview_data import OnChainWalletOverviewData
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # Get store on-chain wallet overview
        api_response = api_instance.store_on_chain_wallets_show_on_chain_wallet_overview(crypto_code, store_id)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_show_on_chain_wallet_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_show_on_chain_wallet_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 

### Return type

[**OnChainWalletOverviewData**](OnChainWalletOverviewData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | specified wallet |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_show_on_chain_wallet_transactions**
> List[OnChainWalletTransactionData] store_on_chain_wallets_show_on_chain_wallet_transactions(crypto_code, store_id, label_filter=label_filter, limit=limit, skip=skip, status_filter=status_filter)

Get store on-chain wallet transactions

Get store on-chain wallet transactions

### Example

* Basic Authentication (Basic):
* Api Key Authentication (API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.on_chain_wallet_transaction_data import OnChainWalletTransactionData
from openapi_client.models.transaction_status import TransactionStatus
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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the wallet to fetch
    store_id = 'store_id_example' # str | The store to fetch
    label_filter = 'invoice' # str | Transaction label to filter by (optional)
    limit = 56 # int | Maximum number of transactions to return (optional)
    skip = 56 # int | Number of transactions to skip from the start (optional)
    status_filter = [openapi_client.TransactionStatus()] # List[TransactionStatus] | Statuses to filter the transactions with (optional)

    try:
        # Get store on-chain wallet transactions
        api_response = api_instance.store_on_chain_wallets_show_on_chain_wallet_transactions(crypto_code, store_id, label_filter=label_filter, limit=limit, skip=skip, status_filter=status_filter)
        print("The response of StoreWalletOnChainApi->store_on_chain_wallets_show_on_chain_wallet_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_show_on_chain_wallet_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **store_id** | **str**| The store to fetch | 
 **label_filter** | **str**| Transaction label to filter by | [optional] 
 **limit** | **int**| Maximum number of transactions to return | [optional] 
 **skip** | **int**| Number of transactions to skip from the start | [optional] 
 **status_filter** | [**List[TransactionStatus]**](TransactionStatus.md)| Statuses to filter the transactions with | [optional] 

### Return type

[**List[OnChainWalletTransactionData]**](OnChainWalletTransactionData.md)

### Authorization

[Basic](../README.md#Basic), [API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transactions list |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet |  -  |
**503** | You need to allow non-admins to use hotwallets for their stores (in /server/policies) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address**
> store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address(crypto_code, store_id)

UnReserve last store on-chain wallet address

UnReserve address

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
    api_instance = openapi_client.StoreWalletOnChainApi(api_client)
    crypto_code = 'BTC' # str | The crypto code of the payment method to fetch
    store_id = 'store_id_example' # str | The store to fetch

    try:
        # UnReserve last store on-chain wallet address
        api_instance.store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address(crypto_code, store_id)
    except Exception as e:
        print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **store_id** | **str**| The store to fetch | 

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
**200** | address unreserved |  -  |
**403** | If you are authenticated but forbidden to view the specified store |  -  |
**404** | The key is not found for this store/wallet or there was no address reserved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

