# CategoryLinkBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The identifier of the category. | 

## Example

```python
from alfresco_core_api_client.models.category_link_body import CategoryLinkBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryLinkBody from a JSON string
category_link_body_instance = CategoryLinkBody.from_json(json)
# print the JSON string representation of the object
print CategoryLinkBody.to_json()

# convert the object into a dict
category_link_body_dict = category_link_body_instance.to_dict()
# create an instance of CategoryLinkBody from a dict
category_link_body_form_dict = category_link_body.from_dict(category_link_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


