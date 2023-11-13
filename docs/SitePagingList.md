# SitePagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[SiteEntry]**](SiteEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.site_paging_list import SitePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SitePagingList from a JSON string
site_paging_list_instance = SitePagingList.from_json(json)
# print the JSON string representation of the object
print SitePagingList.to_json()

# convert the object into a dict
site_paging_list_dict = site_paging_list_instance.to_dict()
# create an instance of SitePagingList from a dict
site_paging_list_form_dict = site_paging_list.from_dict(site_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


