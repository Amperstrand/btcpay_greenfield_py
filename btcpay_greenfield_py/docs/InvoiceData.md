# InvoiceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InvoiceMetadata**](InvoiceMetadata.md) |  | [optional] 
**checkout** | [**InvoiceDataBaseCheckout**](InvoiceDataBaseCheckout.md) |  | [optional] 
**receipt** | [**InvoiceDataBaseReceipt**](InvoiceDataBaseReceipt.md) |  | [optional] 
**id** | **str** | The identifier of the invoice | [optional] 
**store_id** | **str** | The store identifier that the invoice belongs to | [optional] 
**amount** | **decimal.Decimal** | The amount of the invoice. Note that the amount will be zero for a top-up invoice that is paid after invoice expiry. | [optional] 
**currency** | **str** | The currency of the invoice | [optional] 
**type** | [**InvoiceType**](InvoiceType.md) |  | [optional] 
**checkout_link** | **str** | The link to the checkout page, where you can redirect the customer | [optional] 
**created_time** | **float** | A unix timestamp in seconds | [optional] 
**expiration_time** | **float** | A unix timestamp in seconds | [optional] 
**monitoring_expiration** | **float** | A unix timestamp in seconds | [optional] 
**status** | [**InvoiceStatus**](InvoiceStatus.md) |  | [optional] 
**additional_status** | [**InvoiceAdditionalStatus**](InvoiceAdditionalStatus.md) |  | [optional] 
**available_statuses_for_manual_marking** | [**List[InvoiceStatus]**](InvoiceStatus.md) | The statuses the invoice can be manually marked as | [optional] 
**archived** | **bool** | true if the invoice is archived | [optional] 

## Example

```python
from btcpay_greenfield_py.models.invoice_data import InvoiceData

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceData from a JSON string
invoice_data_instance = InvoiceData.from_json(json)
# print the JSON string representation of the object
print InvoiceData.to_json()

# convert the object into a dict
invoice_data_dict = invoice_data_instance.to_dict()
# create an instance of InvoiceData from a dict
invoice_data_form_dict = invoice_data.from_dict(invoice_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


