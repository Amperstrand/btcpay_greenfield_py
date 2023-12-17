# PaymentMethodCriteriaData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**currency_code** | **str** | The currency | [optional] [default to 'USD']
**amount** | **decimal.Decimal** | The amount | [optional] 
**above** | **bool** | If the criterion is for above or below the amount | [optional] [default to False]

## Example

```python
from openapi_client.models.payment_method_criteria_data import PaymentMethodCriteriaData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCriteriaData from a JSON string
payment_method_criteria_data_instance = PaymentMethodCriteriaData.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCriteriaData.to_json()

# convert the object into a dict
payment_method_criteria_data_dict = payment_method_criteria_data_instance.to_dict()
# create an instance of PaymentMethodCriteriaData from a dict
payment_method_criteria_data_form_dict = payment_method_criteria_data.from_dict(payment_method_criteria_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


