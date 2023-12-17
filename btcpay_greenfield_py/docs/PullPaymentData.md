# PullPaymentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the pull payment | [optional] 
**name** | **str** | Name given to pull payment when it was created | [optional] 
**description** | **str** | Description given to pull payment when it was created | [optional] 
**currency** | **str** | The currency of the pull payment&#39;s amount | [optional] 
**amount** | **decimal.Decimal** | The amount in the currency of this pull payment as a decimal string | [optional] 
**period** | **int** | The length of each period in seconds | [optional] 
**bolt11_expiration** | **str** | If lightning is activated, do not accept BOLT11 invoices with expiration less than … days | [optional] 
**auto_approve_claims** | **bool** | Any payouts created for this pull payment will skip the approval phase upon creation | [optional] [default to False]
**archived** | **bool** | Whether this pull payment is archived | [optional] 
**view_link** | **str** | The link to a page to claim payouts to this pull payment | [optional] 

## Example

```python
from btcpay_greenfield_py.models.pull_payment_data import PullPaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of PullPaymentData from a JSON string
pull_payment_data_instance = PullPaymentData.from_json(json)
# print the JSON string representation of the object
print PullPaymentData.to_json()

# convert the object into a dict
pull_payment_data_dict = pull_payment_data_instance.to_dict()
# create an instance of PullPaymentData from a dict
pull_payment_data_form_dict = pull_payment_data.from_dict(pull_payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


