# SiteGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group** | [**GroupMember**](GroupMember.md) |  | 
**role** | **str** |  | 

## Example

```python
from alfresco_core_api_client.models.site_group import SiteGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SiteGroup from a JSON string
site_group_instance = SiteGroup.from_json(json)
# print the JSON string representation of the object
print SiteGroup.to_json()

# convert the object into a dict
site_group_dict = site_group_instance.to_dict()
# create an instance of SiteGroup from a dict
site_group_form_dict = site_group.from_dict(site_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


