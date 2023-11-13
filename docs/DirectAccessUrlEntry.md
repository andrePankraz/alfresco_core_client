# DirectAccessUrlEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**DirectAccessUrl**](DirectAccessUrl.md) |  | 

## Example

```python
from alfresco_core_api_client.models.direct_access_url_entry import DirectAccessUrlEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessUrlEntry from a JSON string
direct_access_url_entry_instance = DirectAccessUrlEntry.from_json(json)
# print the JSON string representation of the object
print DirectAccessUrlEntry.to_json()

# convert the object into a dict
direct_access_url_entry_dict = direct_access_url_entry_instance.to_dict()
# create an instance of DirectAccessUrlEntry from a dict
direct_access_url_entry_form_dict = direct_access_url_entry.from_dict(direct_access_url_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


