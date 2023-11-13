# SiteGroupPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[SiteGroupEntry]**](SiteGroupEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.site_group_paging_list import SiteGroupPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteGroupPagingList from a JSON string
site_group_paging_list_instance = SiteGroupPagingList.from_json(json)
# print the JSON string representation of the object
print SiteGroupPagingList.to_json()

# convert the object into a dict
site_group_paging_list_dict = site_group_paging_list_instance.to_dict()
# create an instance of SiteGroupPagingList from a dict
site_group_paging_list_form_dict = site_group_paging_list.from_dict(site_group_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


