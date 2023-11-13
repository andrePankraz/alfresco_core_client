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

from alfresco_core_api_client.models.preference_entry import PreferenceEntry

class TestPreferenceEntry(unittest.TestCase):
    """PreferenceEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PreferenceEntry:
        """Test PreferenceEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PreferenceEntry`
        """
        model = PreferenceEntry()
        if include_optional:
            return PreferenceEntry(
                entry = alfresco_core_api_client.models.preference.Preference(
                    id = '', 
                    value = '', )
            )
        else:
            return PreferenceEntry(
                entry = alfresco_core_api_client.models.preference.Preference(
                    id = '', 
                    value = '', ),
        )
        """

    def testPreferenceEntry(self):
        """Test PreferenceEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
