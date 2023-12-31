# Download


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_added** | **int** | number of files added so far in the zip | [optional] 
**bytes_added** | **int** | number of bytes added so far in the zip | [optional] 
**id** | **str** | the id of the download node | [optional] 
**total_files** | **int** | the total number of files to be added in the zip | [optional] 
**total_bytes** | **int** | the total number of bytes to be added in the zip | [optional] 
**status** | **str** | the current status of the download node creation | [optional] [default to 'PENDING']

## Example

```python
from alfresco_core_api_client.models.download import Download

# TODO update the JSON string below
json = "{}"
# create an instance of Download from a JSON string
download_instance = Download.from_json(json)
# print the JSON string representation of the object
print Download.to_json()

# convert the object into a dict
download_dict = download_instance.to_dict()
# create an instance of Download from a dict
download_form_dict = download.from_dict(download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


