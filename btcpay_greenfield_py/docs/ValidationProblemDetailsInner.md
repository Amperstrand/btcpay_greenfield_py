# ValidationProblemDetailsInner

A specific validation error on a json property

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The json path of the property which failed validation | [optional] 
**message** | **str** | User friendly error message about the validation | [optional] 

## Example

```python
from btcpay_greenfield_py.models.validation_problem_details_inner import ValidationProblemDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationProblemDetailsInner from a JSON string
validation_problem_details_inner_instance = ValidationProblemDetailsInner.from_json(json)
# print the JSON string representation of the object
print ValidationProblemDetailsInner.to_json()

# convert the object into a dict
validation_problem_details_inner_dict = validation_problem_details_inner_instance.to_dict()
# create an instance of ValidationProblemDetailsInner from a dict
validation_problem_details_inner_form_dict = validation_problem_details_inner.from_dict(validation_problem_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


