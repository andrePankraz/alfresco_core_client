# ChildAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_id** | **str** |  | 
**assoc_type** | **str** |  | 

## Example

```python
from alfresco_core_api_client.models.child_association import ChildAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAssociation from a JSON string
child_association_instance = ChildAssociation.from_json(json)
# print the JSON string representation of the object
print ChildAssociation.to_json()

# convert the object into a dict
child_association_dict = child_association_instance.to_dict()
# create an instance of ChildAssociation from a dict
child_association_form_dict = child_association.from_dict(child_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


