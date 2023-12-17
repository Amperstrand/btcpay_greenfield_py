# LightningPaymentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The payment&#39;s ID | [optional] 
**status** | [**LightningPaymentStatus**](LightningPaymentStatus.md) |  | [optional] 
**bolt11** | **str** | The BOLT11 representation of the payment | [optional] 
**payment_hash** | **str** | The payment hash | [optional] 
**preimage** | **str** | The payment preimage (available when status is complete) | [optional] 
**created_at** | **float** | A unix timestamp in seconds | [optional] 
**total_amount** | **str** | The total amount (including fees) in millisatoshi | [optional] 
**fee_amount** | **str** | The total fees in millisatoshi | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lightning_payment_data import LightningPaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningPaymentData from a JSON string
lightning_payment_data_instance = LightningPaymentData.from_json(json)
# print the JSON string representation of the object
print LightningPaymentData.to_json()

# convert the object into a dict
lightning_payment_data_dict = lightning_payment_data_instance.to_dict()
# create an instance of LightningPaymentData from a dict
lightning_payment_data_form_dict = lightning_payment_data.from_dict(lightning_payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


