# NodeAssociationEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**NodeAssociation**](NodeAssociation.md) |  | 

## Example

```python
from alfresco_core_api_client.models.node_association_entry import NodeAssociationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAssociationEntry from a JSON string
node_association_entry_instance = NodeAssociationEntry.from_json(json)
# print the JSON string representation of the object
print NodeAssociationEntry.to_json()

# convert the object into a dict
node_association_entry_dict = node_association_entry_instance.to_dict()
# create an instance of NodeAssociationEntry from a dict
node_association_entry_form_dict = node_association_entry.from_dict(node_association_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


