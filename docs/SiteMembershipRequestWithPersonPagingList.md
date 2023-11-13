# SiteMembershipRequestWithPersonPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**entries** | [**List[SiteMembershipRequestWithPersonEntry]**](SiteMembershipRequestWithPersonEntry.md) |  | 

## Example

```python
from alfresco_core_api_client.models.site_membership_request_with_person_paging_list import SiteMembershipRequestWithPersonPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestWithPersonPagingList from a JSON string
site_membership_request_with_person_paging_list_instance = SiteMembershipRequestWithPersonPagingList.from_json(json)
# print the JSON string representation of the object
print SiteMembershipRequestWithPersonPagingList.to_json()

# convert the object into a dict
site_membership_request_with_person_paging_list_dict = site_membership_request_with_person_paging_list_instance.to_dict()
# create an instance of SiteMembershipRequestWithPersonPagingList from a dict
site_membership_request_with_person_paging_list_form_dict = site_membership_request_with_person_paging_list.from_dict(site_membership_request_with_person_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


