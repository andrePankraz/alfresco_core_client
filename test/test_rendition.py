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

from alfresco_core_api_client.models.rendition import Rendition

class TestRendition(unittest.TestCase):
    """Rendition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Rendition:
        """Test Rendition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Rendition`
        """
        model = Rendition()
        if include_optional:
            return Rendition(
                id = '',
                content = alfresco_core_api_client.models.content_info.ContentInfo(
                    mime_type = '', 
                    mime_type_name = '', 
                    size_in_bytes = 56, 
                    encoding = '', ),
                status = 'CREATED'
            )
        else:
            return Rendition(
        )
        """

    def testRendition(self):
        """Test Rendition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()