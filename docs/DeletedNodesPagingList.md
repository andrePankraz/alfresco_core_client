# DeletedNodesPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**entries** | [**List[DeletedNodeEntry]**](DeletedNodeEntry.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.deleted_nodes_paging_list import DeletedNodesPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedNodesPagingList from a JSON string
deleted_nodes_paging_list_instance = DeletedNodesPagingList.from_json(json)
# print the JSON string representation of the object
print DeletedNodesPagingList.to_json()

# convert the object into a dict
deleted_nodes_paging_list_dict = deleted_nodes_paging_list_instance.to_dict()
# create an instance of DeletedNodesPagingList from a dict
deleted_nodes_paging_list_form_dict = deleted_nodes_paging_list.from_dict(deleted_nodes_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


