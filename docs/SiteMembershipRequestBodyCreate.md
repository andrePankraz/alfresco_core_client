# SiteMembershipRequestBodyCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**id** | **str** |  | 
**title** | **str** |  | [optional] 
**client** | **str** | Optional client name used when sending an email to the end user, defaults to \&quot;share\&quot; if not provided. **Note:** The client must be registered before this API can send an email. **Note:** This is available in Alfresco 7.0.0 and newer versions.  | [optional] 

## Example

```python
from alfresco_core_api_client.models.site_membership_request_body_create import SiteMembershipRequestBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestBodyCreate from a JSON string
site_membership_request_body_create_instance = SiteMembershipRequestBodyCreate.from_json(json)
# print the JSON string representation of the object
print SiteMembershipRequestBodyCreate.to_json()

# convert the object into a dict
site_membership_request_body_create_dict = site_membership_request_body_create_instance.to_dict()
# create an instance of SiteMembershipRequestBodyCreate from a dict
site_membership_request_body_create_form_dict = site_membership_request_body_create.from_dict(site_membership_request_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


