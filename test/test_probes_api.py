# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alfresco_core_api_client.api.probes_api import ProbesApi


class TestProbesApi(unittest.TestCase):
    """ProbesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProbesApi()

    def tearDown(self) -> None:
        pass

    def test_get_probe(self) -> None:
        """Test case for get_probe

        Check readiness and liveness of the repository
        """
        pass


if __name__ == '__main__':
    unittest.main()
