# CompositeConditionDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverted** | **bool** | Whether to invert the logic for this condition (if true then \&quot;not\&quot; is applied to the whole condition) | [optional] [default to False]
**boolean_mode** | **str** | How to combine the clauses of this condition (\&quot;and\&quot; or \&quot;or\&quot;) | [optional] [default to 'and']
**composite_conditions** | [**List[CompositeConditionDefinition]**](CompositeConditionDefinition.md) | Nested list of composite clauses in this condition | [optional] 
**simple_conditions** | [**List[SimpleConditionDefinition]**](SimpleConditionDefinition.md) | Nested list of simple (per field) conditions. | [optional] 

## Example

```python
from alfresco_core_api_client.models.composite_condition_definition import CompositeConditionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeConditionDefinition from a JSON string
composite_condition_definition_instance = CompositeConditionDefinition.from_json(json)
# print the JSON string representation of the object
print CompositeConditionDefinition.to_json()

# convert the object into a dict
composite_condition_definition_dict = composite_condition_definition_instance.to_dict()
# create an instance of CompositeConditionDefinition from a dict
composite_condition_definition_form_dict = composite_condition_definition.from_dict(composite_condition_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


