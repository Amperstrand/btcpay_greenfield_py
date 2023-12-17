# PullPaymentsApprovePayoutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | The revision number of the payout being modified | [optional] 
**rate_rule** | **str** | The rate rule to calculate the rate of the payout. This can also be a fixed decimal. (if null or unspecified, will use the same rate setting as the store&#39;s settings) | [optional] 

## Example

```python
from openapi_client.models.pull_payments_approve_payout_request import PullPaymentsApprovePayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullPaymentsApprovePayoutRequest from a JSON string
pull_payments_approve_payout_request_instance = PullPaymentsApprovePayoutRequest.from_json(json)
# print the JSON string representation of the object
print PullPaymentsApprovePayoutRequest.to_json()

# convert the object into a dict
pull_payments_approve_payout_request_dict = pull_payments_approve_payout_request_instance.to_dict()
# create an instance of PullPaymentsApprovePayoutRequest from a dict
pull_payments_approve_payout_request_form_dict = pull_payments_approve_payout_request.from_dict(pull_payments_approve_payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


