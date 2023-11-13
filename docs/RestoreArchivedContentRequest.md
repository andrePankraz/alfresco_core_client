# RestoreArchivedContentRequest

Request object holding restore content from artchive related paramteres for given content. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restore_priority** | **str** | Restore from archive priority (Standard/High - to be mapped to Storage Provider specific values in Cloud Connectors) | [optional] 

## Example

```python
from alfresco_core_api_client.models.restore_archived_content_request import RestoreArchivedContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreArchivedContentRequest from a JSON string
restore_archived_content_request_instance = RestoreArchivedContentRequest.from_json(json)
# print the JSON string representation of the object
print RestoreArchivedContentRequest.to_json()

# convert the object into a dict
restore_archived_content_request_dict = restore_archived_content_request_instance.to_dict()
# create an instance of RestoreArchivedContentRequest from a dict
restore_archived_content_request_form_dict = restore_archived_content_request.from_dict(restore_archived_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


