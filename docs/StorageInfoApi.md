# alfresco_core_api_client.StorageInfoApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_properties**](StorageInfoApi.md#get_storage_properties) | **GET** /nodes/{nodeId}/storage-info/{contentPropName} | Retrieve storage properties for given content
[**get_version_storage_properties**](StorageInfoApi.md#get_version_storage_properties) | **GET** /nodes/{nodeId}/versions/{versionId}/storage-info/{contentPropName} | Retrieve storage properties for given version content
[**request_archive_content**](StorageInfoApi.md#request_archive_content) | **POST** /nodes/{nodeId}/storage-info/{contentPropName}/archive | Request to send given content to archive
[**request_archive_version_content**](StorageInfoApi.md#request_archive_version_content) | **POST** /nodes/{nodeId}/versions/{versionId}/storage-info/{contentPropName}/archive | Request to send given version content to archive
[**request_restore_content_from_archive**](StorageInfoApi.md#request_restore_content_from_archive) | **POST** /nodes/{nodeId}/storage-info/{contentPropName}/archive-restore | Request to restore given content from archive
[**request_restore_version_content_from_archive**](StorageInfoApi.md#request_restore_version_content_from_archive) | **POST** /nodes/{nodeId}/versions/{versionId}/storage-info/{contentPropName}/archive-restore | Request to restore given version content from archive


# **get_storage_properties**
> ContentStorageInfo get_storage_properties(node_id, content_prop_name)

Retrieve storage properties for given content

**Note:** this endpoint is available in Alfresco 7.2.0 and newer versions. It also requires at least one specific implementation of underlying functionality in Cloud Connector(s).  Gets storage properties for given content.  Please find below sample responses for this endpoint when Alfresco Content Connector for AWS S3 is installed.  Similar responses will be returned when Alfresco Content Connector for Azure Blob is installed, albeit it with  some native storage properties with x-ms- prefix instead of x-amz- prefix.  Standard storage class: ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archived\": \"false\"     },     \"id\": \"cm:content\"   } } ``` Intelligent tiering storage class: ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archived\": \"false\",       \"x-amz-storage-class\": \"INTELLIGENT_TIERING\"     },     \"id\": \"cm:content\"   } } ``` Glacier archive storage class (no restore request ongoing or submitted): ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archived\": \"true\",       \"x-amz-storage-class\": \"GLACIER\"     },     \"id\": \"cm:content\"   } } ``` Glacier archive storage class (restore request ongoing, not completed): ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archive-restore-in-progress\": \"true\",       \"x-amz-restore\": \"ongoing-request=\\\"true\\\"\",       \"x-alf-archived\": \"true\",       \"x-amz-storage-class\": \"GLACIER\"     },     \"id\": \"cm:content\"   } } ``` Glacier archive storage class (restore request completed): ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archive-restore-in-progress\": \"false\",       \"x-amz-restore\": \"ongoing-request=\\\"false\\\", expiry-date=\\\"Fri Nov 26 01:00:00 CET 2021\\\"\",       \"x-alf-archive-restore-expiry\": \"2021-11-26T00:00:00.000Z\",       \"x-alf-archived\": \"false\",       \"x-amz-storage-class\": \"GLACIER\"     },     \"id\": \"cm:content\"   } } ``` 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.content_storage_info import ContentStorageInfo
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
    api_instance = alfresco_core_api_client.StorageInfoApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    content_prop_name = 'content_prop_name_example' # str | The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (':') or underscore ('_') character (e.g., 'cm:content' or 'cm_content'). 

    try:
        # Retrieve storage properties for given content
        api_response = api_instance.get_storage_properties(node_id, content_prop_name)
        print("The response of StorageInfoApi->get_storage_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageInfoApi->get_storage_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **content_prop_name** | **str**| The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (&#39;:&#39;) or underscore (&#39;_&#39;) character (e.g., &#39;cm:content&#39; or &#39;cm_content&#39;).  | 

### Return type

[**ContentStorageInfo**](ContentStorageInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** or **contentPropName** is not a valid format, or is not a file  |  -  |
**401** | Authentication failed |  -  |
**403** | Not authorized |  -  |
**404** | **nodeId** or **contentPropName** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_storage_properties**
> ContentStorageInfo get_version_storage_properties(node_id, version_id, content_prop_name)

Retrieve storage properties for given version content

**Note:** this endpoint is available in Alfresco 7.2.0 and newer versions. It also requires at least one specific implementation of underlying functionality in Cloud Connector(s).  Gets storage properties for given version content.  Please find below sample responses for this endpoint when Alfresco Content Connector for AWS S3 is installed.  Similar responses will be returned when Alfresco Content Connector for Azure Blob is installed, albeit it with  some native storage properties with x-ms- prefix instead of x-amz- prefix.  Standard storage class: ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archived\": \"false\"     },     \"id\": \"cm:content\"   } } ``` Intelligent tiering storage class: ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archived\": \"false\",       \"x-amz-storage-class\": \"INTELLIGENT_TIERING\"     },     \"id\": \"cm:content\"   } } ``` Glacier archive storage class (no restore request ongoing or submitted): ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archived\": \"true\",       \"x-amz-storage-class\": \"GLACIER\"     },     \"id\": \"cm:content\"   } } ``` Glacier archive storage class (restore request ongoing, not completed): ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archive-restore-in-progress\": \"true\",       \"x-amz-restore\": \"ongoing-request=\\\"true\\\"\",       \"x-alf-archived\": \"true\",       \"x-amz-storage-class\": \"GLACIER\"     },     \"id\": \"cm:content\"   } } ``` Glacier archive storage class (restore request completed): ```json {   \"entry\": {     \"storageProperties\": {       \"x-alf-archive-restore-in-progress\": \"false\",       \"x-amz-restore\": \"ongoing-request=\\\"false\\\", expiry-date=\\\"Fri Nov 26 01:00:00 CET 2021\\\"\",       \"x-alf-archive-restore-expiry\": \"2021-11-26T00:00:00.000Z\",       \"x-alf-archived\": \"false\",       \"x-amz-storage-class\": \"GLACIER\"     },     \"id\": \"cm:content\"   } } ``` 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.content_storage_info import ContentStorageInfo
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
    api_instance = alfresco_core_api_client.StorageInfoApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
    content_prop_name = 'content_prop_name_example' # str | The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (':') or underscore ('_') character (e.g., 'cm:content' or 'cm_content'). 

    try:
        # Retrieve storage properties for given version content
        api_response = api_instance.get_version_storage_properties(node_id, version_id, content_prop_name)
        print("The response of StorageInfoApi->get_version_storage_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageInfoApi->get_version_storage_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **content_prop_name** | **str**| The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (&#39;:&#39;) or underscore (&#39;_&#39;) character (e.g., &#39;cm:content&#39; or &#39;cm_content&#39;).  | 

### Return type

[**ContentStorageInfo**](ContentStorageInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** or **versionId** or **contentPropName** is not a valid format, or is not a file  |  -  |
**401** | Authentication failed |  -  |
**403** | Not authorized |  -  |
**404** | **nodeId** or **versionId** or **contentPropName** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_archive_content**
> request_archive_content(node_id, content_prop_name, archive_content_request=archive_content_request)

Request to send given content to archive

**Note:** this endpoint is available in Alfresco 7.2.0 and newer versions. It also requires at least one specific implementation of underlying functionality in Cloud Connector(s).  Request to send given content to archive. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.archive_content_request import ArchiveContentRequest
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
    api_instance = alfresco_core_api_client.StorageInfoApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    content_prop_name = 'content_prop_name_example' # str | The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (':') or underscore ('_') character (e.g., 'cm:content' or 'cm_content'). 
    archive_content_request = alfresco_core_api_client.ArchiveContentRequest() # ArchiveContentRequest | Archive content request parameters - currently not supported by any Alfresco Cloud Connector. Body is not mandatory. Request body example: ```JSON {   \"archiveParams\": {                 \"x-amz-storage-class\": \"GLACIER\"               } } ```  (optional)

    try:
        # Request to send given content to archive
        api_instance.request_archive_content(node_id, content_prop_name, archive_content_request=archive_content_request)
    except Exception as e:
        print("Exception when calling StorageInfoApi->request_archive_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **content_prop_name** | **str**| The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (&#39;:&#39;) or underscore (&#39;_&#39;) character (e.g., &#39;cm:content&#39; or &#39;cm_content&#39;).  | 
 **archive_content_request** | [**ArchiveContentRequest**](ArchiveContentRequest.md)| Archive content request parameters - currently not supported by any Alfresco Cloud Connector. Body is not mandatory. Request body example: &#x60;&#x60;&#x60;JSON {   \&quot;archiveParams\&quot;: {                 \&quot;x-amz-storage-class\&quot;: \&quot;GLACIER\&quot;               } } &#x60;&#x60;&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** or **contentPropName** is not a valid format, or is not a file Content&#39;s storage state does not allow archive. Invalid archive paramters.  |  -  |
**401** | Authentication failed |  -  |
**403** | Not authorized |  -  |
**404** | **nodeId** or **contentPropName** does not exist  |  -  |
**409** | Content already archived |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_archive_version_content**
> request_archive_version_content(node_id, version_id, content_prop_name, archive_content_request=archive_content_request)

Request to send given version content to archive

**Note:** this endpoint is available in Alfresco 7.2.0 and newer versions. It also requires at least one specific implementation of underlying functionality in Cloud Connector(s).  Request to send given version content to archive. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.archive_content_request import ArchiveContentRequest
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
    api_instance = alfresco_core_api_client.StorageInfoApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
    content_prop_name = 'content_prop_name_example' # str | The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (':') or underscore ('_') character (e.g., 'cm:content' or 'cm_content'). 
    archive_content_request = alfresco_core_api_client.ArchiveContentRequest() # ArchiveContentRequest | Archive content request parameters - currently not supported by any Alfresco Cloud Connector. Body is not mandatory. Request body example: ```JSON {   \"archiveParams\": {                 \"x-amz-storage-class\": \"GLACIER\"               } } ```  (optional)

    try:
        # Request to send given version content to archive
        api_instance.request_archive_version_content(node_id, version_id, content_prop_name, archive_content_request=archive_content_request)
    except Exception as e:
        print("Exception when calling StorageInfoApi->request_archive_version_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **content_prop_name** | **str**| The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (&#39;:&#39;) or underscore (&#39;_&#39;) character (e.g., &#39;cm:content&#39; or &#39;cm_content&#39;).  | 
 **archive_content_request** | [**ArchiveContentRequest**](ArchiveContentRequest.md)| Archive content request parameters - currently not supported by any Alfresco Cloud Connector. Body is not mandatory. Request body example: &#x60;&#x60;&#x60;JSON {   \&quot;archiveParams\&quot;: {                 \&quot;x-amz-storage-class\&quot;: \&quot;GLACIER\&quot;               } } &#x60;&#x60;&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** or **versionId** or **contentPropName** is not a valid format, or is not a file Content&#39;s storage state does not allow archive. Invalid archive paramters.  |  -  |
**401** | Authentication failed |  -  |
**403** | Not authorized |  -  |
**404** | **nodeId** or **versionId** or **contentPropName** does not exist  |  -  |
**409** | Content already archived |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_restore_content_from_archive**
> request_restore_content_from_archive(node_id, content_prop_name, restore_archived_content_request=restore_archived_content_request)

Request to restore given content from archive

**Note:** this endpoint is available in Alfresco 7.2.0 and newer versions. It also requires at least one specific implementation of underlying functionality in Cloud Connector(s).  Request to restore given content from archive. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.restore_archived_content_request import RestoreArchivedContentRequest
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
    api_instance = alfresco_core_api_client.StorageInfoApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    content_prop_name = 'content_prop_name_example' # str | The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (':') or underscore ('_') character (e.g., 'cm:content' or 'cm_content'). 
    restore_archived_content_request = alfresco_core_api_client.RestoreArchivedContentRequest() # RestoreArchivedContentRequest | Restore content from archive request parameters. At the moment there is one parameter being supported which is restore priority. 'High' restore priority translates to 'Expedited' Glacier restore tier in AWS S3 and 'High' rehydrate priority in Azure Blob. 'Standard' restore priority translates to 'Standard' Glacier restore tier in AWS S3 and 'Standard' rehydrate priority in Azure Blob. Body is not mandatory. High restore priority request body example: ```JSON {   \"restorePriority\": \"High\" } ``` Standard restore priority request body example: ```JSON {   \"restorePriority\": \"Standard\" } ```  (optional)

    try:
        # Request to restore given content from archive
        api_instance.request_restore_content_from_archive(node_id, content_prop_name, restore_archived_content_request=restore_archived_content_request)
    except Exception as e:
        print("Exception when calling StorageInfoApi->request_restore_content_from_archive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **content_prop_name** | **str**| The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (&#39;:&#39;) or underscore (&#39;_&#39;) character (e.g., &#39;cm:content&#39; or &#39;cm_content&#39;).  | 
 **restore_archived_content_request** | [**RestoreArchivedContentRequest**](RestoreArchivedContentRequest.md)| Restore content from archive request parameters. At the moment there is one parameter being supported which is restore priority. &#39;High&#39; restore priority translates to &#39;Expedited&#39; Glacier restore tier in AWS S3 and &#39;High&#39; rehydrate priority in Azure Blob. &#39;Standard&#39; restore priority translates to &#39;Standard&#39; Glacier restore tier in AWS S3 and &#39;Standard&#39; rehydrate priority in Azure Blob. Body is not mandatory. High restore priority request body example: &#x60;&#x60;&#x60;JSON {   \&quot;restorePriority\&quot;: \&quot;High\&quot; } &#x60;&#x60;&#x60; Standard restore priority request body example: &#x60;&#x60;&#x60;JSON {   \&quot;restorePriority\&quot;: \&quot;Standard\&quot; } &#x60;&#x60;&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful response (request accepted) |  -  |
**400** | Invalid parameter: n**nodeId** or **contentPropName** is not a valid format, or is not a file Content&#39;s storage state does not allow restore. Invalid restore paramters.  |  -  |
**401** | Authentication failed |  -  |
**403** | Not authorized |  -  |
**404** | **nodeId** or **contentPropName** does not exist  |  -  |
**409** | Content already restored or restoration is already in progress |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_restore_version_content_from_archive**
> request_restore_version_content_from_archive(node_id, version_id, content_prop_name, restore_archived_content_request=restore_archived_content_request)

Request to restore given version content from archive

**Note:** this endpoint is available in Alfresco 7.2.0 and newer versions. It also requires at least one specific implementation of underlying functionality in Cloud Connector(s).  Request to restore given version content from archive. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import alfresco_core_api_client
from alfresco_core_api_client.models.restore_archived_content_request import RestoreArchivedContentRequest
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
    api_instance = alfresco_core_api_client.StorageInfoApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
    content_prop_name = 'content_prop_name_example' # str | The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (':') or underscore ('_') character (e.g., 'cm:content' or 'cm_content'). 
    restore_archived_content_request = alfresco_core_api_client.RestoreArchivedContentRequest() # RestoreArchivedContentRequest | Restore content from archive request parameters. At the moment there is one parameter being supported which is restore priority. 'High' restore priority translates to 'Expedited' Glacier restore tier in AWS S3 and 'High' rehydrate priority in Azure Blob. 'Standard' restore priority translates to 'Standard' Glacier restore tier in AWS S3 and 'Standard' rehydrate priority in Azure Blob. Body is not mandatory. High restore priority request body example: ```JSON {   \"restorePriority\": \"High\" } ``` Standard restore priority request body example: ```JSON {   \"restorePriority\": \"Standard\" } ```  (optional)

    try:
        # Request to restore given version content from archive
        api_instance.request_restore_version_content_from_archive(node_id, version_id, content_prop_name, restore_archived_content_request=restore_archived_content_request)
    except Exception as e:
        print("Exception when calling StorageInfoApi->request_restore_version_content_from_archive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **content_prop_name** | **str**| The namespace-prefix property name of content. Delimiter between namespace-prefix and property name can be either colon (&#39;:&#39;) or underscore (&#39;_&#39;) character (e.g., &#39;cm:content&#39; or &#39;cm_content&#39;).  | 
 **restore_archived_content_request** | [**RestoreArchivedContentRequest**](RestoreArchivedContentRequest.md)| Restore content from archive request parameters. At the moment there is one parameter being supported which is restore priority. &#39;High&#39; restore priority translates to &#39;Expedited&#39; Glacier restore tier in AWS S3 and &#39;High&#39; rehydrate priority in Azure Blob. &#39;Standard&#39; restore priority translates to &#39;Standard&#39; Glacier restore tier in AWS S3 and &#39;Standard&#39; rehydrate priority in Azure Blob. Body is not mandatory. High restore priority request body example: &#x60;&#x60;&#x60;JSON {   \&quot;restorePriority\&quot;: \&quot;High\&quot; } &#x60;&#x60;&#x60; Standard restore priority request body example: &#x60;&#x60;&#x60;JSON {   \&quot;restorePriority\&quot;: \&quot;Standard\&quot; } &#x60;&#x60;&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful response (request accepted) |  -  |
**400** | Invalid parameter: **nodeId** or **versionId** or **contentPropName** is not a valid format, or is not a file Content&#39;s storage state does not allow restore. Invalid restore paramters.  |  -  |
**401** | Authentication failed |  -  |
**403** | Not authorized |  -  |
**404** | **nodeId** or **versionId** or **contentPropName** does not exist  |  -  |
**409** | Content already restored or restoration is already in progress |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

