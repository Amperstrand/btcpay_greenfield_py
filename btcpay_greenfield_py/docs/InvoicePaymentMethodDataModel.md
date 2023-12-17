# InvoicePaymentMethodDataModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**crypto_code** | **str** | Crypto code of the payment method (e.g., \&quot;BTC\&quot; or \&quot;LTC\&quot;) | [optional] 
**destination** | **str** | The destination the payment must be made to | [optional] 
**payment_link** | **str** | A payment link that helps pay to the payment destination | [optional] 
**rate** | **decimal.Decimal** | The rate between this payment method&#39;s currency and the invoice currency | [optional] 
**payment_method_paid** | **decimal.Decimal** | The amount paid by this payment method | [optional] 
**total_paid** | **decimal.Decimal** | The total amount paid by all payment methods to the invoice, converted to this payment method&#39;s currency | [optional] 
**due** | **decimal.Decimal** | The total amount left to be paid, converted to this payment method&#39;s currency (will be negative if overpaid) | [optional] 
**amount** | **decimal.Decimal** | The invoice amount, converted to this payment method&#39;s currency | [optional] 
**network_fee** | **decimal.Decimal** | The added merchant fee to pay for network costs of this payment method. | [optional] 
**payments** | [**List[Payment]**](Payment.md) | Payments made with this payment method. | [optional] 
**activated** | **bool** | If the payment method is activated (when lazy payments option is enabled | [optional] 
**additional_data** | [**InvoicePaymentMethodDataModelAdditionalData**](InvoicePaymentMethodDataModelAdditionalData.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.invoice_payment_method_data_model import InvoicePaymentMethodDataModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePaymentMethodDataModel from a JSON string
invoice_payment_method_data_model_instance = InvoicePaymentMethodDataModel.from_json(json)
# print the JSON string representation of the object
print InvoicePaymentMethodDataModel.to_json()

# convert the object into a dict
invoice_payment_method_data_model_dict = invoice_payment_method_data_model_instance.to_dict()
# create an instance of InvoicePaymentMethodDataModel from a dict
invoice_payment_method_data_model_form_dict = invoice_payment_method_data_model.from_dict(invoice_payment_method_data_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


