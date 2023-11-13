# SharedLinkPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[SharedLinkEntry]**](SharedLinkEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.shared_link_paging_list import SharedLinkPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkPagingList from a JSON string
shared_link_paging_list_instance = SharedLinkPagingList.from_json(json)
# print the JSON string representation of the object
print SharedLinkPagingList.to_json()

# convert the object into a dict
shared_link_paging_list_dict = shared_link_paging_list_instance.to_dict()
# create an instance of SharedLinkPagingList from a dict
shared_link_paging_list_form_dict = shared_link_paging_list.from_dict(shared_link_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


