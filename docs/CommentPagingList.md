# CommentPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[CommentEntry]**](CommentEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.comment_paging_list import CommentPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of CommentPagingList from a JSON string
comment_paging_list_instance = CommentPagingList.from_json(json)
# print the JSON string representation of the object
print CommentPagingList.to_json()

# convert the object into a dict
comment_paging_list_dict = comment_paging_list_instance.to_dict()
# create an instance of CommentPagingList from a dict
comment_paging_list_form_dict = comment_paging_list.from_dict(comment_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


