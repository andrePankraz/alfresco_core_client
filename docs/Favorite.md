# Favorite

A favorite describes an Alfresco entity that a person has marked as a favorite. The target can be a site, file or folder. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_guid** | **str** | The guid of the object that is a favorite. | 
**created_at** | **datetime** | The time the object was made a favorite. | [optional] 
**target** | **object** |  | 
**properties** | **object** | A subset of the target favorite properties, system properties and properties already available in the target are excluded. | [optional] 
**allowable_operations** | **List[str]** | The allowable operations for the target. | [optional] 

## Example

```python
from alfresco_core_api_client.models.favorite import Favorite

# TODO update the JSON string below
json = "{}"
# create an instance of Favorite from a JSON string
favorite_instance = Favorite.from_json(json)
# print the JSON string representation of the object
print Favorite.to_json()

# convert the object into a dict
favorite_dict = favorite_instance.to_dict()
# create an instance of Favorite from a dict
favorite_form_dict = favorite.from_dict(favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


