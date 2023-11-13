# PasswordResetBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | the new password | 
**id** | **str** | the workflow id provided in the reset password email | 
**key** | **str** | the workflow key provided in the reset password email | 

## Example

```python
from alfresco_core_api_client.models.password_reset_body import PasswordResetBody

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordResetBody from a JSON string
password_reset_body_instance = PasswordResetBody.from_json(json)
# print the JSON string representation of the object
print PasswordResetBody.to_json()

# convert the object into a dict
password_reset_body_dict = password_reset_body_instance.to_dict()
# create an instance of PasswordResetBody from a dict
password_reset_body_form_dict = password_reset_body.from_dict(password_reset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


