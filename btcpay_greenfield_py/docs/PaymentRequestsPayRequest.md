# PaymentRequestsPayRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **decimal.Decimal** | The amount of the invoice. If &#x60;null&#x60; or &#x60;unspecified&#x60;, it will be set to the payment request&#39;s due amount. Note that the payment&#39;s request &#x60;allowCustomPaymentAmounts&#x60; must be &#x60;true&#x60;, or a 422 error will be sent back.&#39; | [optional] 
**allow_pending_invoice_reuse** | **bool** | If &#x60;true&#x60;, this endpoint will not necessarily create a new invoice, and instead attempt to give back a pending one for this payment request. | [optional] [default to False]

## Example

```python
from btcpay_greenfield_py.models.payment_requests_pay_request import PaymentRequestsPayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestsPayRequest from a JSON string
payment_requests_pay_request_instance = PaymentRequestsPayRequest.from_json(json)
# print the JSON string representation of the object
print PaymentRequestsPayRequest.to_json()

# convert the object into a dict
payment_requests_pay_request_dict = payment_requests_pay_request_instance.to_dict()
# create an instance of PaymentRequestsPayRequest from a dict
payment_requests_pay_request_form_dict = payment_requests_pay_request.from_dict(payment_requests_pay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


