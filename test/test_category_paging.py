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

from alfresco_core_api_client.models.category_paging import CategoryPaging

class TestCategoryPaging(unittest.TestCase):
    """CategoryPaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryPaging:
        """Test CategoryPaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryPaging`
        """
        model = CategoryPaging()
        if include_optional:
            return CategoryPaging(
                list = alfresco_core_api_client.models.category_paging_list.CategoryPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.category_entry.CategoryEntry(
                            entry = alfresco_core_api_client.models.category.Category(
                                id = '', 
                                name = '', 
                                parent_id = '', 
                                has_children = True, 
                                count = 1.337, 
                                path = '', ), )
                        ], )
            )
        else:
            return CategoryPaging(
                list = alfresco_core_api_client.models.category_paging_list.CategoryPaging_list(
                    pagination = alfresco_core_api_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        alfresco_core_api_client.models.category_entry.CategoryEntry(
                            entry = alfresco_core_api_client.models.category.Category(
                                id = '', 
                                name = '', 
                                parent_id = '', 
                                has_children = True, 
                                count = 1.337, 
                                path = '', ), )
                        ], ),
        )
        """

    def testCategoryPaging(self):
        """Test CategoryPaging"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
