# SiteMembershipRequestWithPerson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**site** | [**Site**](Site.md) |  | 
**person** | [**Person**](Person.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.site_membership_request_with_person import SiteMembershipRequestWithPerson

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestWithPerson from a JSON string
site_membership_request_with_person_instance = SiteMembershipRequestWithPerson.from_json(json)
# print the JSON string representation of the object
print SiteMembershipRequestWithPerson.to_json()

# convert the object into a dict
site_membership_request_with_person_dict = site_membership_request_with_person_instance.to_dict()
# create an instance of SiteMembershipRequestWithPerson from a dict
site_membership_request_with_person_form_dict = site_membership_request_with_person.from_dict(site_membership_request_with_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


