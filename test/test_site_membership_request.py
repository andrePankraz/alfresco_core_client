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

from alfresco_core_api_client.models.site_membership_request import SiteMembershipRequest

class TestSiteMembershipRequest(unittest.TestCase):
    """SiteMembershipRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiteMembershipRequest:
        """Test SiteMembershipRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiteMembershipRequest`
        """
        model = SiteMembershipRequest()
        if include_optional:
            return SiteMembershipRequest(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                site = alfresco_core_api_client.models.site.Site(
                    id = '', 
                    guid = '', 
                    title = '', 
                    description = '', 
                    visibility = 'PRIVATE', 
                    preset = '', 
                    role = 'SiteConsumer', ),
                message = ''
            )
        else:
            return SiteMembershipRequest(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                site = alfresco_core_api_client.models.site.Site(
                    id = '', 
                    guid = '', 
                    title = '', 
                    description = '', 
                    visibility = 'PRIVATE', 
                    preset = '', 
                    role = 'SiteConsumer', ),
        )
        """

    def testSiteMembershipRequest(self):
        """Test SiteMembershipRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
