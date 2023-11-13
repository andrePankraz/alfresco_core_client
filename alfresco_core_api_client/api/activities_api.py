# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictStr

from typing import List, Optional

from alfresco_core_api_client.models.activity_paging import ActivityPaging

from alfresco_core_api_client.api_client import ApiClient
from alfresco_core_api_client.api_response import ApiResponse
from alfresco_core_api_client.rest import RESTResponseType


class ActivitiesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list_activities_for_person(
        self,
        person_id: Annotated[StrictStr, Field(description="The identifier of a person.")],
        skip_count: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. ")] = None,
        max_items: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The maximum number of items to return in the list. If not supplied then the default value is 100. ")] = None,
        who: Annotated[Optional[StrictStr], Field(description="A filter to include the user's activities only `me`, other user's activities only `others`' ")] = None,
        site_id: Annotated[Optional[StrictStr], Field(description="Include only activity feed entries relating to this site.")] = None,
        fields: Annotated[Optional[List[StrictStr]], Field(description="A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ActivityPaging:
        """List activities

        Gets a list of activities for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

        :param person_id: The identifier of a person. (required)
        :type person_id: str
        :param skip_count: The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. 
        :type skip_count: int
        :param max_items: The maximum number of items to return in the list. If not supplied then the default value is 100. 
        :type max_items: int
        :param who: A filter to include the user's activities only `me`, other user's activities only `others`' 
        :type who: str
        :param site_id: Include only activity feed entries relating to this site.
        :type site_id: str
        :param fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :type fields: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_activities_for_person_serialize(
            person_id=person_id,
            skip_count=skip_count,
            max_items=max_items,
            who=who,
            site_id=site_id,
            fields=fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActivityPaging",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_activities_for_person_with_http_info(
        self,
        person_id: Annotated[StrictStr, Field(description="The identifier of a person.")],
        skip_count: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. ")] = None,
        max_items: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The maximum number of items to return in the list. If not supplied then the default value is 100. ")] = None,
        who: Annotated[Optional[StrictStr], Field(description="A filter to include the user's activities only `me`, other user's activities only `others`' ")] = None,
        site_id: Annotated[Optional[StrictStr], Field(description="Include only activity feed entries relating to this site.")] = None,
        fields: Annotated[Optional[List[StrictStr]], Field(description="A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ActivityPaging]:
        """List activities

        Gets a list of activities for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

        :param person_id: The identifier of a person. (required)
        :type person_id: str
        :param skip_count: The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. 
        :type skip_count: int
        :param max_items: The maximum number of items to return in the list. If not supplied then the default value is 100. 
        :type max_items: int
        :param who: A filter to include the user's activities only `me`, other user's activities only `others`' 
        :type who: str
        :param site_id: Include only activity feed entries relating to this site.
        :type site_id: str
        :param fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :type fields: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_activities_for_person_serialize(
            person_id=person_id,
            skip_count=skip_count,
            max_items=max_items,
            who=who,
            site_id=site_id,
            fields=fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActivityPaging",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_activities_for_person_without_preload_content(
        self,
        person_id: Annotated[StrictStr, Field(description="The identifier of a person.")],
        skip_count: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. ")] = None,
        max_items: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The maximum number of items to return in the list. If not supplied then the default value is 100. ")] = None,
        who: Annotated[Optional[StrictStr], Field(description="A filter to include the user's activities only `me`, other user's activities only `others`' ")] = None,
        site_id: Annotated[Optional[StrictStr], Field(description="Include only activity feed entries relating to this site.")] = None,
        fields: Annotated[Optional[List[StrictStr]], Field(description="A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List activities

        Gets a list of activities for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

        :param person_id: The identifier of a person. (required)
        :type person_id: str
        :param skip_count: The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0. 
        :type skip_count: int
        :param max_items: The maximum number of items to return in the list. If not supplied then the default value is 100. 
        :type max_items: int
        :param who: A filter to include the user's activities only `me`, other user's activities only `others`' 
        :type who: str
        :param site_id: Include only activity feed entries relating to this site.
        :type site_id: str
        :param fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :type fields: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_activities_for_person_serialize(
            person_id=person_id,
            skip_count=skip_count,
            max_items=max_items,
            who=who,
            site_id=site_id,
            fields=fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActivityPaging",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_activities_for_person_serialize(
        self,
        person_id,
        skip_count,
        max_items,
        who,
        site_id,
        fields,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
            'fields': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if person_id is not None:
            _path_params['personId'] = person_id
        # process the query parameters
        if skip_count is not None:
            
            _query_params.append(('skipCount', skip_count))
            
        if max_items is not None:
            
            _query_params.append(('maxItems', max_items))
            
        if who is not None:
            
            _query_params.append(('who', who))
            
        if site_id is not None:
            
            _query_params.append(('siteId', site_id))
            
        if fields is not None:
            
            _query_params.append(('fields', fields))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'basicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/people/{personId}/activities',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


