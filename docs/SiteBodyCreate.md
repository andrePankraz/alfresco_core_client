# SiteBodyCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | [default to 'PUBLIC']

## Example

```python
from alfresco_core_api_client.models.site_body_create import SiteBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBodyCreate from a JSON string
site_body_create_instance = SiteBodyCreate.from_json(json)
# print the JSON string representation of the object
print SiteBodyCreate.to_json()

# convert the object into a dict
site_body_create_dict = site_body_create_instance.to_dict()
# create an instance of SiteBodyCreate from a dict
site_body_create_form_dict = site_body_create.from_dict(site_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


