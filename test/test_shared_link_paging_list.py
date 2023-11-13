# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from alfresco_core_api_client.models.shared_link_paging_list import SharedLinkPagingList

class TestSharedLinkPagingList(unittest.TestCase):
    """SharedLinkPagingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SharedLinkPagingList:
        """Test SharedLinkPagingList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SharedLinkPagingList`
        """
        model = SharedLinkPagingList()
        if include_optional:
            return SharedLinkPagingList(
                pagination = alfresco_core_api_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ),
                entries = [
                    alfresco_core_api_client.models.shared_link_entry.SharedLinkEntry(
                        entry = alfresco_core_api_client.models.shared_link.SharedLink(
                            id = '', 
                            expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            node_id = '', 
                            name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.', 
                            title = '', 
                            description = '', 
                            modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            modified_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                                display_name = '', 
                                id = '', ), 
                            shared_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                                display_name = '', 
                                id = '', ), 
                            content = alfresco_core_api_client.models.content_info.ContentInfo(
                                mime_type = '', 
                                mime_type_name = '', 
                                size_in_bytes = 56, 
                                encoding = '', ), 
                            allowable_operations = [
                                ''
                                ], 
                            allowable_operations_on_target = [
                                ''
                                ], 
                            is_favorite = True, 
                            properties = alfresco_core_api_client.models.properties.properties(), 
                            aspect_names = [
                                ''
                                ], 
                            path = alfresco_core_api_client.models.path_info.PathInfo(
                                elements = [
                                    alfresco_core_api_client.models.path_element.PathElement(
                                        id = '', 
                                        name = '', 
                                        node_type = '', )
                                    ], 
                                name = '', 
                                is_complete = True, ), ), )
                    ]
            )
        else:
            return SharedLinkPagingList(
                pagination = alfresco_core_api_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ),
                entries = [
                    alfresco_core_api_client.models.shared_link_entry.SharedLinkEntry(
                        entry = alfresco_core_api_client.models.shared_link.SharedLink(
                            id = '', 
                            expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            node_id = '', 
                            name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.', 
                            title = '', 
                            description = '', 
                            modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            modified_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                                display_name = '', 
                                id = '', ), 
                            shared_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                                display_name = '', 
                                id = '', ), 
                            content = alfresco_core_api_client.models.content_info.ContentInfo(
                                mime_type = '', 
                                mime_type_name = '', 
                                size_in_bytes = 56, 
                                encoding = '', ), 
                            allowable_operations = [
                                ''
                                ], 
                            allowable_operations_on_target = [
                                ''
                                ], 
                            is_favorite = True, 
                            properties = alfresco_core_api_client.models.properties.properties(), 
                            aspect_names = [
                                ''
                                ], 
                            path = alfresco_core_api_client.models.path_info.PathInfo(
                                elements = [
                                    alfresco_core_api_client.models.path_element.PathElement(
                                        id = '', 
                                        name = '', 
                                        node_type = '', )
                                    ], 
                                name = '', 
                                is_complete = True, ), ), )
                    ],
        )
        """

    def testSharedLinkPagingList(self):
        """Test SharedLinkPagingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
