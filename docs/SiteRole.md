# SiteRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site** | [**Site**](Site.md) |  | 
**id** | **str** |  | 
**guid** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from alfresco_core_api_client.models.site_role import SiteRole

# TODO update the JSON string below
json = "{}"
# create an instance of SiteRole from a JSON string
site_role_instance = SiteRole.from_json(json)
# print the JSON string representation of the object
print SiteRole.to_json()

# convert the object into a dict
site_role_dict = site_role_instance.to_dict()
# create an instance of SiteRole from a dict
site_role_form_dict = site_role.from_dict(site_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


