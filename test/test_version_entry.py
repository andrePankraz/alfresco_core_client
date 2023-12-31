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

from alfresco_core_api_client.models.version_entry import VersionEntry

class TestVersionEntry(unittest.TestCase):
    """VersionEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VersionEntry:
        """Test VersionEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VersionEntry`
        """
        model = VersionEntry()
        if include_optional:
            return VersionEntry(
                entry = alfresco_core_api_client.models.version.Version(
                    id = '', 
                    version_comment = '', 
                    name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.', 
                    node_type = '', 
                    is_folder = True, 
                    is_file = True, 
                    modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                        display_name = '', 
                        id = '', ), 
                    content = alfresco_core_api_client.models.content_info.ContentInfo(
                        mime_type = '', 
                        mime_type_name = '', 
                        size_in_bytes = 56, 
                        encoding = '', ), 
                    aspect_names = [
                        ''
                        ], 
                    properties = alfresco_core_api_client.models.properties.properties(), )
            )
        else:
            return VersionEntry(
        )
        """

    def testVersionEntry(self):
        """Test VersionEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
