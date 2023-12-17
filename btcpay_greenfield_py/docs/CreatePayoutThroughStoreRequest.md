# CreatePayoutThroughStoreRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The destination of the payout (can be an address or a BIP21 url) | [optional] 
**amount** | **decimal.Decimal** | The amount of the payout in the currency of the pull payment (eg. USD). | [optional] 
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**pull_payment_id** | **str** | The pull payment to create this for. Optional. | [optional] 
**approved** | **bool** | Whether to approve this payout automatically upon creation | [optional] 
**metadata** | **object** | Additional metadata to store with the payout | [optional] 

## Example

```python
from openapi_client.models.create_payout_through_store_request import CreatePayoutThroughStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayoutThroughStoreRequest from a JSON string
create_payout_through_store_request_instance = CreatePayoutThroughStoreRequest.from_json(json)
# print the JSON string representation of the object
print CreatePayoutThroughStoreRequest.to_json()

# convert the object into a dict
create_payout_through_store_request_dict = create_payout_through_store_request_instance.to_dict()
# create an instance of CreatePayoutThroughStoreRequest from a dict
create_payout_through_store_request_form_dict = create_payout_through_store_request.from_dict(create_payout_through_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


