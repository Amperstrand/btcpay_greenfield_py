# PayLightningInvoiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bolt11** | **str** | The BOLT11 of the invoice to pay | [optional] 
**amount** | **str** | Optional explicit payment amount in millisatoshi (if specified, it overrides the BOLT11 amount) | [optional] 
**max_fee_percent** | **float** | The fee limit expressed as a percentage of the payment amount | [optional] 
**max_fee_flat** | **str** | The fee limit expressed as a fixed amount in satoshi | [optional] 
**send_timeout** | **object** |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.pay_lightning_invoice_request import PayLightningInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayLightningInvoiceRequest from a JSON string
pay_lightning_invoice_request_instance = PayLightningInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print PayLightningInvoiceRequest.to_json()

# convert the object into a dict
pay_lightning_invoice_request_dict = pay_lightning_invoice_request_instance.to_dict()
# create an instance of PayLightningInvoiceRequest from a dict
pay_lightning_invoice_request_form_dict = pay_lightning_invoice_request.from_dict(pay_lightning_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


