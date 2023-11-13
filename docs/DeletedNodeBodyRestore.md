# DeletedNodeBodyRestore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_parent_id** | **str** |  | [optional] 
**assoc_type** | **str** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.deleted_node_body_restore import DeletedNodeBodyRestore

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedNodeBodyRestore from a JSON string
deleted_node_body_restore_instance = DeletedNodeBodyRestore.from_json(json)
# print the JSON string representation of the object
print DeletedNodeBodyRestore.to_json()

# convert the object into a dict
deleted_node_body_restore_dict = deleted_node_body_restore_instance.to_dict()
# create an instance of DeletedNodeBodyRestore from a dict
deleted_node_body_restore_form_dict = deleted_node_body_restore.from_dict(deleted_node_body_restore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


