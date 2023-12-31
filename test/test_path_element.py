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

from alfresco_core_api_client.models.path_element import PathElement

class TestPathElement(unittest.TestCase):
    """PathElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PathElement:
        """Test PathElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PathElement`
        """
        model = PathElement()
        if include_optional:
            return PathElement(
                id = '',
                name = '',
                node_type = '',
                aspect_names = [
                    ''
                    ]
            )
        else:
            return PathElement(
        )
        """

    def testPathElement(self):
        """Test PathElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
