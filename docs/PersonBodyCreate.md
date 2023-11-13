# PersonBodyCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | 
**skype_id** | **str** |  | [optional] 
**google_id** | **str** |  | [optional] 
**instant_message_id** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**mobile** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**user_status** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to True]
**email_notifications_enabled** | **bool** |  | [optional] [default to True]
**password** | **str** |  | 
**aspect_names** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.person_body_create import PersonBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PersonBodyCreate from a JSON string
person_body_create_instance = PersonBodyCreate.from_json(json)
# print the JSON string representation of the object
print PersonBodyCreate.to_json()

# convert the object into a dict
person_body_create_dict = person_body_create_instance.to_dict()
# create an instance of PersonBodyCreate from a dict
person_body_create_form_dict = person_body_create.from_dict(person_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


