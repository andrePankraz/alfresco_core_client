# SiteMembershipRequestBodyUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.site_membership_request_body_update import SiteMembershipRequestBodyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestBodyUpdate from a JSON string
site_membership_request_body_update_instance = SiteMembershipRequestBodyUpdate.from_json(json)
# print the JSON string representation of the object
print SiteMembershipRequestBodyUpdate.to_json()

# convert the object into a dict
site_membership_request_body_update_dict = site_membership_request_body_update_instance.to_dict()
# create an instance of SiteMembershipRequestBodyUpdate from a dict
site_membership_request_body_update_form_dict = site_membership_request_body_update.from_dict(site_membership_request_body_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


