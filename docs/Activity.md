# Activity

Activities describe any past activity in a site, for example creating an item of content, commenting on a node, liking an item of content. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_person_id** | **str** | The id of the person who performed the activity | 
**id** | **int** | The unique id of the activity | 
**site_id** | **str** | The unique id of the site on which the activity was performed | [optional] 
**posted_at** | **datetime** | The date time at which the activity was performed | [optional] 
**feed_person_id** | **str** | The feed on which this activity was posted | 
**activity_summary** | **Dict[str, str]** | An object summarizing the activity | [optional] 
**activity_type** | **str** | The type of the activity posted | 

## Example

```python
from alfresco_core_api_client.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print Activity.to_json()

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_form_dict = activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


