# ActionConstraintData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Constraint value (this can also be a node id) | 
**label** | **str** | Constraint display label | [optional] 

## Example

```python
from alfresco_core_api_client.models.action_constraint_data import ActionConstraintData

# TODO update the JSON string below
json = "{}"
# create an instance of ActionConstraintData from a JSON string
action_constraint_data_instance = ActionConstraintData.from_json(json)
# print the JSON string representation of the object
print ActionConstraintData.to_json()

# convert the object into a dict
action_constraint_data_dict = action_constraint_data_instance.to_dict()
# create an instance of ActionConstraintData from a dict
action_constraint_data_form_dict = action_constraint_data.from_dict(action_constraint_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


