# coding: utf-8

"""
    Slurm Rest API RO

    API to access Slurm. Only GET requests are implemented.

    The version of the OpenAPI document: 0.0.38
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v0038_node_allocation import V0038NodeAllocation

class TestV0038NodeAllocation(unittest.TestCase):
    """V0038NodeAllocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038NodeAllocation:
        """Test V0038NodeAllocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038NodeAllocation`
        """
        model = V0038NodeAllocation()
        if include_optional:
            return V0038NodeAllocation(
                memory = 56,
                cpus = 56,
                sockets = {"cores":"{}"},
                nodename = ''
            )
        else:
            return V0038NodeAllocation(
        )
        """

    def testV0038NodeAllocation(self):
        """Test V0038NodeAllocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
