# PersonNetwork

A network is the group of users and sites that belong to an organization. Networks are organized by email domain. When a user signs up for an Alfresco account , their email domain becomes their Home Network. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This network&#39;s unique id | 
**home_network** | **bool** | Is this the home network? | [optional] 
**is_enabled** | **bool** |  | 
**created_at** | **datetime** |  | [optional] 
**paid_network** | **bool** |  | [optional] 
**subscription_level** | **str** |  | [optional] 
**quotas** | [**List[NetworkQuota]**](NetworkQuota.md) |  | [optional] 

## Example

```python
from alfresco_core_api_client.models.person_network import PersonNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNetwork from a JSON string
person_network_instance = PersonNetwork.from_json(json)
# print the JSON string representation of the object
print PersonNetwork.to_json()

# convert the object into a dict
person_network_dict = person_network_instance.to_dict()
# create an instance of PersonNetwork from a dict
person_network_form_dict = person_network.from_dict(person_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


