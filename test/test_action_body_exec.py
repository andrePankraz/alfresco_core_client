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

from alfresco_core_api_client.models.action_body_exec import ActionBodyExec

class TestActionBodyExec(unittest.TestCase):
    """ActionBodyExec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionBodyExec:
        """Test ActionBodyExec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionBodyExec`
        """
        model = ActionBodyExec()
        if include_optional:
            return ActionBodyExec(
                action_definition_id = '',
                target_id = '',
                params = None
            )
        else:
            return ActionBodyExec(
                action_definition_id = '',
        )
        """

    def testActionBodyExec(self):
        """Test ActionBodyExec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()