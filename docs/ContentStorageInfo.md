# ContentStorageInfo

Response object holding storage properties related data for given content. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Content type property identifier (e.g. cm:content). Inside this object only colon (&#39;:&#39;) delimiter for namespace-prefix will be used.  | 
**storage_properties** | **Dict[str, str]** | A map (String-String) of storage properties for given content.  | [optional] 

## Example

```python
from alfresco_core_api_client.models.content_storage_info import ContentStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStorageInfo from a JSON string
content_storage_info_instance = ContentStorageInfo.from_json(json)
# print the JSON string representation of the object
print ContentStorageInfo.to_json()

# convert the object into a dict
content_storage_info_dict = content_storage_info_instance.to_dict()
# create an instance of ContentStorageInfo from a dict
content_storage_info_form_dict = content_storage_info.from_dict(content_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


