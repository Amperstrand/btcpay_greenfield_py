# CreateLightningInvoiceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount wrapped in a string, represented in a millistatoshi string. (1000 millisatoshi &#x3D; 1 satoshi) | [optional] 
**description** | **str** | Description of the invoice in the BOLT11 | [optional] 
**description_hash_only** | **bool** | If &#x60;descriptionHashOnly&#x60; is &#x60;true&#x60; (default is &#x60;false&#x60;), then the BOLT11 returned contains a hash of the &#x60;description&#x60;, rather than the &#x60;description&#x60;, itself. This allows for much longer descriptions, but they must be communicated via some other mechanism. | [optional] [default to False]
**expiry** | **object** |  | [optional] 
**private_route_hints** | **bool** | True if the invoice should include private route hints | [optional] [default to False]

## Example

```python
from btcpay_greenfield_py.models.create_lightning_invoice_request import CreateLightningInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLightningInvoiceRequest from a JSON string
create_lightning_invoice_request_instance = CreateLightningInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print CreateLightningInvoiceRequest.to_json()

# convert the object into a dict
create_lightning_invoice_request_dict = create_lightning_invoice_request_instance.to_dict()
# create an instance of CreateLightningInvoiceRequest from a dict
create_lightning_invoice_request_form_dict = create_lightning_invoice_request.from_dict(create_lightning_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


