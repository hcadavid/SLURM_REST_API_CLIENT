# coding: utf-8

# flake8: noqa
"""
    Slurm Rest API RO

    API to access Slurm. Only GET requests are implemented.

    The version of the OpenAPI document: 0.0.38
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.v0038_diag import V0038Diag
from openapi_client.models.v0038_diag_rpcm import V0038DiagRpcm
from openapi_client.models.v0038_diag_rpcu import V0038DiagRpcu
from openapi_client.models.v0038_diag_statistics import V0038DiagStatistics
from openapi_client.models.v0038_error import V0038Error
from openapi_client.models.v0038_errors import V0038Errors
from openapi_client.models.v0038_job_properties import V0038JobProperties
from openapi_client.models.v0038_job_resources import V0038JobResources
from openapi_client.models.v0038_job_response_properties import V0038JobResponseProperties
from openapi_client.models.v0038_jobs_response import V0038JobsResponse
from openapi_client.models.v0038_license import V0038License
from openapi_client.models.v0038_licenses import V0038Licenses
from openapi_client.models.v0038_meta import V0038Meta
from openapi_client.models.v0038_meta_plugin import V0038MetaPlugin
from openapi_client.models.v0038_meta_slurm import V0038MetaSlurm
from openapi_client.models.v0038_meta_slurm_version import V0038MetaSlurmVersion
from openapi_client.models.v0038_node import V0038Node
from openapi_client.models.v0038_node_allocation import V0038NodeAllocation
from openapi_client.models.v0038_node_allocation_sockets import V0038NodeAllocationSockets
from openapi_client.models.v0038_nodes_response import V0038NodesResponse
from openapi_client.models.v0038_partition import V0038Partition
from openapi_client.models.v0038_partitions_response import V0038PartitionsResponse
from openapi_client.models.v0038_ping import V0038Ping
from openapi_client.models.v0038_pings import V0038Pings
from openapi_client.models.v0038_reservation import V0038Reservation
from openapi_client.models.v0038_reservation_purge_completed import V0038ReservationPurgeCompleted
from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse
