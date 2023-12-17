# InvoiceDataBaseReceipt

Additional settings to customize the public receipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | A public page will be accessible once the invoice is settled. If null or unspecified, it will fallback to the store&#39;s settings. (The default store settings is true) | [optional] 
**show_qr** | **bool** | Show the QR code of the receipt in the public receipt page. If null or unspecified, it will fallback to the store&#39;s settings. (The default store setting is true) | [optional] 
**show_payments** | **bool** | Show the payment list in the public receipt page. If null or unspecified, it will fallback to the store&#39;s settings. (The default store setting is true) | [optional] 

## Example

```python
from openapi_client.models.invoice_data_base_receipt import InvoiceDataBaseReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDataBaseReceipt from a JSON string
invoice_data_base_receipt_instance = InvoiceDataBaseReceipt.from_json(json)
# print the JSON string representation of the object
print InvoiceDataBaseReceipt.to_json()

# convert the object into a dict
invoice_data_base_receipt_dict = invoice_data_base_receipt_instance.to_dict()
# create an instance of InvoiceDataBaseReceipt from a dict
invoice_data_base_receipt_form_dict = invoice_data_base_receipt.from_dict(invoice_data_base_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


