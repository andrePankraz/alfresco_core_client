# CategoryPaging


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**CategoryPagingList**](CategoryPagingList.md) |  | 

## Example

```python
from alfresco_core_api_client.models.category_paging import CategoryPaging

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryPaging from a JSON string
category_paging_instance = CategoryPaging.from_json(json)
# print the JSON string representation of the object
print CategoryPaging.to_json()

# convert the object into a dict
category_paging_dict = category_paging_instance.to_dict()
# create an instance of CategoryPaging from a dict
category_paging_form_dict = category_paging.from_dict(category_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


