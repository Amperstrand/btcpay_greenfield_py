# UpdateInvoiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InvoiceMetadata**](InvoiceMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_invoice_request import UpdateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoiceRequest from a JSON string
update_invoice_request_instance = UpdateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateInvoiceRequest.to_json()

# convert the object into a dict
update_invoice_request_dict = update_invoice_request_instance.to_dict()
# create an instance of UpdateInvoiceRequest from a dict
update_invoice_request_form_dict = update_invoice_request.from_dict(update_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


