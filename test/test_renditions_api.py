# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alfresco_core_api_client.api.renditions_api import RenditionsApi


class TestRenditionsApi(unittest.TestCase):
    """RenditionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RenditionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_rendition(self) -> None:
        """Test case for create_rendition

        Create rendition
        """
        pass

    def test_delete_rendition(self) -> None:
        """Test case for delete_rendition

        Delete rendition
        """
        pass

    def test_get_rendition(self) -> None:
        """Test case for get_rendition

        Get rendition information
        """
        pass

    def test_get_rendition_content(self) -> None:
        """Test case for get_rendition_content

        Get rendition content
        """
        pass

    def test_list_renditions(self) -> None:
        """Test case for list_renditions

        List renditions
        """
        pass

    def test_request_rendition_direct_access_url(self) -> None:
        """Test case for request_rendition_direct_access_url

        Generate a direct access content URL
        """
        pass


if __name__ == '__main__':
    unittest.main()