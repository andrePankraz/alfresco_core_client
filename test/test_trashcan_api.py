# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alfresco_core_api_client.api.trashcan_api import TrashcanApi


class TestTrashcanApi(unittest.TestCase):
    """TrashcanApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TrashcanApi()

    def tearDown(self) -> None:
        pass

    def test_delete_deleted_node(self) -> None:
        """Test case for delete_deleted_node

        Permanently delete a deleted node
        """
        pass

    def test_get_archived_node_rendition(self) -> None:
        """Test case for get_archived_node_rendition

        Get rendition information for a deleted node
        """
        pass

    def test_get_archived_node_rendition_content(self) -> None:
        """Test case for get_archived_node_rendition_content

        Get rendition content of a deleted node
        """
        pass

    def test_get_deleted_node(self) -> None:
        """Test case for get_deleted_node

        Get a deleted node
        """
        pass

    def test_get_deleted_node_content(self) -> None:
        """Test case for get_deleted_node_content

        Get deleted node content
        """
        pass

    def test_list_deleted_node_renditions(self) -> None:
        """Test case for list_deleted_node_renditions

        List renditions for a deleted node
        """
        pass

    def test_list_deleted_nodes(self) -> None:
        """Test case for list_deleted_nodes

        List deleted nodes
        """
        pass

    def test_request_archived_node_rendition_direct_access_url(self) -> None:
        """Test case for request_archived_node_rendition_direct_access_url

        Generate a direct access content URL
        """
        pass

    def test_request_deleted_node_direct_access_url(self) -> None:
        """Test case for request_deleted_node_direct_access_url

        Generate a direct access content URL
        """
        pass

    def test_restore_deleted_node(self) -> None:
        """Test case for restore_deleted_node

        Restore a deleted node
        """
        pass


if __name__ == '__main__':
    unittest.main()
