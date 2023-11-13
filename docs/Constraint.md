# Constraint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** | the type of the constraint | [optional] 
**title** | **str** | the human-readable constraint title | [optional] 
**description** | **str** | the human-readable constraint description | [optional] 
**parameters** | **Dict[str, object]** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print Constraint.to_json()

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_form_dict = constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


