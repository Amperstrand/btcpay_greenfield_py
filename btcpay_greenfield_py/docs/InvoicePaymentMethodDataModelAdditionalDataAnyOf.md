# InvoicePaymentMethodDataModelAdditionalDataAnyOf

LNURL Pay information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provided_comment** | **str** | The provided comment to a LNUrl payment with comments enabled | [optional] 
**consumed_lightning_address** | **str** | The consumed lightning address of a LN Address payment | [optional] 

## Example

```python
from openapi_client.models.invoice_payment_method_data_model_additional_data_any_of import InvoicePaymentMethodDataModelAdditionalDataAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePaymentMethodDataModelAdditionalDataAnyOf from a JSON string
invoice_payment_method_data_model_additional_data_any_of_instance = InvoicePaymentMethodDataModelAdditionalDataAnyOf.from_json(json)
# print the JSON string representation of the object
print InvoicePaymentMethodDataModelAdditionalDataAnyOf.to_json()

# convert the object into a dict
invoice_payment_method_data_model_additional_data_any_of_dict = invoice_payment_method_data_model_additional_data_any_of_instance.to_dict()
# create an instance of InvoicePaymentMethodDataModelAdditionalDataAnyOf from a dict
invoice_payment_method_data_model_additional_data_any_of_form_dict = invoice_payment_method_data_model_additional_data_any_of.from_dict(invoice_payment_method_data_model_additional_data_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


