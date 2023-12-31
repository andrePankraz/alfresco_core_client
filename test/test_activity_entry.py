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

from alfresco_core_api_client.models.activity_entry import ActivityEntry

class TestActivityEntry(unittest.TestCase):
    """ActivityEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityEntry:
        """Test ActivityEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityEntry`
        """
        model = ActivityEntry()
        if include_optional:
            return ActivityEntry(
                entry = alfresco_core_api_client.models.activity.Activity(
                    post_person_id = '', 
                    id = 56, 
                    site_id = '', 
                    posted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    feed_person_id = '', 
                    activity_summary = {
                        'key' : ''
                        }, 
                    activity_type = '', )
            )
        else:
            return ActivityEntry(
                entry = alfresco_core_api_client.models.activity.Activity(
                    post_person_id = '', 
                    id = 56, 
                    site_id = '', 
                    posted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    feed_person_id = '', 
                    activity_summary = {
                        'key' : ''
                        }, 
                    activity_type = '', ),
        )
        """

    def testActivityEntry(self):
        """Test ActivityEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
