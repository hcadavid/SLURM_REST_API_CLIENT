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

from openapi_client.models.v0038_node import V0038Node

class TestV0038Node(unittest.TestCase):
    """V0038Node unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038Node:
        """Test V0038Node
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038Node`
        """
        model = V0038Node()
        if include_optional:
            return V0038Node(
                architecture = '',
                burstbuffer_network_address = '',
                boards = 56,
                boot_time = 56,
                cores = 56,
                cpu_binding = 56,
                cpu_load = 56,
                free_memory = 56,
                cpus = 56,
                features = '',
                active_features = '',
                gres = '',
                gres_drained = '',
                gres_used = '',
                mcs_label = '',
                name = '',
                next_state_after_reboot = '',
                next_state_after_reboot_flags = [
                    ''
                    ],
                address = '',
                hostname = '',
                state = '',
                state_flags = [
                    ''
                    ],
                operating_system = '',
                owner = '',
                partitions = [
                    ''
                    ],
                port = 56,
                real_memory = 56,
                reason = '',
                reason_changed_at = 56,
                reason_set_by_user = '',
                slurmd_start_time = 56,
                sockets = 56,
                threads = 56,
                temporary_disk = 56,
                weight = 56,
                tres = '',
                tres_used = '',
                tres_weighted = 1.337,
                slurmd_version = '',
                alloc_cpus = 56,
                idle_cpus = 56,
                alloc_memory = 56
            )
        else:
            return V0038Node(
        )
        """

    def testV0038Node(self):
        """Test V0038Node"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
