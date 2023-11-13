# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alfresco_core_api_client.api.actions_api import ActionsApi


class TestActionsApi(unittest.TestCase):
    """ActionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActionsApi()

    def tearDown(self) -> None:
        pass

    def test_action_details(self) -> None:
        """Test case for action_details

        Retrieve the details of an action definition
        """
        pass

    def test_action_exec(self) -> None:
        """Test case for action_exec

        Execute an action
        """
        pass

    def test_get_action_constraint(self) -> None:
        """Test case for get_action_constraint

        Retrieve an action parameter constraint by requested name
        """
        pass

    def test_list_actions(self) -> None:
        """Test case for list_actions

        Retrieve list of available actions
        """
        pass

    def test_node_actions(self) -> None:
        """Test case for node_actions

        Retrieve actions for a node
        """
        pass


if __name__ == '__main__':
    unittest.main()
