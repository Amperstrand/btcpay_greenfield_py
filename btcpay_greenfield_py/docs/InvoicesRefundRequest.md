# InvoicesRefundRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the pull payment (Default: &#39;Refund&#39; followed by the invoice id) | [optional] 
**description** | **str** | Description of the pull payment | [optional] 
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**refund_variant** | **str** | * &#x60;RateThen&#x60;: Refund the crypto currency price, at the rate the invoice got paid.  * &#x60;CurrentRate&#x60;: Refund the crypto currency price, at the current rate.  *&#x60;Fiat&#x60;: Refund the invoice currency, at the rate when the refund will be sent.  *&#x60;OverpaidAmount&#x60;: Refund the crypto currency amount that was overpaid.  *&#x60;Custom&#x60;: Specify the amount, currency, and rate of the refund. (see &#x60;customAmount&#x60; and &#x60;customCurrency&#x60;) | [optional] 
**subtract_percentage** | **decimal.Decimal** | Optional percentage by which to reduce the refund, e.g. as processing charge or to compensate for the mining fee. | [optional] 
**custom_amount** | **decimal.Decimal** | The amount to refund if the &#x60;refundVariant&#x60; is &#x60;Custom&#x60;. | [optional] 
**custom_currency** | **str** | The currency to refund if the &#x60;refundVariant&#x60; is &#x60;Custom&#x60; | [optional] 

## Example

```python
from openapi_client.models.invoices_refund_request import InvoicesRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesRefundRequest from a JSON string
invoices_refund_request_instance = InvoicesRefundRequest.from_json(json)
# print the JSON string representation of the object
print InvoicesRefundRequest.to_json()

# convert the object into a dict
invoices_refund_request_dict = invoices_refund_request_instance.to_dict()
# create an instance of InvoicesRefundRequest from a dict
invoices_refund_request_form_dict = invoices_refund_request.from_dict(invoices_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


