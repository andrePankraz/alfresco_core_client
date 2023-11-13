# alfresco_core_api_client.TagsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /tags | Create a tag
[**create_tag_for_node**](TagsApi.md#create_tag_for_node) | **POST** /nodes/{nodeId}/tags | Create a tag for a node
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{tagId} | Delete a tag
[**delete_tag_from_node**](TagsApi.md#delete_tag_from_node) | **DELETE** /nodes/{nodeId}/tags/{tagId} | Delete a tag from a node
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{tagId} | Get a tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | List tags
[**list_tags_for_node**](TagsApi.md#list_tags_for_node) | **GET** /nodes/{nodeId}/tags | List tags for a node
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags/{tagId} | Update a tag


# **create_tag**
> TagEntry create_tag(tag_body_create, include=include, fields=fields)

Create a tag

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Creates a new tag.  You must have admin rights to create a tag with this endpoint. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.tag_body import TagBody
from alfresco_core_api_client.models.tag_entry import TagEntry
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    tag_body_create = alfresco_core_api_client.TagBody() # TagBody | The tag details
    include = ['include_example'] # List[str] | Returns additional information about the tag. The following optional fields can be requested: * count  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a tag
        api_response = api_instance.create_tag(tag_body_create, include=include, fields=fields)
        print("The response of TagsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_body_create** | [**TagBody**](TagBody.md)| The tag details | 
 **include** | [**List[str]**](str.md)| Returns additional information about the tag. The following optional fields can be requested: * count  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**403** | User is not an administrator |  -  |
**409** | Tag with the given name already exists |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag_for_node**
> TagEntry create_tag_for_node(node_id, tag_body_create, fields=fields)

Create a tag for a node

Creates a tag on the node **nodeId**. You specify the tag in a JSON body like this:  ```JSON {   \"tag\":\"test-tag-1\" } ```  **Note:** You can create more than one tag by specifying a list of tags in the JSON body like this:  ```JSON [   {     \"tag\":\"test-tag-1\"   },   {     \"tag\":\"test-tag-2\"   } ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {          ...         }       }     ]   } } ``` 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.tag_body import TagBody
from alfresco_core_api_client.models.tag_entry import TagEntry
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    tag_body_create = alfresco_core_api_client.TagBody() # TagBody | The new tag
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a tag for a node
        api_response = api_instance.create_tag_for_node(node_id, tag_body_create, fields=fields)
        print("The response of TagsApi->create_tag_for_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag_for_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **tag_body_create** | [**TagBody**](TagBody.md)| The new tag | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to create tags on the node |  -  |
**404** | **nodeId** does not exist  |  -  |
**405** | Cannot tag a node of this type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag_id)

Delete a tag

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Deletes the tag with **tagId**. This will cause the tag to be removed from all nodes.  You must have admin rights to delete a tag. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | The identifier of a tag.

    try:
        # Delete a tag
        api_instance.delete_tag(tag_id)
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The identifier of a tag. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**403** | Current user is not an administrator and so does not have permission to delete the tag. |  -  |
**404** | **tagId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_from_node**
> delete_tag_from_node(node_id, tag_id)

Delete a tag from a node

Deletes tag **tagId** from node **nodeId**.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    tag_id = 'tag_id_example' # str | The identifier of a tag.

    try:
        # Delete a tag from a node
        api_instance.delete_tag_from_node(node_id, tag_id)
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag_from_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **tag_id** | **str**| The identifier of a tag. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to delete the tag |  -  |
**404** | **nodeId** or **tagId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagEntry get_tag(tag_id, include=include, fields=fields)

Get a tag

Get a specific tag with **tagId**.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.tag_entry import TagEntry
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | The identifier of a tag.
    include = ['include_example'] # List[str] | Returns additional information about the tag. The following optional fields can be requested: * count  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a tag
        api_response = api_instance.get_tag(tag_id, include=include, fields=fields)
        print("The response of TagsApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The identifier of a tag. | 
 **include** | [**List[str]**](str.md)| Returns additional information about the tag. The following optional fields can be requested: * count  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**404** | **tagId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> TagPaging list_tags(skip_count=skip_count, max_items=max_items, fields=fields, include=include, order_by=order_by, where=where)

List tags

Gets a list of tags in this repository.  You can use the **include** parameter to return additional **values** information.  You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * tag * count 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.tag_paging import TagPaging
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
    include = ['include_example'] # List[str] | Returns additional information about the tag. The following optional fields can be requested: * count  (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    where = 'where_example' # str | Optionally filter the list. The only supported options are:  * ```where=(tag='tagName')```  * ```where=(tag in ('tag1', 'tag2'))```  * ```where=(tag matches ('*tag*'))```  OR operator is also supported.  (optional)

    try:
        # List tags
        api_response = api_instance.list_tags(skip_count=skip_count, max_items=max_items, fields=fields, include=include, order_by=order_by, where=where)
        print("The response of TagsApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **include** | [**List[str]**](str.md)| Returns additional information about the tag. The following optional fields can be requested: * count  | [optional] 
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **where** | **str**| Optionally filter the list. The only supported options are:  * &#x60;&#x60;&#x60;where&#x3D;(tag&#x3D;&#39;tagName&#39;)&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;where&#x3D;(tag in (&#39;tag1&#39;, &#39;tag2&#39;))&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;where&#x3D;(tag matches (&#39;*tag*&#39;))&#x60;&#x60;&#x60;  OR operator is also supported.  | [optional] 

### Return type

[**TagPaging**](TagPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_for_node**
> TagPaging list_tags_for_node(node_id, skip_count=skip_count, max_items=max_items, fields=fields)

List tags for a node

Gets a list of tags for node **nodeId**.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.tag_paging import TagPaging
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List tags for a node
        api_response = api_instance.list_tags_for_node(node_id, skip_count=skip_count, max_items=max_items, fields=fields)
        print("The response of TagsApi->list_tags_for_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->list_tags_for_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagPaging**](TagPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to read tags on the node |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> TagEntry update_tag(tag_id, tag_body_update, include=include, fields=fields)

Update a tag

Updates the tag **tagId**.  You must have admin rights to update a tag. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.tag_body import TagBody
from alfresco_core_api_client.models.tag_entry import TagEntry
from alfresco_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_api_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_api_client.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | The identifier of a tag.
    tag_body_update = alfresco_core_api_client.TagBody() # TagBody | The updated tag
    include = ['include_example'] # List[str] | Returns additional information about the tag. The following optional fields can be requested: * count  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Update a tag
        api_response = api_instance.update_tag(tag_id, tag_body_update, include=include, fields=fields)
        print("The response of TagsApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->update_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The identifier of a tag. | 
 **tag_body_update** | [**TagBody**](TagBody.md)| The updated tag | 
 **include** | [**List[str]**](str.md)| Returns additional information about the tag. The following optional fields can be requested: * count  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**TagEntry**](TagEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | An invalid parameter has been supplied. |  -  |
**401** | Authentication failed |  -  |
**403** | Current user is not an administrator and so does not have permission to update the tag. |  -  |
**404** | **tagId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

