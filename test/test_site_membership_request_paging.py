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

from alfresco_core_api_client.models.site_membership_request_paging import SiteMembershipRequestPaging

class TestSiteMembershipRequestPaging(unittest.TestCase):
    """SiteMembershipRequestPaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiteMembershipRequestPaging:
        """Test SiteMembershipRequestPaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiteMembershipRequestPaging`
        """
        model = SiteMembershipRequestPaging()
        if include_optional:
            return SiteMembershipRequestPaging(
                list = alfresco_core_api_client.models.site_membership_request_paging_list.SiteMembershipRequestPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.site_membership_request_entry.SiteMembershipRequestEntry(
                            entry = alfresco_core_api_client.models.site_membership_request.SiteMembershipRequest(
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
                                message = '', ), )
                        ], )
            )
        else:
            return SiteMembershipRequestPaging(
                list = alfresco_core_api_client.models.site_membership_request_paging_list.SiteMembershipRequestPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.site_membership_request_entry.SiteMembershipRequestEntry(
                            entry = alfresco_core_api_client.models.site_membership_request.SiteMembershipRequest(
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
                                message = '', ), )
                        ], ),
        )
        """

    def testSiteMembershipRequestPaging(self):
        """Test SiteMembershipRequestPaging"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()