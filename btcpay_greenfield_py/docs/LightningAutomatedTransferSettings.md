# LightningAutomatedTransferSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**interval_seconds** | **object** |  | [optional] 
**cancel_payout_after_failures** | **float** | How many failures should the processor tolerate before cancelling the payout | [optional] 
**process_new_payouts_instantly** | **bool** | Skip the interval when ane eligible payout has been approved (or created with pre-approval) | [optional] [default to False]

## Example

```python
from openapi_client.models.lightning_automated_transfer_settings import LightningAutomatedTransferSettings

# TODO update the JSON string below
json = "{}"
# create an instance of LightningAutomatedTransferSettings from a JSON string
lightning_automated_transfer_settings_instance = LightningAutomatedTransferSettings.from_json(json)
# print the JSON string representation of the object
print LightningAutomatedTransferSettings.to_json()

# convert the object into a dict
lightning_automated_transfer_settings_dict = lightning_automated_transfer_settings_instance.to_dict()
# create an instance of LightningAutomatedTransferSettings from a dict
lightning_automated_transfer_settings_form_dict = lightning_automated_transfer_settings.from_dict(lightning_automated_transfer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


