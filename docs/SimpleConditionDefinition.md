# SimpleConditionDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The name of the property to compare.  This should be either a property (e.g. \&quot;cm:name\&quot;) or one of the keywords from this list: * size (the size of the content for a node) * mimetype (the mimetype of the content for a node) * encoding (the encoding of the content for a node) * category (a category for the node) * tag (a tag that the node has) * aspect (an aspect that the node has)  For multi-valued properties the condition is satisfied if any of the values match the condition.  | 
**comparator** | **str** | The method to compare the property against the parameter.  Depending on the type of the property then different comparators are available: * All types: equals * text: contains, startsWith, endsWith * int/long/float/double/date: greaterThan, lessThan, greaterThanOrEqual, lessThanOrEqual * type: instanceOf  Where a property is multivalued then the condition is true if it is satisfied by any of the values.  | 
**parameter** | **str** | The value to compare the field against | 

## Example

```python
from alfresco_core_api_client.models.simple_condition_definition import SimpleConditionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleConditionDefinition from a JSON string
simple_condition_definition_instance = SimpleConditionDefinition.from_json(json)
# print the JSON string representation of the object
print SimpleConditionDefinition.to_json()

# convert the object into a dict
simple_condition_definition_dict = simple_condition_definition_instance.to_dict()
# create an instance of SimpleConditionDefinition from a dict
simple_condition_definition_form_dict = simple_condition_definition.from_dict(simple_condition_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


