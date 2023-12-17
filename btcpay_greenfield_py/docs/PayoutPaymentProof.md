# PayoutPaymentProof

Additional information around how the payout is being or has been paid out. The mentioned properties are all optional (except `proofType`) and you can introduce any json format you wish.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proof_type** | **str** | The type of payment proof it is. | [optional] 

## Example

```python
from btcpay_greenfield_py.models.payout_payment_proof import PayoutPaymentProof

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutPaymentProof from a JSON string
payout_payment_proof_instance = PayoutPaymentProof.from_json(json)
# print the JSON string representation of the object
print PayoutPaymentProof.to_json()

# convert the object into a dict
payout_payment_proof_dict = payout_payment_proof_instance.to_dict()
# create an instance of PayoutPaymentProof from a dict
payout_payment_proof_form_dict = payout_payment_proof.from_dict(payout_payment_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


