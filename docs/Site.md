# Site


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**guid** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | 
**preset** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print Site.to_json()

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_form_dict = site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


