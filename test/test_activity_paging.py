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

from alfresco_core_api_client.models.activity_paging import ActivityPaging

class TestActivityPaging(unittest.TestCase):
    """ActivityPaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityPaging:
        """Test ActivityPaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityPaging`
        """
        model = ActivityPaging()
        if include_optional:
            return ActivityPaging(
                list = alfresco_core_api_client.models.activity_paging_list.ActivityPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.activity_entry.ActivityEntry(
                            entry = alfresco_core_api_client.models.activity.Activity(
                                post_person_id = '', 
                                id = 56, 
                                site_id = '', 
                                posted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                feed_person_id = '', 
                                activity_summary = {
                                    'key' : ''
                                    }, 
                                activity_type = '', ), )
                        ], )
            )
        else:
            return ActivityPaging(
                list = alfresco_core_api_client.models.activity_paging_list.ActivityPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.activity_entry.ActivityEntry(
                            entry = alfresco_core_api_client.models.activity.Activity(
                                post_person_id = '', 
                                id = 56, 
                                site_id = '', 
                                posted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                feed_person_id = '', 
                                activity_summary = {
                                    'key' : ''
                                    }, 
                                activity_type = '', ), )
                        ], ),
        )
        """

    def testActivityPaging(self):
        """Test ActivityPaging"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
