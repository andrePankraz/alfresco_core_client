# TagPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[TagEntry]**](TagEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.tag_paging_list import TagPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of TagPagingList from a JSON string
tag_paging_list_instance = TagPagingList.from_json(json)
# print the JSON string representation of the object
print TagPagingList.to_json()

# convert the object into a dict
tag_paging_list_dict = tag_paging_list_instance.to_dict()
# create an instance of TagPagingList from a dict
tag_paging_list_form_dict = tag_paging_list.from_dict(tag_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


