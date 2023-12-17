# WithdrawalRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**qty** | [**WithdrawalRequestDataQty**](WithdrawalRequestDataQty.md) |  | [optional] 

## Example

```python
from openapi_client.models.withdrawal_request_data import WithdrawalRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalRequestData from a JSON string
withdrawal_request_data_instance = WithdrawalRequestData.from_json(json)
# print the JSON string representation of the object
print WithdrawalRequestData.to_json()

# convert the object into a dict
withdrawal_request_data_dict = withdrawal_request_data_instance.to_dict()
# create an instance of WithdrawalRequestData from a dict
withdrawal_request_data_form_dict = withdrawal_request_data.from_dict(withdrawal_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


