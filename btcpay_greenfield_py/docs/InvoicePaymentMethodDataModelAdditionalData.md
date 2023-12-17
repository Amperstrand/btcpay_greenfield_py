# InvoicePaymentMethodDataModelAdditionalData

Additional data provided by the payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provided_comment** | **str** | The provided comment to a LNUrl payment with comments enabled | [optional] 
**consumed_lightning_address** | **str** | The consumed lightning address of a LN Address payment | [optional] 

## Example

```python
from openapi_client.models.invoice_payment_method_data_model_additional_data import InvoicePaymentMethodDataModelAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePaymentMethodDataModelAdditionalData from a JSON string
invoice_payment_method_data_model_additional_data_instance = InvoicePaymentMethodDataModelAdditionalData.from_json(json)
# print the JSON string representation of the object
print InvoicePaymentMethodDataModelAdditionalData.to_json()

# convert the object into a dict
invoice_payment_method_data_model_additional_data_dict = invoice_payment_method_data_model_additional_data_instance.to_dict()
# create an instance of InvoicePaymentMethodDataModelAdditionalData from a dict
invoice_payment_method_data_model_additional_data_form_dict = invoice_payment_method_data_model_additional_data.from_dict(invoice_payment_method_data_model_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


