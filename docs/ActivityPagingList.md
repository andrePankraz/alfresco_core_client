# ActivityPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[ActivityEntry]**](ActivityEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.activity_paging_list import ActivityPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPagingList from a JSON string
activity_paging_list_instance = ActivityPagingList.from_json(json)
# print the JSON string representation of the object
print ActivityPagingList.to_json()

# convert the object into a dict
activity_paging_list_dict = activity_paging_list_instance.to_dict()
# create an instance of ActivityPagingList from a dict
activity_paging_list_form_dict = activity_paging_list.from_dict(activity_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


