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

from alfresco_core_api_client.models.direct_access_url_body_create import DirectAccessUrlBodyCreate

class TestDirectAccessUrlBodyCreate(unittest.TestCase):
    """DirectAccessUrlBodyCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectAccessUrlBodyCreate:
        """Test DirectAccessUrlBodyCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectAccessUrlBodyCreate`
        """
        model = DirectAccessUrlBodyCreate()
        if include_optional:
            return DirectAccessUrlBodyCreate(
                attachment = True
            )
        else:
            return DirectAccessUrlBodyCreate(
        )
        """

    def testDirectAccessUrlBodyCreate(self):
        """Test DirectAccessUrlBodyCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
