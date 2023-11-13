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

from alfresco_core_api_client.models.comment_paging import CommentPaging

class TestCommentPaging(unittest.TestCase):
    """CommentPaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentPaging:
        """Test CommentPaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentPaging`
        """
        model = CommentPaging()
        if include_optional:
            return CommentPaging(
                list = alfresco_core_api_client.models.comment_paging_list.CommentPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.comment_entry.CommentEntry(
                            entry = alfresco_core_api_client.models.comment.Comment(
                                id = '', 
                                title = '', 
                                content = '', 
                                created_by = alfresco_core_api_client.models.person.Person(
                                    id = '', 
                                    first_name = '', 
                                    last_name = '', 
                                    display_name = '', 
                                    description = '', 
                                    avatar_id = '', 
                                    email = '', 
                                    skype_id = '', 
                                    google_id = '', 
                                    instant_message_id = '', 
                                    job_title = '', 
                                    location = '', 
                                    company = alfresco_core_api_client.models.company.Company(
                                        organization = '', 
                                        address1 = '', 
                                        address2 = '', 
                                        address3 = '', 
                                        postcode = '', 
                                        telephone = '', 
                                        fax = '', 
                                        email = '', ), 
                                    mobile = '', 
                                    telephone = '', 
                                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    user_status = '', 
                                    enabled = True, 
                                    email_notifications_enabled = True, 
                                    aspect_names = [
                                        ''
                                        ], 
                                    properties = alfresco_core_api_client.models.properties.properties(), 
                                    capabilities = alfresco_core_api_client.models.capabilities.Capabilities(
                                        is_admin = True, 
                                        is_guest = True, 
                                        is_mutable = True, ), ), 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                edited = True, 
                                modified_by = alfresco_core_api_client.models.person.Person(
                                    id = '', 
                                    first_name = '', 
                                    last_name = '', 
                                    display_name = '', 
                                    description = '', 
                                    avatar_id = '', 
                                    email = '', 
                                    skype_id = '', 
                                    google_id = '', 
                                    instant_message_id = '', 
                                    job_title = '', 
                                    location = '', 
                                    mobile = '', 
                                    telephone = '', 
                                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    user_status = '', 
                                    enabled = True, 
                                    email_notifications_enabled = True, 
                                    properties = alfresco_core_api_client.models.properties.properties(), ), 
                                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                can_edit = True, 
                                can_delete = True, ), )
                        ], )
            )
        else:
            return CommentPaging(
                list = alfresco_core_api_client.models.comment_paging_list.CommentPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.comment_entry.CommentEntry(
                            entry = alfresco_core_api_client.models.comment.Comment(
                                id = '', 
                                title = '', 
                                content = '', 
                                created_by = alfresco_core_api_client.models.person.Person(
                                    id = '', 
                                    first_name = '', 
                                    last_name = '', 
                                    display_name = '', 
                                    description = '', 
                                    avatar_id = '', 
                                    email = '', 
                                    skype_id = '', 
                                    google_id = '', 
                                    instant_message_id = '', 
                                    job_title = '', 
                                    location = '', 
                                    company = alfresco_core_api_client.models.company.Company(
                                        organization = '', 
                                        address1 = '', 
                                        address2 = '', 
                                        address3 = '', 
                                        postcode = '', 
                                        telephone = '', 
                                        fax = '', 
                                        email = '', ), 
                                    mobile = '', 
                                    telephone = '', 
                                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    user_status = '', 
                                    enabled = True, 
                                    email_notifications_enabled = True, 
                                    aspect_names = [
                                        ''
                                        ], 
                                    properties = alfresco_core_api_client.models.properties.properties(), 
                                    capabilities = alfresco_core_api_client.models.capabilities.Capabilities(
                                        is_admin = True, 
                                        is_guest = True, 
                                        is_mutable = True, ), ), 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                edited = True, 
                                modified_by = alfresco_core_api_client.models.person.Person(
                                    id = '', 
                                    first_name = '', 
                                    last_name = '', 
                                    display_name = '', 
                                    description = '', 
                                    avatar_id = '', 
                                    email = '', 
                                    skype_id = '', 
                                    google_id = '', 
                                    instant_message_id = '', 
                                    job_title = '', 
                                    location = '', 
                                    mobile = '', 
                                    telephone = '', 
                                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    user_status = '', 
                                    enabled = True, 
                                    email_notifications_enabled = True, 
                                    properties = alfresco_core_api_client.models.properties.properties(), ), 
                                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                can_edit = True, 
                                can_delete = True, ), )
                        ], ),
        )
        """

    def testCommentPaging(self):
        """Test CommentPaging"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
