# PreferencePagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[PreferenceEntry]**](PreferenceEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.preference_paging_list import PreferencePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of PreferencePagingList from a JSON string
preference_paging_list_instance = PreferencePagingList.from_json(json)
# print the JSON string representation of the object
print PreferencePagingList.to_json()

# convert the object into a dict
preference_paging_list_dict = preference_paging_list_instance.to_dict()
# create an instance of PreferencePagingList from a dict
preference_paging_list_form_dict = preference_paging_list.from_dict(preference_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


