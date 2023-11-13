# ActionConstraint

Response object holding action parameter constraint name and map of its values-labels. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_name** | **str** | Name of the constraint.  | [optional] 
**constraint_values** | [**List[ActionConstraintData]**](ActionConstraintData.md) | A list of constraint possbile values along with additional data (label, isNode flag). Sample object could be: &#x60;&#x60;&#x60;JSON \&quot;constraintValues\&quot;: [            {               \&quot;value\&quot;: \&quot;EQUALS\&quot;,               \&quot;label\&quot;: \&quot;Equals\&quot;            },            {               \&quot;value\&quot;: \&quot;CONTAINS\&quot;,               \&quot;label\&quot;: \&quot;Contains\&quot;            },            {               \&quot;value\&quot;: \&quot;BEGINS\&quot;,               \&quot;label\&quot;: \&quot;Begins With\&quot;            },            {               \&quot;value\&quot;: \&quot;ENDS\&quot;,               \&quot;label\&quot;: \&quot;Ends With\&quot;            },            {               \&quot;value\&quot;: \&quot;GREATER_THAN\&quot;,               \&quot;label\&quot;: \&quot;Greater Than\&quot;            },            {               \&quot;value\&quot;: \&quot;GREATER_THAN_EQUAL\&quot;,               \&quot;label\&quot;: \&quot;Greater Than Or Equal To\&quot;            },            {               \&quot;value\&quot;: \&quot;LESS_THAN\&quot;,               \&quot;label\&quot;: \&quot;Less Than\&quot;            },            {               \&quot;value\&quot;: \&quot;LESS_THAN_EQUAL\&quot;,               \&quot;label\&quot;: \&quot;Less Than Or Equal To\&quot;            }         ] &#x60;&#x60;&#x60; or &#x60;&#x60;&#x60;JSON \&quot;constraintValues\&quot;: [                         {                             \&quot;value\&quot;: \&quot;fa41fd6e-5640-410f-9f3e-93f268186f69\&quot;,                             \&quot;label\&quot;: \&quot;Start Pooled Review and Approve Workflow\&quot;,                             \&quot;isNode\&quot;: true                         }                     ] &#x60;&#x60;&#x60;  | [optional] 

## Example

```python
from alfresco_core_api_client.models.action_constraint import ActionConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ActionConstraint from a JSON string
action_constraint_instance = ActionConstraint.from_json(json)
# print the JSON string representation of the object
print ActionConstraint.to_json()

# convert the object into a dict
action_constraint_dict = action_constraint_instance.to_dict()
# create an instance of ActionConstraint from a dict
action_constraint_form_dict = action_constraint.from_dict(action_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


