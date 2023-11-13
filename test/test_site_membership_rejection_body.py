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

from alfresco_core_api_client.models.site_membership_rejection_body import SiteMembershipRejectionBody

class TestSiteMembershipRejectionBody(unittest.TestCase):
    """SiteMembershipRejectionBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiteMembershipRejectionBody:
        """Test SiteMembershipRejectionBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiteMembershipRejectionBody`
        """
        model = SiteMembershipRejectionBody()
        if include_optional:
            return SiteMembershipRejectionBody(
                comment = ''
            )
        else:
            return SiteMembershipRejectionBody(
        )
        """

    def testSiteMembershipRejectionBody(self):
        """Test SiteMembershipRejectionBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
