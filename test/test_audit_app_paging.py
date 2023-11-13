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

from alfresco_core_api_client.models.audit_app_paging import AuditAppPaging

class TestAuditAppPaging(unittest.TestCase):
    """AuditAppPaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuditAppPaging:
        """Test AuditAppPaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuditAppPaging`
        """
        model = AuditAppPaging()
        if include_optional:
            return AuditAppPaging(
                list = alfresco_core_api_client.models.audit_app_paging_list.AuditAppPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.audit_app_entry.AuditAppEntry(
                            entry = alfresco_core_api_client.models.audit_app.AuditApp(
                                id = '', 
                                name = '', 
                                is_enabled = True, 
                                max_entry_id = 56, 
                                min_entry_id = 56, ), )
                        ], )
            )
        else:
            return AuditAppPaging(
        )
        """

    def testAuditAppPaging(self):
        """Test AuditAppPaging"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()