# alfresco_core_api_client.CategoriesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category**](CategoriesApi.md#create_category) | **POST** /categories/{categoryId}/subcategories | Create a category
[**create_category_link_for_node**](CategoriesApi.md#create_category_link_for_node) | **POST** /nodes/{nodeId}/category-links | Assign a node to a category
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /categories/{categoryId} | Delete a category
[**delete_category_link_from_node**](CategoriesApi.md#delete_category_link_from_node) | **DELETE** /nodes/{nodeId}/category-links/{categoryId} | Unassign a node from a category
[**get_category**](CategoriesApi.md#get_category) | **GET** /categories/{categoryId} | Get a category
[**list_categories_for_node**](CategoriesApi.md#list_categories_for_node) | **GET** /nodes/{nodeId}/category-links | List categories that a node is assigned to
[**list_subcategories**](CategoriesApi.md#list_subcategories) | **GET** /categories/{categoryId}/subcategories | List categories
[**update_category**](CategoriesApi.md#update_category) | **PUT** /categories/{categoryId} | Update a category


# **create_category**
> CategoryEntry create_category(category_id, category_body_create, include=include, fields=fields)

Create a category

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Creates a new category within the category **categoryId**.  The parameter categoryId can be set to the alias -root- to create a new top level category.  You must have admin rights to create a category.  It is possible to create more than one subcategory by posting a list of categories: ```JSON [   {     \"name\": \"test category 1\"   },   {     \"name\": \"test category 2\"   } ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {          ...         }       }     ]   } } ``` 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.category_body import CategoryBody
from alfresco_core_api_client.models.category_entry import CategoryEntry
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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | The identifier of a category.
    category_body_create = alfresco_core_api_client.CategoryBody() # CategoryBody | The category details
    include = ['include_example'] # List[str] | Returns additional information about the category. The following optional fields can be requested: * count * path  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a category
        api_response = api_instance.create_category(category_id, category_body_create, include=include, fields=fields)
        print("The response of CategoriesApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The identifier of a category. | 
 **category_body_create** | [**CategoryBody**](CategoryBody.md)| The category details | 
 **include** | [**List[str]**](str.md)| Returns additional information about the category. The following optional fields can be requested: * count * path  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**CategoryEntry**](CategoryEntry.md)

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
**409** | Category with the given name already exists under the parent category |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_category_link_for_node**
> CategoryEntry create_category_link_for_node(node_id, category_link_body_create, include=include, fields=fields)

Assign a node to a category

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Assign the node **nodeId** to a category. You specify the category ID in a JSON body like this:  ```JSON {   \"categoryId\": \"01234567-89ab-cdef-0123-456789abcdef\" } ```  **Note:** You can assign the node to more than one category by specifying a list of categories in the JSON body like this:  ```JSON [   {     \"categoryId\": \"01234567-89ab-cdef-0123-456789abcdef\"   },   {     \"categoryId\": \"89abcdef-0123-4567-89ab-cdef01234567\"   } ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {          ...         }       }     ]   } } ``` 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.category_entry import CategoryEntry
from alfresco_core_api_client.models.category_link_body import CategoryLinkBody
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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    category_link_body_create = alfresco_core_api_client.CategoryLinkBody() # CategoryLinkBody | The new category link
    include = ['include_example'] # List[str] | Returns additional information about the category. The following optional fields can be requested: * path  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Assign a node to a category
        api_response = api_instance.create_category_link_for_node(node_id, category_link_body_create, include=include, fields=fields)
        print("The response of CategoriesApi->create_category_link_for_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category_link_for_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **category_link_body_create** | [**CategoryLinkBody**](CategoryLinkBody.md)| The new category link | 
 **include** | [**List[str]**](str.md)| Returns additional information about the category. The following optional fields can be requested: * path  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**CategoryEntry**](CategoryEntry.md)

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
**403** | User does not have permission to assign the node to a category |  -  |
**404** | **nodeId** or **categoryId** does not exist  |  -  |
**422** | Cannot assign a node of this type to a category |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(category_id)

Delete a category

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Deletes the category with **categoryId**. This will cause everything to be removed from the category.  You must have admin rights to delete a category. 

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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | The identifier of a category.

    try:
        # Delete a category
        api_instance.delete_category(category_id)
    except Exception as e:
        print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The identifier of a category. | 

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
**403** | Current user is not an administrator and so does not have permission to delete the category. |  -  |
**404** | **categoryId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category_link_from_node**
> delete_category_link_from_node(node_id, category_id)

Unassign a node from a category

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Removes the node **nodeId** from the category **categoryId**. 

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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    category_id = 'category_id_example' # str | The identifier of a category.

    try:
        # Unassign a node from a category
        api_instance.delete_category_link_from_node(node_id, category_id)
    except Exception as e:
        print("Exception when calling CategoriesApi->delete_category_link_from_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **category_id** | **str**| The identifier of a category. | 

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
**403** | User does not have permission to remove the node from the category |  -  |
**404** | **nodeId** or **categoryId** does not exist  |  -  |
**422** | Invalid type for node with id **nodeId** |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> CategoryEntry get_category(category_id, include=include, fields=fields)

Get a category

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Get a specific category with **categoryId**. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.category_entry import CategoryEntry
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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | The identifier of a category.
    include = ['include_example'] # List[str] | Returns additional information about the category. The following optional fields can be requested: * count * path  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a category
        api_response = api_instance.get_category(category_id, include=include, fields=fields)
        print("The response of CategoriesApi->get_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The identifier of a category. | 
 **include** | [**List[str]**](str.md)| Returns additional information about the category. The following optional fields can be requested: * count * path  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**CategoryEntry**](CategoryEntry.md)

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
**404** | **categoryId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories_for_node**
> CategoryPaging list_categories_for_node(node_id, skip_count=skip_count, max_items=max_items, include=include, fields=fields)

List categories that a node is assigned to

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Gets a list of categories for node **nodeId**. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.category_paging import CategoryPaging
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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    include = ['include_example'] # List[str] | Returns additional information about the category. The following optional fields can be requested: * path  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List categories that a node is assigned to
        api_response = api_instance.list_categories_for_node(node_id, skip_count=skip_count, max_items=max_items, include=include, fields=fields)
        print("The response of CategoriesApi->list_categories_for_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->list_categories_for_node: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **include** | [**List[str]**](str.md)| Returns additional information about the category. The following optional fields can be requested: * path  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**CategoryPaging**](CategoryPaging.md)

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
**403** | User does not have permission to read categories on the node |  -  |
**404** | **nodeId** does not exist  |  -  |
**422** | Invalid type for node with id **nodeId** |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subcategories**
> CategoryPaging list_subcategories(category_id, include=include, skip_count=skip_count, max_items=max_items, fields=fields)

List categories

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Gets a list of subcategories within the category **categoryId**.  The parameter categoryId can be set to the alias -root- to obtain a list of top level categories. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.category_paging import CategoryPaging
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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | The identifier of a category.
    include = ['include_example'] # List[str] | Returns additional information about the category. The following optional fields can be requested: * count * path  (optional)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List categories
        api_response = api_instance.list_subcategories(category_id, include=include, skip_count=skip_count, max_items=max_items, fields=fields)
        print("The response of CategoriesApi->list_subcategories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->list_subcategories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The identifier of a category. | 
 **include** | [**List[str]**](str.md)| Returns additional information about the category. The following optional fields can be requested: * count * path  | [optional] 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**CategoryPaging**](CategoryPaging.md)

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
**404** | **categoryId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> CategoryEntry update_category(category_id, category_body_update, include=include, fields=fields)

Update a category

**Note:** this endpoint is available in Alfresco 7.4 and newer versions.  Updates the category **categoryId**.  You must have admin rights to update a category. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.category_body import CategoryBody
from alfresco_core_api_client.models.category_entry import CategoryEntry
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
    api_instance = alfresco_core_api_client.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | The identifier of a category.
    category_body_update = alfresco_core_api_client.CategoryBody() # CategoryBody | The updated category
    include = ['include_example'] # List[str] | Returns additional information about the category. The following optional fields can be requested: * count * path  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Update a category
        api_response = api_instance.update_category(category_id, category_body_update, include=include, fields=fields)
        print("The response of CategoriesApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The identifier of a category. | 
 **category_body_update** | [**CategoryBody**](CategoryBody.md)| The updated category | 
 **include** | [**List[str]**](str.md)| Returns additional information about the category. The following optional fields can be requested: * count * path  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**CategoryEntry**](CategoryEntry.md)

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
**403** | Current user is not an administrator and so does not have permission to update the category. |  -  |
**404** | **categoryId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

