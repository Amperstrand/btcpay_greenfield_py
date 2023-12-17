# LightningAddressData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username of the lightning address | [optional] 
**currency_code** | **str** | The currency to generate the invoices for this lightning address in. Leave null lto use the store default. | [optional] 
**min** | **str** | The minimum amount in sats this ln address allows | [optional] 
**max** | **str** | The maximum amount in sats this ln address allows | [optional] 

## Example

```python
from btcpay_greenfield_py.models.lightning_address_data import LightningAddressData

# TODO update the JSON string below
json = "{}"
# create an instance of LightningAddressData from a JSON string
lightning_address_data_instance = LightningAddressData.from_json(json)
# print the JSON string representation of the object
print LightningAddressData.to_json()

# convert the object into a dict
lightning_address_data_dict = lightning_address_data_instance.to_dict()
# create an instance of LightningAddressData from a dict
lightning_address_data_form_dict = lightning_address_data.from_dict(lightning_address_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


