# UpdateOnChainAutomatedTransferSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_target_block** | **float** | How many blocks should the fee rate calculation target to confirm in. Set to 1 if not provided | [optional] 
**interval_seconds** | **object** |  | [optional] 
**threshold** | **decimal.Decimal** | Only process payouts when this payout sum is reached. | [optional] 
**process_new_payouts_instantly** | **bool** | Skip the interval when ane eligible payout has been approved (or created with pre-approval) | [optional] [default to False]

## Example

```python
from openapi_client.models.update_on_chain_automated_transfer_settings import UpdateOnChainAutomatedTransferSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOnChainAutomatedTransferSettings from a JSON string
update_on_chain_automated_transfer_settings_instance = UpdateOnChainAutomatedTransferSettings.from_json(json)
# print the JSON string representation of the object
print UpdateOnChainAutomatedTransferSettings.to_json()

# convert the object into a dict
update_on_chain_automated_transfer_settings_dict = update_on_chain_automated_transfer_settings_instance.to_dict()
# create an instance of UpdateOnChainAutomatedTransferSettings from a dict
update_on_chain_automated_transfer_settings_form_dict = update_on_chain_automated_transfer_settings.from_dict(update_on_chain_automated_transfer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


