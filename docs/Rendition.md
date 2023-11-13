# Rendition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.rendition import Rendition

# TODO update the JSON string below
json = "{}"
# create an instance of Rendition from a JSON string
rendition_instance = Rendition.from_json(json)
# print the JSON string representation of the object
print Rendition.to_json()

# convert the object into a dict
rendition_dict = rendition_instance.to_dict()
# create an instance of Rendition from a dict
rendition_form_dict = rendition.from_dict(rendition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


