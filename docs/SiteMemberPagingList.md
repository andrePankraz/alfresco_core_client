# SiteMemberPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[SiteMemberEntry]**](SiteMemberEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.site_member_paging_list import SiteMemberPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMemberPagingList from a JSON string
site_member_paging_list_instance = SiteMemberPagingList.from_json(json)
# print the JSON string representation of the object
print SiteMemberPagingList.to_json()

# convert the object into a dict
site_member_paging_list_dict = site_member_paging_list_instance.to_dict()
# create an instance of SiteMemberPagingList from a dict
site_member_paging_list_form_dict = site_member_paging_list.from_dict(site_member_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


