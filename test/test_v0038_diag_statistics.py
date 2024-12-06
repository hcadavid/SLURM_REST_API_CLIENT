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

from openapi_client.models.v0038_diag_statistics import V0038DiagStatistics

class TestV0038DiagStatistics(unittest.TestCase):
    """V0038DiagStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038DiagStatistics:
        """Test V0038DiagStatistics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038DiagStatistics`
        """
        model = V0038DiagStatistics()
        if include_optional:
            return V0038DiagStatistics(
                parts_packed = 56,
                req_time = 56,
                req_time_start = 56,
                server_thread_count = 56,
                agent_queue_size = 56,
                agent_count = 56,
                agent_thread_count = 56,
                dbd_agent_queue_size = 56,
                gettimeofday_latency = 56,
                schedule_cycle_max = 56,
                schedule_cycle_last = 56,
                schedule_cycle_total = 56,
                schedule_cycle_mean = 56,
                schedule_cycle_mean_depth = 56,
                schedule_cycle_per_minute = 56,
                schedule_queue_length = 56,
                jobs_submitted = 56,
                jobs_started = 56,
                jobs_completed = 56,
                jobs_canceled = 56,
                jobs_failed = 56,
                jobs_pending = 56,
                jobs_running = 56,
                job_states_ts = 56,
                bf_backfilled_jobs = 56,
                bf_last_backfilled_jobs = 56,
                bf_backfilled_het_jobs = 56,
                bf_cycle_counter = 56,
                bf_cycle_mean = 56,
                bf_cycle_max = 56,
                bf_last_depth = 56,
                bf_last_depth_try = 56,
                bf_depth_mean = 56,
                bf_depth_mean_try = 56,
                bf_cycle_last = 56,
                bf_queue_len = 56,
                bf_queue_len_mean = 56,
                bf_table_size = 56,
                bf_table_size_mean = 56,
                bf_when_last_cycle = 56,
                bf_active = True,
                rpcs_by_message_type = [
                    {"average_time":7,"type_id":3,"count":3,"message_type":"message_type","total_time":5}
                    ],
                rpcs_by_user = [
                    {"average_time":0,"user_id":3,"count":4,"total_time":6,"user":"user"}
                    ]
            )
        else:
            return V0038DiagStatistics(
        )
        """

    def testV0038DiagStatistics(self):
        """Test V0038DiagStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
