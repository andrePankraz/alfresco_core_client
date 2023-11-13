# ActionConstraintEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ActionConstraint**](ActionConstraint.md) |  | 

## Example

```python
from alfresco_core_api_client.models.action_constraint_entry import ActionConstraintEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActionConstraintEntry from a JSON string
action_constraint_entry_instance = ActionConstraintEntry.from_json(json)
# print the JSON string representation of the object
print ActionConstraintEntry.to_json()

# convert the object into a dict
action_constraint_entry_dict = action_constraint_entry_instance.to_dict()
# create an instance of ActionConstraintEntry from a dict
action_constraint_entry_form_dict = action_constraint_entry.from_dict(action_constraint_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


