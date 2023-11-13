# AuditEntryPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**entries** | [**List[AuditEntryEntry]**](AuditEntryEntry.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.audit_entry_paging_list import AuditEntryPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntryPagingList from a JSON string
audit_entry_paging_list_instance = AuditEntryPagingList.from_json(json)
# print the JSON string representation of the object
print AuditEntryPagingList.to_json()

# convert the object into a dict
audit_entry_paging_list_dict = audit_entry_paging_list_instance.to_dict()
# create an instance of AuditEntryPagingList from a dict
audit_entry_paging_list_form_dict = audit_entry_paging_list.from_dict(audit_entry_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


