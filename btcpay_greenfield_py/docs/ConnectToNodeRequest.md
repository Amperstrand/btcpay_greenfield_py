# ConnectToNodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_uri** | **str** | Node URI in the form &#x60;pubkey@endpoint[:port]&#x60; | [optional] 

## Example

```python
from btcpay_greenfield_py.models.connect_to_node_request import ConnectToNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectToNodeRequest from a JSON string
connect_to_node_request_instance = ConnectToNodeRequest.from_json(json)
# print the JSON string representation of the object
print ConnectToNodeRequest.to_json()

# convert the object into a dict
connect_to_node_request_dict = connect_to_node_request_instance.to_dict()
# create an instance of ConnectToNodeRequest from a dict
connect_to_node_request_form_dict = connect_to_node_request.from_dict(connect_to_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


