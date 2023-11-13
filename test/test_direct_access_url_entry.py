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

from alfresco_core_api_client.models.direct_access_url_entry import DirectAccessUrlEntry

class TestDirectAccessUrlEntry(unittest.TestCase):
    """DirectAccessUrlEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectAccessUrlEntry:
        """Test DirectAccessUrlEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectAccessUrlEntry`
        """
        model = DirectAccessUrlEntry()
        if include_optional:
            return DirectAccessUrlEntry(
                entry = alfresco_core_api_client.models.direct_access_url.DirectAccessUrl(
                    content_url = '', 
                    attachment = True, 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return DirectAccessUrlEntry(
                entry = alfresco_core_api_client.models.direct_access_url.DirectAccessUrl(
                    content_url = '', 
                    attachment = True, 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testDirectAccessUrlEntry(self):
        """Test DirectAccessUrlEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()