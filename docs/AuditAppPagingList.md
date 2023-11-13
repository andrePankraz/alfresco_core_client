# AuditAppPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**entries** | [**List[AuditAppEntry]**](AuditAppEntry.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.audit_app_paging_list import AuditAppPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of AuditAppPagingList from a JSON string
audit_app_paging_list_instance = AuditAppPagingList.from_json(json)
# print the JSON string representation of the object
print AuditAppPagingList.to_json()

# convert the object into a dict
audit_app_paging_list_dict = audit_app_paging_list_instance.to_dict()
# create an instance of AuditAppPagingList from a dict
audit_app_paging_list_form_dict = audit_app_paging_list.from_dict(audit_app_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


