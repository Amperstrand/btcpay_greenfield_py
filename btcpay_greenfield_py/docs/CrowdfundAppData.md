# CrowdfundAppData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the app | [optional] 
**name** | **str** | Name given to the app when it was created | [optional] 
**store_id** | **str** | Id of the store to which the app belongs | [optional] 
**created** | **int** | UNIX timestamp for when the app was created | [optional] 
**app_type** | **str** | Type of the app which was created | [optional] 
**archived** | **bool** | If true, the app does not appear in the apps list by default. | [optional] [default to False]
**title** | **str** | Display title of the app | [optional] 
**description** | **str** | App description | [optional] 
**enabled** | **bool** | Whether the app is enabled to be viewed by everyone | [optional] 
**enforce_target_amount** | **bool** | Whether contributions over the set target amount are allowed | [optional] 
**start_date** | **float** | A unix timestamp in seconds | [optional] 
**end_date** | **float** | A unix timestamp in seconds | [optional] 
**target_currency** | **str** | Target currency for the crowdfund | [optional] 
**target_amount** | **float** | Target amount for the crowdfund | [optional] 
**custom_css_link** | **str** | Link to a custom CSS stylesheet to be used in the app | [optional] 
**main_image_url** | **str** | URL for image used as a cover image for the app | [optional] 
**embedded_css** | **str** | Custom CSS embedded into the app | [optional] 
**perks** | **object** | JSON of perks available in the app | [optional] 
**notification_url** | **str** | Callback notification url to POST to once when invoice is paid for and once when there are enough blockchain confirmations | [optional] 
**tagline** | **str** | Tagline for the app displayed to user | [optional] 
**disqus_enabled** | **bool** | Whether Disqus is enabled for the app | [optional] 
**disqus_shortname** | **str** | Disqus shortname to used for the app | [optional] 
**sounds_enabled** | **bool** | Whether sounds on new contributions are enabled | [optional] 
**animations_enabled** | **bool** | Whether background animations on new contributions are enabled | [optional] 
**reset_every_amount** | **float** | Contribution goal reset frequency amount | [optional] 
**reset_every** | **str** | Contribution goal reset frequency | [optional] 
**display_perks_value** | **bool** | Whether perk values are displayed | [optional] 
**sort_perks_by_popularity** | **bool** | Whether perks are sorted by popularity | [optional] [default to True]
**sounds** | **List[str]** | Array of custom sounds which can be used on new contributions | [optional] 
**animation_colors** | **List[str]** | Array of custom HEX colors which can be used for background animations on new contributions | [optional] 

## Example

```python
from openapi_client.models.crowdfund_app_data import CrowdfundAppData

# TODO update the JSON string below
json = "{}"
# create an instance of CrowdfundAppData from a JSON string
crowdfund_app_data_instance = CrowdfundAppData.from_json(json)
# print the JSON string representation of the object
print CrowdfundAppData.to_json()

# convert the object into a dict
crowdfund_app_data_dict = crowdfund_app_data_instance.to_dict()
# create an instance of CrowdfundAppData from a dict
crowdfund_app_data_form_dict = crowdfund_app_data.from_dict(crowdfund_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


