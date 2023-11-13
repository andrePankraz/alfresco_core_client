# NodeBodyMove


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_parent_id** | **str** |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | [optional] 

## Example

```python
from alfresco_core_api_client.models.node_body_move import NodeBodyMove

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBodyMove from a JSON string
node_body_move_instance = NodeBodyMove.from_json(json)
# print the JSON string representation of the object
print NodeBodyMove.to_json()

# convert the object into a dict
node_body_move_dict = node_body_move_instance.to_dict()
# create an instance of NodeBodyMove from a dict
node_body_move_form_dict = node_body_move.from_dict(node_body_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


