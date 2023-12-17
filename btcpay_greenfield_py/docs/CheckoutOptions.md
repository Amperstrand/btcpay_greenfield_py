# CheckoutOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed_policy** | [**SpeedPolicy**](SpeedPolicy.md) |  | [optional] 
**payment_methods** | **List[str]** | A specific set of payment methods to use for this invoice (ie. BTC, BTC-LightningNetwork). By default, select all payment methods enabled in the store. | [optional] 
**default_payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**lazy_payment_methods** | **bool** | If true, payment methods are enabled individually upon user interaction in the invoice. Default to store&#39;s settings&#39; | [optional] 
**expiration_minutes** | **object** |  | [optional] 
**monitoring_minutes** | **object** |  | [optional] 
**payment_tolerance** | **float** | A percentage determining whether to count the invoice as paid when the invoice is paid within the specified margin of error. Defaults to the store&#39;s settings. (The default store settings is 100) | [optional] 
**redirect_url** | **str** | When the customer has paid the invoice, the URL where the customer will be redirected when clicking on the &#x60;return to store&#x60; button. You can use placeholders &#x60;{InvoiceId}&#x60; or &#x60;{OrderId}&#x60; in the URL, BTCPay Server will replace those with this invoice &#x60;id&#x60; or &#x60;metadata.orderId&#x60; respectively. | [optional] 
**redirect_automatically** | **bool** | When the customer has paid the invoice, and a &#x60;redirectURL&#x60; is set, the checkout is redirected to &#x60;redirectURL&#x60; automatically if &#x60;redirectAutomatically&#x60; is true. Defaults to the store&#39;s settings. (The default store settings is false) | [optional] 
**requires_refund_email** | **bool** | Invoice will require user to provide a refund email if this option is set to &#x60;true&#x60;. Has no effect if &#x60;buyerEmail&#x60; metadata is set as there is no email to collect in this case. | [optional] 
**checkout_type** | **str** | &#x60;\&quot;V1\&quot;&#x60;: The original checkout form    &#x60;\&quot;V2\&quot;&#x60;: The new experimental checkout form.    If &#x60;null&#x60; or unspecified, the store&#39;s settings will be used. | [optional] 
**default_language** | **str** | The language code (eg. en-US, en, fr-FR...) of the language presented to your customer in the checkout page. BTCPay Server tries to match the best language available. If null or not set, will fallback on the store&#39;s default language. You can see the list of language codes with [this operation](#operation/langCodes). | [optional] 

## Example

```python
from openapi_client.models.checkout_options import CheckoutOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutOptions from a JSON string
checkout_options_instance = CheckoutOptions.from_json(json)
# print the JSON string representation of the object
print CheckoutOptions.to_json()

# convert the object into a dict
checkout_options_dict = checkout_options_instance.to_dict()
# create an instance of CheckoutOptions from a dict
checkout_options_form_dict = checkout_options.from_dict(checkout_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


