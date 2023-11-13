# CategoryPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[CategoryEntry]**](CategoryEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.category_paging_list import CategoryPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryPagingList from a JSON string
category_paging_list_instance = CategoryPagingList.from_json(json)
# print the JSON string representation of the object
print CategoryPagingList.to_json()

# convert the object into a dict
category_paging_list_dict = category_paging_list_instance.to_dict()
# create an instance of CategoryPagingList from a dict
category_paging_list_form_dict = category_paging_list.from_dict(category_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


