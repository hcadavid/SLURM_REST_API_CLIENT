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

from openapi_client.models.v0038_meta_slurm_version import V0038MetaSlurmVersion

class TestV0038MetaSlurmVersion(unittest.TestCase):
    """V0038MetaSlurmVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038MetaSlurmVersion:
        """Test V0038MetaSlurmVersion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038MetaSlurmVersion`
        """
        model = V0038MetaSlurmVersion()
        if include_optional:
            return V0038MetaSlurmVersion(
                major = 56,
                micro = 56,
                minor = 56
            )
        else:
            return V0038MetaSlurmVersion(
        )
        """

    def testV0038MetaSlurmVersion(self):
        """Test V0038MetaSlurmVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
