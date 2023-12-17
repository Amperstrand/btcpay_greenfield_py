# CreateCrowdfundAppRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | The name of the app (shown in admin UI) | [optional] 
**title** | **str** | The title of the app (shown to the user) | [optional] 
**description** | **str** | The description of the app (shown to the user) | [optional] 
**enabled** | **bool** | Determines if the app is enabled to be viewed by everyone | [optional] [default to True]
**enforce_target_amount** | **bool** | Will not allow contributions over the set target amount | [optional] [default to False]
**start_date** | **float** | A unix timestamp in seconds | [optional] 
**end_date** | **float** | A unix timestamp in seconds | [optional] 
**target_currency** | **str** | Target currency for the crowdfund. Defaults to the currency used by the store if not specified | [optional] 
**target_amount** | **float** | Target amount for the crowdfund | [optional] 
**custom_css_link** | **str** | Link to a custom CSS stylesheet to be used in the app | [optional] 
**main_image_url** | **str** | URL for image to be used as a cover image for the app | [optional] 
**embedded_css** | **str** | Custom CSS to embed into the app | [optional] 
**perks_template** | **str** | YAML template of perks available in the app | [optional] 
**notification_url** | **str** | Callback notification url to POST to once when invoice is paid for and once when there are enough blockchain confirmations | [optional] 
**tagline** | **str** | Tagline for the app (shown to the user) | [optional] 
**disqus_shortname** | **str** | Disqus shortname to used for the app. Enables Disqus functionality if set. | [optional] 
**sounds_enabled** | **bool** | Enables sounds on new contributions if set to true | [optional] [default to False]
**animations_enabled** | **bool** | Enables background animations on new contributions if set to true | [optional] [default to False]
**reset_every_amount** | **float** | Contribution goal reset frequency amount. Must be used in conjunction with resetEvery and startDate. | [optional] [default to 1]
**reset_every** | **str** | Contribution goal reset frequency. Must be used in conjunction with resetEveryAmount and startDate. | [optional] [default to 'Never']
**display_perks_value** | **bool** | Displays values of perks if set to true | [optional] [default to False]
**sort_perks_by_popularity** | **bool** | Sorts perks by popularity if set to true | [optional] [default to False]
**sounds** | **List[str]** | Array of custom sounds to use on new contributions | [optional] 
**animation_colors** | **List[str]** | Array of custom HEX colors to use for background animations on new contributions | [optional] 

## Example

```python
from openapi_client.models.create_crowdfund_app_request import CreateCrowdfundAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCrowdfundAppRequest from a JSON string
create_crowdfund_app_request_instance = CreateCrowdfundAppRequest.from_json(json)
# print the JSON string representation of the object
print CreateCrowdfundAppRequest.to_json()

# convert the object into a dict
create_crowdfund_app_request_dict = create_crowdfund_app_request_instance.to_dict()
# create an instance of CreateCrowdfundAppRequest from a dict
create_crowdfund_app_request_form_dict = create_crowdfund_app_request.from_dict(create_crowdfund_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


