# MarkInvoiceStatusRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**InvoiceStatusMark**](InvoiceStatusMark.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.mark_invoice_status_request import MarkInvoiceStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkInvoiceStatusRequest from a JSON string
mark_invoice_status_request_instance = MarkInvoiceStatusRequest.from_json(json)
# print the JSON string representation of the object
print MarkInvoiceStatusRequest.to_json()

# convert the object into a dict
mark_invoice_status_request_dict = mark_invoice_status_request_instance.to_dict()
# create an instance of MarkInvoiceStatusRequest from a dict
mark_invoice_status_request_form_dict = mark_invoice_status_request.from_dict(mark_invoice_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


