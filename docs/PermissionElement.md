# PermissionElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**access_status** | **str** |  | [optional] [default to 'ALLOWED']

## Example

```python
from alfresco_core_api_client.models.permission_element import PermissionElement

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionElement from a JSON string
permission_element_instance = PermissionElement.from_json(json)
# print the JSON string representation of the object
print PermissionElement.to_json()

# convert the object into a dict
permission_element_dict = permission_element_instance.to_dict()
# create an instance of PermissionElement from a dict
permission_element_form_dict = permission_element.from_dict(permission_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


