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

from alfresco_core_api_client.models.node_body_update import NodeBodyUpdate

class TestNodeBodyUpdate(unittest.TestCase):
    """NodeBodyUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeBodyUpdate:
        """Test NodeBodyUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeBodyUpdate`
        """
        model = NodeBodyUpdate()
        if include_optional:
            return NodeBodyUpdate(
                name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.',
                node_type = '',
                aspect_names = [
                    ''
                    ],
                properties = {
                    'key' : ''
                    },
                permissions = alfresco_core_api_client.models.permissions_body.PermissionsBody(
                    is_inheritance_enabled = True, 
                    locally_set = [
                        alfresco_core_api_client.models.permission_element.PermissionElement(
                            authority_id = '', 
                            name = '', 
                            access_status = 'ALLOWED', )
                        ], )
            )
        else:
            return NodeBodyUpdate(
        )
        """

    def testNodeBodyUpdate(self):
        """Test NodeBodyUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
