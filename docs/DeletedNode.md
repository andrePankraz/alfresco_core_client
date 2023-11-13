# DeletedNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**is_folder** | **bool** |  | 
**is_file** | **bool** |  | 
**is_locked** | **bool** |  | [optional] [default to False]
**modified_at** | **datetime** |  | 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | 
**created_at** | **datetime** |  | 
**created_by_user** | [**UserInfo**](UserInfo.md) |  | 
**parent_id** | **str** |  | [optional] 
**is_link** | **bool** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**is_direct_link_enabled** | **bool** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**aspect_names** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 
**allowable_operations** | **List[str]** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 
**permissions** | [**PermissionsInfo**](PermissionsInfo.md) |  | [optional] 
**definition** | [**Definition**](Definition.md) |  | [optional] 
**archived_by_user** | [**UserInfo**](UserInfo.md) |  | 
**archived_at** | **datetime** |  | 

## Example

```python
from alfresco_core_api_client.models.deleted_node import DeletedNode

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedNode from a JSON string
deleted_node_instance = DeletedNode.from_json(json)
# print the JSON string representation of the object
print DeletedNode.to_json()

# convert the object into a dict
deleted_node_dict = deleted_node_instance.to_dict()
# create an instance of DeletedNode from a dict
deleted_node_form_dict = deleted_node.from_dict(deleted_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


