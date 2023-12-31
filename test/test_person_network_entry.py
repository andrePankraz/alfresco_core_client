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

from alfresco_core_api_client.models.person_network_entry import PersonNetworkEntry

class TestPersonNetworkEntry(unittest.TestCase):
    """PersonNetworkEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonNetworkEntry:
        """Test PersonNetworkEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonNetworkEntry`
        """
        model = PersonNetworkEntry()
        if include_optional:
            return PersonNetworkEntry(
                entry = alfresco_core_api_client.models.person_network.PersonNetwork(
                    id = '', 
                    home_network = True, 
                    is_enabled = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    paid_network = True, 
                    subscription_level = 'Free', 
                    quotas = [
                        alfresco_core_api_client.models.network_quota.NetworkQuota(
                            id = '', 
                            limit = 56, 
                            usage = 56, )
                        ], )
            )
        else:
            return PersonNetworkEntry(
                entry = alfresco_core_api_client.models.person_network.PersonNetwork(
                    id = '', 
                    home_network = True, 
                    is_enabled = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    paid_network = True, 
                    subscription_level = 'Free', 
                    quotas = [
                        alfresco_core_api_client.models.network_quota.NetworkQuota(
                            id = '', 
                            limit = 56, 
                            usage = 56, )
                        ], ),
        )
        """

    def testPersonNetworkEntry(self):
        """Test PersonNetworkEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
