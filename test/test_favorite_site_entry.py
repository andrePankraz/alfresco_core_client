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

from alfresco_core_api_client.models.favorite_site_entry import FavoriteSiteEntry

class TestFavoriteSiteEntry(unittest.TestCase):
    """FavoriteSiteEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FavoriteSiteEntry:
        """Test FavoriteSiteEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FavoriteSiteEntry`
        """
        model = FavoriteSiteEntry()
        if include_optional:
            return FavoriteSiteEntry(
                entry = alfresco_core_api_client.models.favorite_site.FavoriteSite(
                    id = '', )
            )
        else:
            return FavoriteSiteEntry(
                entry = alfresco_core_api_client.models.favorite_site.FavoriteSite(
                    id = '', ),
        )
        """

    def testFavoriteSiteEntry(self):
        """Test FavoriteSiteEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
