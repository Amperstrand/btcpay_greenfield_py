# InvoiceMetadata

Additional information around the invoice that can be supplied. The mentioned properties are all optional and you can introduce any json format you wish. See [our documentation](https://docs.btcpayserver.org/Development/InvoiceMetadata/) for more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from btcpay_greenfield_py.models.invoice_metadata import InvoiceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceMetadata from a JSON string
invoice_metadata_instance = InvoiceMetadata.from_json(json)
# print the JSON string representation of the object
print InvoiceMetadata.to_json()

# convert the object into a dict
invoice_metadata_dict = invoice_metadata_instance.to_dict()
# create an instance of InvoiceMetadata from a dict
invoice_metadata_form_dict = invoice_metadata.from_dict(invoice_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


