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

from alfresco_core_api_client.models.node_body_copy import NodeBodyCopy

class TestNodeBodyCopy(unittest.TestCase):
    """NodeBodyCopy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeBodyCopy:
        """Test NodeBodyCopy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeBodyCopy`
        """
        model = NodeBodyCopy()
        if include_optional:
            return NodeBodyCopy(
                target_parent_id = '',
                name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.'
            )
        else:
            return NodeBodyCopy(
                target_parent_id = '',
        )
        """

    def testNodeBodyCopy(self):
        """Test NodeBodyCopy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()