# NodeBodyLock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_to_expire** | **int** |  | [optional] 
**type** | **str** |  | [optional] [default to 'ALLOW_OWNER_CHANGES']
**lifetime** | **str** |  | [optional] [default to 'PERSISTENT']

## Example

```python
from alfresco_core_api_client.models.node_body_lock import NodeBodyLock

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBodyLock from a JSON string
node_body_lock_instance = NodeBodyLock.from_json(json)
# print the JSON string representation of the object
print NodeBodyLock.to_json()

# convert the object into a dict
node_body_lock_dict = node_body_lock_instance.to_dict()
# create an instance of NodeBodyLock from a dict
node_body_lock_form_dict = node_body_lock.from_dict(node_body_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


