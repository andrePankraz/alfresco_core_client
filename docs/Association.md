# Association


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** |  | 
**assoc_type** | **str** |  | 

## Example

```python
from alfresco_core_api_client.models.association import Association

# TODO update the JSON string below
json = "{}"
# create an instance of Association from a JSON string
association_instance = Association.from_json(json)
# print the JSON string representation of the object
print Association.to_json()

# convert the object into a dict
association_dict = association_instance.to_dict()
# create an instance of Association from a dict
association_form_dict = association.from_dict(association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


