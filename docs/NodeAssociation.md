# NodeAssociation


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
**association** | [**AssociationInfo**](AssociationInfo.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.node_association import NodeAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAssociation from a JSON string
node_association_instance = NodeAssociation.from_json(json)
# print the JSON string representation of the object
print NodeAssociation.to_json()

# convert the object into a dict
node_association_dict = node_association_instance.to_dict()
# create an instance of NodeAssociation from a dict
node_association_form_dict = node_association.from_dict(node_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


