# ChildAssociationBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_id** | **str** |  | 
**assoc_type** | **str** |  | 

## Example

```python
from alfresco_core_api_client.models.child_association_body import ChildAssociationBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAssociationBody from a JSON string
child_association_body_instance = ChildAssociationBody.from_json(json)
# print the JSON string representation of the object
print ChildAssociationBody.to_json()

# convert the object into a dict
child_association_body_dict = child_association_body_instance.to_dict()
# create an instance of ChildAssociationBody from a dict
child_association_body_form_dict = child_association_body.from_dict(child_association_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


