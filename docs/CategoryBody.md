# CategoryBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the category.  This must be unique within the parent category.  | 

## Example

```python
from alfresco_core_api_client.models.category_body import CategoryBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryBody from a JSON string
category_body_instance = CategoryBody.from_json(json)
# print the JSON string representation of the object
print CategoryBody.to_json()

# convert the object into a dict
category_body_dict = category_body_instance.to_dict()
# create an instance of CategoryBody from a dict
category_body_form_dict = category_body.from_dict(category_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


