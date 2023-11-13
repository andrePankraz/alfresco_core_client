# ActionBodyExecTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_definition_id** | **str** |  | 
**params** | **object** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.action_body_exec_template import ActionBodyExecTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ActionBodyExecTemplate from a JSON string
action_body_exec_template_instance = ActionBodyExecTemplate.from_json(json)
# print the JSON string representation of the object
print ActionBodyExecTemplate.to_json()

# convert the object into a dict
action_body_exec_template_dict = action_body_exec_template_instance.to_dict()
# create an instance of ActionBodyExecTemplate from a dict
action_body_exec_template_form_dict = action_body_exec_template.from_dict(action_body_exec_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


