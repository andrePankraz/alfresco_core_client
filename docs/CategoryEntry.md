# CategoryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Category**](Category.md) |  | 

## Example

```python
from alfresco_core_api_client.models.category_entry import CategoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryEntry from a JSON string
category_entry_instance = CategoryEntry.from_json(json)
# print the JSON string representation of the object
print CategoryEntry.to_json()

# convert the object into a dict
category_entry_dict = category_entry_instance.to_dict()
# create an instance of CategoryEntry from a dict
category_entry_form_dict = category_entry.from_dict(category_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


