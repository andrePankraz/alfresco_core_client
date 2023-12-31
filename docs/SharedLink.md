# SharedLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**node_id** | **str** |  | [optional] 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**shared_by_user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**allowable_operations** | **List[str]** | The allowable operations for the Quickshare link itself. See allowableOperationsOnTarget for the allowable operations pertaining to the linked content node.  | [optional] 
**allowable_operations_on_target** | **List[str]** | The allowable operations for the content node being shared.  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**properties** | **object** | A subset of the target node&#39;s properties, system properties and properties already available in the SharedLink are excluded.  | [optional] 
**aspect_names** | **List[str]** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.shared_link import SharedLink

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLink from a JSON string
shared_link_instance = SharedLink.from_json(json)
# print the JSON string representation of the object
print SharedLink.to_json()

# convert the object into a dict
shared_link_dict = shared_link_instance.to_dict()
# create an instance of SharedLink from a dict
shared_link_form_dict = shared_link.from_dict(shared_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


