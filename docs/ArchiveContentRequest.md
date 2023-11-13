# ArchiveContentRequest

Request object holding archive content related paramteres for given content. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_params** | **Dict[str, str]** | Optional map (String-String) of archive request properties for given content.  | [optional] 

## Example

```python
from alfresco_core_api_client.models.archive_content_request import ArchiveContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveContentRequest from a JSON string
archive_content_request_instance = ArchiveContentRequest.from_json(json)
# print the JSON string representation of the object
print ArchiveContentRequest.to_json()

# convert the object into a dict
archive_content_request_dict = archive_content_request_instance.to_dict()
# create an instance of ArchiveContentRequest from a dict
archive_content_request_form_dict = archive_content_request.from_dict(archive_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


