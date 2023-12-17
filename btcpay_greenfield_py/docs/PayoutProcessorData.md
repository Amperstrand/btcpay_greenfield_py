# PayoutProcessorData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | unique identifier of the payout processor | [optional] 
**friendly_name** | **str** | Human name of the payout processor | [optional] 
**payment_methods** | **List[str]** | Supported, payment methods by this processor | [optional] 

## Example

```python
from btcpay_greenfield_py.models.payout_processor_data import PayoutProcessorData

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutProcessorData from a JSON string
payout_processor_data_instance = PayoutProcessorData.from_json(json)
# print the JSON string representation of the object
print PayoutProcessorData.to_json()

# convert the object into a dict
payout_processor_data_dict = payout_processor_data_instance.to_dict()
# create an instance of PayoutProcessorData from a dict
payout_processor_data_form_dict = payout_processor_data.from_dict(payout_processor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


