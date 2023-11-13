# Person


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**email** | **str** |  | 
**skype_id** | **str** |  | [optional] 
**google_id** | **str** |  | [optional] 
**instant_message_id** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**mobile** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**status_updated_at** | **datetime** |  | [optional] 
**user_status** | **str** |  | [optional] 
**enabled** | **bool** |  | [default to True]
**email_notifications_enabled** | **bool** |  | [optional] [default to True]
**aspect_names** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 
**capabilities** | [**Capabilities**](Capabilities.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print Person.to_json()

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_form_dict = person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


