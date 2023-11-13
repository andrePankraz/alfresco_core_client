# Category


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier for the category. | 
**name** | **str** | The name of the category.  This must be unique within the parent category.  | 
**parent_id** | **str** | The id of the parent category (or -root- if this is a top level category). | [optional] 
**has_children** | **bool** | True if the category has at least one child category. | [optional] 
**count** | **float** | The number of nodes that are assigned to this category. | [optional] 
**path** | **str** | The path to this category. | [optional] 

## Example

```python
from alfresco_core_api_client.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print Category.to_json()

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_form_dict = category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


