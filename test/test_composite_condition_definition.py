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

from alfresco_core_api_client.models.composite_condition_definition import CompositeConditionDefinition

class TestCompositeConditionDefinition(unittest.TestCase):
    """CompositeConditionDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompositeConditionDefinition:
        """Test CompositeConditionDefinition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompositeConditionDefinition`
        """
        model = CompositeConditionDefinition()
        if include_optional:
            return CompositeConditionDefinition(
                inverted = True,
                boolean_mode = 'and',
                composite_conditions = [
                    alfresco_core_api_client.models.composite_condition_definition.CompositeConditionDefinition(
                        inverted = True, 
                        boolean_mode = 'and', 
                        composite_conditions = [
                            alfresco_core_api_client.models.composite_condition_definition.CompositeConditionDefinition(
                                inverted = True, 
                                boolean_mode = 'and', 
                                simple_conditions = [
                                    alfresco_core_api_client.models.simple_condition_definition.SimpleConditionDefinition(
                                        field = '', 
                                        comparator = '', 
                                        parameter = '', )
                                    ], )
                            ], 
                        simple_conditions = [
                            alfresco_core_api_client.models.simple_condition_definition.SimpleConditionDefinition(
                                field = '', 
                                comparator = '', 
                                parameter = '', )
                            ], )
                    ],
                simple_conditions = [
                    alfresco_core_api_client.models.simple_condition_definition.SimpleConditionDefinition(
                        field = '', 
                        comparator = '', 
                        parameter = '', )
                    ]
            )
        else:
            return CompositeConditionDefinition(
        )
        """

    def testCompositeConditionDefinition(self):
        """Test CompositeConditionDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()