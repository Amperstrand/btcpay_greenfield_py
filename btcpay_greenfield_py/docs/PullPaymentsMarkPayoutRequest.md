# PullPaymentsMarkPayoutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**PayoutState**](PayoutState.md) |  | [optional] 
**payment_proof** | [**PayoutPaymentProof**](PayoutPaymentProof.md) |  | [optional] 

## Example

```python
from btcpay_greenfield_py.models.pull_payments_mark_payout_request import PullPaymentsMarkPayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullPaymentsMarkPayoutRequest from a JSON string
pull_payments_mark_payout_request_instance = PullPaymentsMarkPayoutRequest.from_json(json)
# print the JSON string representation of the object
print PullPaymentsMarkPayoutRequest.to_json()

# convert the object into a dict
pull_payments_mark_payout_request_dict = pull_payments_mark_payout_request_instance.to_dict()
# create an instance of PullPaymentsMarkPayoutRequest from a dict
pull_payments_mark_payout_request_form_dict = pull_payments_mark_payout_request.from_dict(pull_payments_mark_payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


