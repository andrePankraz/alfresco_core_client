# VersionPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**entries** | [**List[VersionEntry]**](VersionEntry.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.version_paging_list import VersionPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of VersionPagingList from a JSON string
version_paging_list_instance = VersionPagingList.from_json(json)
# print the JSON string representation of the object
print VersionPagingList.to_json()

# convert the object into a dict
version_paging_list_dict = version_paging_list_instance.to_dict()
# create an instance of VersionPagingList from a dict
version_paging_list_form_dict = version_paging_list.from_dict(version_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


