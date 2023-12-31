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

from alfresco_core_api_client.models.node_association_paging import NodeAssociationPaging

class TestNodeAssociationPaging(unittest.TestCase):
    """NodeAssociationPaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeAssociationPaging:
        """Test NodeAssociationPaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeAssociationPaging`
        """
        model = NodeAssociationPaging()
        if include_optional:
            return NodeAssociationPaging(
                list = alfresco_core_api_client.models.node_association_paging_list.NodeAssociationPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.node_association_entry.NodeAssociationEntry(
                            entry = null, )
                        ], 
                    source = alfresco_core_api_client.models.node.Node(
                        id = '', 
                        name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.', 
                        node_type = '', 
                        is_folder = True, 
                        is_file = True, 
                        is_locked = True, 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                            display_name = '', 
                            id = '', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by_user = alfresco_core_api_client.models.user_info.UserInfo(
                            display_name = '', 
                            id = '', ), 
                        parent_id = '', 
                        is_link = True, 
                        is_favorite = True, 
                        is_direct_link_enabled = True, 
                        content = alfresco_core_api_client.models.content_info.ContentInfo(
                            mime_type = '', 
                            mime_type_name = '', 
                            size_in_bytes = 56, 
                            encoding = '', ), 
                        aspect_names = [
                            ''
                            ], 
                        properties = alfresco_core_api_client.models.properties.properties(), 
                        allowable_operations = [
                            ''
                            ], 
                        path = alfresco_core_api_client.models.path_info.PathInfo(
                            elements = [
                                alfresco_core_api_client.models.path_element.PathElement(
                                    id = '', 
                                    name = '', 
                                    node_type = '', )
                                ], 
                            name = '', 
                            is_complete = True, ), 
                        permissions = alfresco_core_api_client.models.permissions_info.PermissionsInfo(
                            is_inheritance_enabled = True, 
                            inherited = [
                                alfresco_core_api_client.models.permission_element.PermissionElement(
                                    authority_id = '', 
                                    name = '', 
                                    access_status = 'ALLOWED', )
                                ], 
                            locally_set = [
                                alfresco_core_api_client.models.permission_element.PermissionElement(
                                    authority_id = '', 
                                    name = '', 
                                    access_status = 'ALLOWED', )
                                ], 
                            settable = [
                                ''
                                ], ), 
                        definition = alfresco_core_api_client.models.definition.Definition(
                            properties = [
                                alfresco_core_api_client.models.property.Property(
                                    id = '', 
                                    title = '', 
                                    description = '', 
                                    default_value = '', 
                                    data_type = '', 
                                    is_multi_valued = True, 
                                    is_mandatory = True, 
                                    is_mandatory_enforced = True, 
                                    is_protected = True, 
                                    constraints = [
                                        alfresco_core_api_client.models.constraint.Constraint(
                                            id = '', 
                                            type = '', 
                                            title = '', 
                                            description = '', 
                                            parameters = {
                                                'key' : None
                                                }, )
                                        ], )
                                ], ), ), )
            )
        else:
            return NodeAssociationPaging(
        )
        """

    def testNodeAssociationPaging(self):
        """Test NodeAssociationPaging"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
