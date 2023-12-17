# OnChainAutomatedTransferSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**fee_target_block** | **float** | How many blocks should the fee rate calculation target to confirm in. | [optional] 
**interval_seconds** | **object** |  | [optional] 
**threshold** | **decimal.Decimal** | Only process payouts when this payout sum is reached. | [optional] 
**process_new_payouts_instantly** | **bool** | Skip the interval when ane eligible payout has been approved (or created with pre-approval) | [optional] [default to False]

## Example

```python
from openapi_client.models.on_chain_automated_transfer_settings import OnChainAutomatedTransferSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OnChainAutomatedTransferSettings from a JSON string
on_chain_automated_transfer_settings_instance = OnChainAutomatedTransferSettings.from_json(json)
# print the JSON string representation of the object
print OnChainAutomatedTransferSettings.to_json()

# convert the object into a dict
on_chain_automated_transfer_settings_dict = on_chain_automated_transfer_settings_instance.to_dict()
# create an instance of OnChainAutomatedTransferSettings from a dict
on_chain_automated_transfer_settings_form_dict = on_chain_automated_transfer_settings.from_dict(on_chain_automated_transfer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


