# AssociationBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** |  | 
**assoc_type** | **str** |  | 

## Example

```python
from alfresco_core_api_client.models.association_body import AssociationBody

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationBody from a JSON string
association_body_instance = AssociationBody.from_json(json)
# print the JSON string representation of the object
print AssociationBody.to_json()

# convert the object into a dict
association_body_dict = association_body_instance.to_dict()
# create an instance of AssociationBody from a dict
association_body_form_dict = association_body.from_dict(association_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


