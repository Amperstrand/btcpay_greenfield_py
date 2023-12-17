# CreateInvoiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InvoiceMetadata**](InvoiceMetadata.md) |  | [optional] 
**checkout** | [**InvoiceDataBaseCheckout**](InvoiceDataBaseCheckout.md) |  | [optional] 
**receipt** | [**InvoiceDataBaseReceipt**](InvoiceDataBaseReceipt.md) |  | [optional] 
**amount** | **decimal.Decimal** | The amount of the invoice. If null or unspecified, the invoice will be a top-up invoice. (ie. The invoice will consider any payment as a full payment) | [optional] 
**currency** | **str** | The currency of the invoice (if null, empty or unspecified, the currency will be the store&#39;s settings default)&#39; | [optional] 
**additional_search_terms** | **List[str]** | Additional search term to help you find this invoice via text search | [optional] 

## Example

```python
from btcpay_greenfield_py.models.create_invoice_request import CreateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequest from a JSON string
create_invoice_request_instance = CreateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print CreateInvoiceRequest.to_json()

# convert the object into a dict
create_invoice_request_dict = create_invoice_request_instance.to_dict()
# create an instance of CreateInvoiceRequest from a dict
create_invoice_request_form_dict = create_invoice_request.from_dict(create_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


