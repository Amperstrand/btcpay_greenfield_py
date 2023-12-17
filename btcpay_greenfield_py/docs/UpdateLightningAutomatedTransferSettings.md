# UpdateLightningAutomatedTransferSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_seconds** | **object** |  | [optional] 
**cancel_payout_after_failures** | **float** | How many failures should the processor tolerate before cancelling the payout | [optional] 
**process_new_payouts_instantly** | **bool** | Skip the interval when ane eligible payout has been approved (or created with pre-approval) | [optional] [default to False]

## Example

```python
from openapi_client.models.update_lightning_automated_transfer_settings import UpdateLightningAutomatedTransferSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLightningAutomatedTransferSettings from a JSON string
update_lightning_automated_transfer_settings_instance = UpdateLightningAutomatedTransferSettings.from_json(json)
# print the JSON string representation of the object
print UpdateLightningAutomatedTransferSettings.to_json()

# convert the object into a dict
update_lightning_automated_transfer_settings_dict = update_lightning_automated_transfer_settings_instance.to_dict()
# create an instance of UpdateLightningAutomatedTransferSettings from a dict
update_lightning_automated_transfer_settings_form_dict = update_lightning_automated_transfer_settings.from_dict(update_lightning_automated_transfer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


