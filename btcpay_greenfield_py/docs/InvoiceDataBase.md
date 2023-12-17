# InvoiceDataBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InvoiceMetadata**](InvoiceMetadata.md) |  | [optional] 
**checkout** | [**InvoiceDataBaseCheckout**](InvoiceDataBaseCheckout.md) |  | [optional] 
**receipt** | [**InvoiceDataBaseReceipt**](InvoiceDataBaseReceipt.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_data_base import InvoiceDataBase

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDataBase from a JSON string
invoice_data_base_instance = InvoiceDataBase.from_json(json)
# print the JSON string representation of the object
print InvoiceDataBase.to_json()

# convert the object into a dict
invoice_data_base_dict = invoice_data_base_instance.to_dict()
# create an instance of InvoiceDataBase from a dict
invoice_data_base_form_dict = invoice_data_base.from_dict(invoice_data_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


