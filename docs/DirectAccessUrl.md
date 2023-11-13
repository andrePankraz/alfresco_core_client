# DirectAccessUrl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_url** | **str** | The direct access URL of a binary content | 
**attachment** | **bool** | Flag to control the download method, **true** for attachment URL, **false** for embedded URL | [optional] 
**expires_at** | **datetime** | The direct access URL would become invalid when the expiry date is reached | [optional] 

## Example

```python
from alfresco_core_api_client.models.direct_access_url import DirectAccessUrl

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessUrl from a JSON string
direct_access_url_instance = DirectAccessUrl.from_json(json)
# print the JSON string representation of the object
print DirectAccessUrl.to_json()

# convert the object into a dict
direct_access_url_dict = direct_access_url_instance.to_dict()
# create an instance of DirectAccessUrl from a dict
direct_access_url_form_dict = direct_access_url.from_dict(direct_access_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


