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

from alfresco_core_api_client.models.network_quota import NetworkQuota

class TestNetworkQuota(unittest.TestCase):
    """NetworkQuota unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkQuota:
        """Test NetworkQuota
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkQuota`
        """
        model = NetworkQuota()
        if include_optional:
            return NetworkQuota(
                id = '',
                limit = 56,
                usage = 56
            )
        else:
            return NetworkQuota(
                id = '',
                limit = 56,
                usage = 56,
        )
        """

    def testNetworkQuota(self):
        """Test NetworkQuota"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
