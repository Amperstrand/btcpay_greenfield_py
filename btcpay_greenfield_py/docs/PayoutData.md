# PayoutData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the payout | [optional] 
**revision** | **int** | The revision number of the payout. This revision number is incremented when the payout amount or destination is modified before the approval. | [optional] 
**pull_payment_id** | **str** | The id of the pull payment this payout belongs to | [optional] 
**var_date** | **str** | The creation date of the payout as a unix timestamp | [optional] 
**destination** | **str** | The destination of the payout (can be an address or a BIP21 url) | [optional] 
**amount** | **decimal.Decimal** | The amount of the payout in the currency of the pull payment (eg. USD). | [optional] 
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**crypto_code** | **str** | Crypto code of the payment method of the payout (e.g., \&quot;BTC\&quot; or \&quot;LTC\&quot;) | [optional] 
**payment_method_amount** | **decimal.Decimal** | The amount of the payout in the currency of the payment method (eg. BTC). This is only available from the &#x60;AwaitingPayment&#x60; state. | [optional] 
**state** | [**PayoutState**](PayoutState.md) |  | [optional] 
**payment_proof** | [**PayoutPaymentProof**](PayoutPaymentProof.md) |  | [optional] 
**metadata** | **AnyOf[str, object]** | Additional information around the payout that can be supplied. The mentioned properties are all optional and you can introduce any json format you wish. | [optional] 

## Example

```python
from openapi_client.models.payout_data import PayoutData

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutData from a JSON string
payout_data_instance = PayoutData.from_json(json)
# print the JSON string representation of the object
print PayoutData.to_json()

# convert the object into a dict
payout_data_dict = payout_data_instance.to_dict()
# create an instance of PayoutData from a dict
payout_data_form_dict = payout_data.from_dict(payout_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


