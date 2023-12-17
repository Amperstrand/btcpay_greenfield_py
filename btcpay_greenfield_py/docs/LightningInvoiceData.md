# LightningInvoiceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invoice&#39;s ID | [optional] 
**status** | [**LightningInvoiceStatus**](LightningInvoiceStatus.md) |  | [optional] 
**bolt11** | **str** | The BOLT11 representation of the invoice | [optional] 
**paid_at** | **float** | A unix timestamp in seconds | [optional] 
**expires_at** | **float** | A unix timestamp in seconds | [optional] 
**amount** | **str** | The amount of the invoice in millisatoshi | [optional] 
**amount_received** | **str** | The amount received in millisatoshi | [optional] 
**payment_hash** | **str** | The payment hash | [optional] 
**preimage** | **str** | The payment preimage (available when status is complete) | [optional] 
**custom_records** | **object** | The custom TLV records attached to a keysend payment | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lightning_invoice_data import LightningInvoiceData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningInvoiceData from a JSON string
lightning_invoice_data_instance = LightningInvoiceData.from_json(json)
# print the JSON string representation of the object
print LightningInvoiceData.to_json()

# convert the object into a dict
lightning_invoice_data_dict = lightning_invoice_data_instance.to_dict()
# create an instance of LightningInvoiceData from a dict
lightning_invoice_data_form_dict = lightning_invoice_data.from_dict(lightning_invoice_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


