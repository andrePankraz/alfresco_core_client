# PersonBodyUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**skype_id** | **str** |  | [optional] 
**google_id** | **str** |  | [optional] 
**instant_message_id** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**mobile** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**user_status** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**email_notifications_enabled** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 
**aspect_names** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.person_body_update import PersonBodyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PersonBodyUpdate from a JSON string
person_body_update_instance = PersonBodyUpdate.from_json(json)
# print the JSON string representation of the object
print PersonBodyUpdate.to_json()

# convert the object into a dict
person_body_update_dict = person_body_update_instance.to_dict()
# create an instance of PersonBodyUpdate from a dict
person_body_update_form_dict = person_body_update.from_dict(person_body_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


