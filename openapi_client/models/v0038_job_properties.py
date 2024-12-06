# coding: utf-8

"""
    Slurm Rest API RO

    API to access Slurm. Only GET requests are implemented.

    The version of the OpenAPI document: 0.0.38
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class V0038JobProperties(BaseModel):
    """
    V0038JobProperties
    """ # noqa: E501
    account: Optional[StrictStr] = Field(default=None, description="Charge resources used by this job to specified account.")
    account_gather_frequency: Optional[StrictStr] = Field(default=None, description="Define the job accounting and profiling sampling intervals.")
    argv: Optional[List[StrictStr]] = Field(default=None, description="Arguments to the script.")
    array: Optional[StrictStr] = Field(default=None, description="Submit a job array, multiple jobs to be executed with identical parameters. The indexes specification identifies what array index values should be used.")
    batch_features: Optional[StrictStr] = Field(default=None, description="features required for batch script's node")
    begin_time: Optional[StrictInt] = Field(default=None, description="Submit the batch script to the Slurm controller immediately, like normal, but tell the controller to defer the allocation of the job until the specified time.")
    burst_buffer: Optional[StrictStr] = Field(default=None, description="Burst buffer specification.")
    cluster_constraint: Optional[StrictStr] = Field(default=None, description="Specifies features that a federated cluster must have to have a sibling job submitted to it.")
    comment: Optional[StrictStr] = Field(default=None, description="An arbitrary comment.")
    constraints: Optional[StrictStr] = Field(default=None, description="node features required by job.")
    container: Optional[StrictStr] = Field(default=None, description="absolute path to OCI container bundle")
    core_specification: Optional[StrictInt] = Field(default=None, description="Count of specialized threads per node reserved by the job for system operations and not used by the application.")
    cores_per_socket: Optional[StrictInt] = Field(default=None, description="Restrict node selection to nodes with at least the specified number of cores per socket.")
    cpu_binding: Optional[StrictStr] = Field(default=None, description="Cpu binding")
    cpu_binding_hint: Optional[StrictStr] = Field(default=None, description="Cpu binding hint")
    cpu_frequency: Optional[StrictStr] = Field(default=None, description="Request that job steps initiated by srun commands inside this sbatch script be run at some requested frequency if possible, on the CPUs selected for the step on the compute node(s).")
    cpus_per_gpu: Optional[StrictStr] = Field(default=None, description="Number of CPUs requested per allocated GPU.")
    cpus_per_task: Optional[StrictInt] = Field(default=None, description="Advise the Slurm controller that ensuing job steps will require ncpus number of processors per task.")
    current_working_directory: Optional[StrictStr] = Field(default=None, description="Instruct Slurm to connect the batch script's standard output directly to the file name.")
    deadline: Optional[StrictStr] = Field(default=None, description="Remove the job if no ending is possible before this deadline (start > (deadline - time[-min])).")
    delay_boot: Optional[StrictInt] = Field(default=None, description="Do not reboot nodes in order to satisfied this job's feature specification if the job has been eligible to run for less than this time period.")
    dependency: Optional[StrictStr] = Field(default=None, description="Defer the start of this job until the specified dependencies have been satisfied completed.")
    distribution: Optional[StrictStr] = Field(default=None, description="Specify alternate distribution methods for remote processes.")
    environment: Dict[str, Any] = Field(description="Dictionary of environment entries.")
    exclusive: Optional[StrictStr] = Field(default=None, description="The job allocation can share nodes just other users with the \"user\" option or with the \"mcs\" option).")
    get_user_environment: Optional[StrictBool] = Field(default=None, description="Load new login environment for user on job node.")
    gres: Optional[StrictStr] = Field(default=None, description="Specifies a comma delimited list of generic consumable resources.")
    gres_flags: Optional[StrictStr] = Field(default=None, description="Specify generic resource task binding options.")
    gpu_binding: Optional[StrictStr] = Field(default=None, description="Requested binding of tasks to GPU.")
    gpu_frequency: Optional[StrictStr] = Field(default=None, description="Requested GPU frequency.")
    gpus: Optional[StrictStr] = Field(default=None, description="GPUs per job.")
    gpus_per_node: Optional[StrictStr] = Field(default=None, description="GPUs per node.")
    gpus_per_socket: Optional[StrictStr] = Field(default=None, description="GPUs per socket.")
    gpus_per_task: Optional[StrictStr] = Field(default=None, description="GPUs per task.")
    hold: Optional[StrictBool] = Field(default=None, description="Specify the job is to be submitted in a held state (priority of zero).")
    kill_on_invalid_dependency: Optional[StrictBool] = Field(default=None, description="If a job has an invalid dependency, then Slurm is to terminate it.")
    licenses: Optional[StrictStr] = Field(default=None, description="Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job.")
    mail_type: Optional[StrictStr] = Field(default=None, description="Notify user by email when certain event types occur.")
    mail_user: Optional[StrictStr] = Field(default=None, description="User to receive email notification of state changes as defined by mail_type.")
    mcs_label: Optional[StrictStr] = Field(default=None, description="This parameter is a group among the groups of the user.")
    memory_binding: Optional[StrictStr] = Field(default=None, description="Bind tasks to memory.")
    memory_per_cpu: Optional[StrictInt] = Field(default=None, description="Minimum real memory per cpu (MB).")
    memory_per_gpu: Optional[StrictInt] = Field(default=None, description="Minimum memory required per allocated GPU.")
    memory_per_node: Optional[StrictInt] = Field(default=None, description="Minimum real memory per node (MB).")
    minimum_cpus_per_node: Optional[StrictInt] = Field(default=None, description="Minimum number of CPUs per node.")
    minimum_nodes: Optional[StrictBool] = Field(default=None, description="If a range of node counts is given, prefer the smaller count.")
    name: Optional[StrictStr] = Field(default=None, description="Specify a name for the job allocation.")
    nice: Optional[StrictInt] = Field(default=None, description="Run the job with an adjusted scheduling priority within Slurm.")
    no_kill: Optional[StrictBool] = Field(default=None, description="Do not automatically terminate a job if one of the nodes it has been allocated fails.")
    nodes: Optional[Annotated[List[StrictInt], Field(min_length=1, max_length=2)]] = Field(default=None, description="Request that a minimum of minnodes nodes and a maximum node count.")
    open_mode: Optional[StrictStr] = Field(default='append', description="Open the output and error files using append or truncate mode as specified.")
    oversubscribe: Optional[StrictBool] = Field(default=False, description="The job allocation can over-subscribe resources with other running jobs.")
    partition: Optional[StrictStr] = Field(default=None, description="Request a specific partition for the resource allocation.")
    prefer: Optional[StrictStr] = Field(default=None, description="Comma delimited list of features for scheduler to prefer but not a strict requirement like a constraint. Value can be used for job submission but is only displayed for PENDING jobs.")
    priority: Optional[StrictStr] = Field(default=None, description="Request a specific job priority.")
    qos: Optional[StrictStr] = Field(default=None, description="Request a quality of service for the job.")
    requeue: Optional[StrictBool] = Field(default=None, description="Specifies that the batch job should eligible to being requeue.")
    reservation: Optional[StrictStr] = Field(default=None, description="Allocate resources for the job from the named reservation.")
    signal: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="When a job is within sig_time seconds of its end time, send it the signal sig_num.")
    sockets_per_node: Optional[StrictInt] = Field(default=None, description="Restrict node selection to nodes with at least the specified number of sockets.")
    spread_job: Optional[StrictBool] = Field(default=None, description="Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes.")
    standard_error: Optional[StrictStr] = Field(default=None, description="Instruct Slurm to connect the batch script's standard error directly to the file name.")
    standard_input: Optional[StrictStr] = Field(default=None, description="Instruct Slurm to connect the batch script's standard input directly to the file name specified.")
    standard_output: Optional[StrictStr] = Field(default=None, description="Instruct Slurm to connect the batch script's standard output directly to the file name.")
    tasks: Optional[StrictInt] = Field(default=None, description="Advises the Slurm controller that job steps run within the allocation will launch a maximum of number tasks and to provide for sufficient resources.")
    tasks_per_core: Optional[StrictInt] = Field(default=None, description="Request the maximum ntasks be invoked on each core.")
    tasks_per_node: Optional[StrictInt] = Field(default=None, description="Request the maximum ntasks be invoked on each node.")
    tasks_per_socket: Optional[StrictInt] = Field(default=None, description="Request the maximum ntasks be invoked on each socket.")
    thread_specification: Optional[StrictInt] = Field(default=None, description="Count of specialized threads per node reserved by the job for system operations and not used by the application.")
    threads_per_core: Optional[StrictInt] = Field(default=None, description="Restrict node selection to nodes with at least the specified number of threads per core.")
    time_limit: Optional[StrictInt] = Field(default=None, description="Step time limit in minutes.")
    time_minimum: Optional[StrictInt] = Field(default=None, description="Minimum run time in minutes.")
    wait_all_nodes: Optional[StrictBool] = Field(default=None, description="Do not begin execution until all nodes are ready for use.")
    wckey: Optional[StrictStr] = Field(default=None, description="Specify wckey to be used with job.")
    __properties: ClassVar[List[str]] = ["account", "account_gather_frequency", "argv", "array", "batch_features", "begin_time", "burst_buffer", "cluster_constraint", "comment", "constraints", "container", "core_specification", "cores_per_socket", "cpu_binding", "cpu_binding_hint", "cpu_frequency", "cpus_per_gpu", "cpus_per_task", "current_working_directory", "deadline", "delay_boot", "dependency", "distribution", "environment", "exclusive", "get_user_environment", "gres", "gres_flags", "gpu_binding", "gpu_frequency", "gpus", "gpus_per_node", "gpus_per_socket", "gpus_per_task", "hold", "kill_on_invalid_dependency", "licenses", "mail_type", "mail_user", "mcs_label", "memory_binding", "memory_per_cpu", "memory_per_gpu", "memory_per_node", "minimum_cpus_per_node", "minimum_nodes", "name", "nice", "no_kill", "nodes", "open_mode", "oversubscribe", "partition", "prefer", "priority", "qos", "requeue", "reservation", "signal", "sockets_per_node", "spread_job", "standard_error", "standard_input", "standard_output", "tasks", "tasks_per_core", "tasks_per_node", "tasks_per_socket", "thread_specification", "threads_per_core", "time_limit", "time_minimum", "wait_all_nodes", "wckey"]

    @field_validator('exclusive')
    def exclusive_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['user', 'mcs', 'true', 'false']):
            raise ValueError("must be one of enum values ('user', 'mcs', 'true', 'false')")
        return value

    @field_validator('gres_flags')
    def gres_flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['disable-binding', 'enforce-binding']):
            raise ValueError("must be one of enum values ('disable-binding', 'enforce-binding')")
        return value

    @field_validator('open_mode')
    def open_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['append', 'truncate']):
            raise ValueError("must be one of enum values ('append', 'truncate')")
        return value

    @field_validator('signal')
    def signal_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"(B:|)sig_num(@sig_time|)", value):
            raise ValueError(r"must validate the regular expression /(B:|)sig_num(@sig_time|)/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V0038JobProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0038JobProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "account_gather_frequency": obj.get("account_gather_frequency"),
            "argv": obj.get("argv"),
            "array": obj.get("array"),
            "batch_features": obj.get("batch_features"),
            "begin_time": obj.get("begin_time"),
            "burst_buffer": obj.get("burst_buffer"),
            "cluster_constraint": obj.get("cluster_constraint"),
            "comment": obj.get("comment"),
            "constraints": obj.get("constraints"),
            "container": obj.get("container"),
            "core_specification": obj.get("core_specification"),
            "cores_per_socket": obj.get("cores_per_socket"),
            "cpu_binding": obj.get("cpu_binding"),
            "cpu_binding_hint": obj.get("cpu_binding_hint"),
            "cpu_frequency": obj.get("cpu_frequency"),
            "cpus_per_gpu": obj.get("cpus_per_gpu"),
            "cpus_per_task": obj.get("cpus_per_task"),
            "current_working_directory": obj.get("current_working_directory"),
            "deadline": obj.get("deadline"),
            "delay_boot": obj.get("delay_boot"),
            "dependency": obj.get("dependency"),
            "distribution": obj.get("distribution"),
            "environment": obj.get("environment"),
            "exclusive": obj.get("exclusive"),
            "get_user_environment": obj.get("get_user_environment"),
            "gres": obj.get("gres"),
            "gres_flags": obj.get("gres_flags"),
            "gpu_binding": obj.get("gpu_binding"),
            "gpu_frequency": obj.get("gpu_frequency"),
            "gpus": obj.get("gpus"),
            "gpus_per_node": obj.get("gpus_per_node"),
            "gpus_per_socket": obj.get("gpus_per_socket"),
            "gpus_per_task": obj.get("gpus_per_task"),
            "hold": obj.get("hold"),
            "kill_on_invalid_dependency": obj.get("kill_on_invalid_dependency"),
            "licenses": obj.get("licenses"),
            "mail_type": obj.get("mail_type"),
            "mail_user": obj.get("mail_user"),
            "mcs_label": obj.get("mcs_label"),
            "memory_binding": obj.get("memory_binding"),
            "memory_per_cpu": obj.get("memory_per_cpu"),
            "memory_per_gpu": obj.get("memory_per_gpu"),
            "memory_per_node": obj.get("memory_per_node"),
            "minimum_cpus_per_node": obj.get("minimum_cpus_per_node"),
            "minimum_nodes": obj.get("minimum_nodes"),
            "name": obj.get("name"),
            "nice": obj.get("nice"),
            "no_kill": obj.get("no_kill"),
            "nodes": obj.get("nodes"),
            "open_mode": obj.get("open_mode") if obj.get("open_mode") is not None else 'append',
            "oversubscribe": obj.get("oversubscribe") if obj.get("oversubscribe") is not None else False,
            "partition": obj.get("partition"),
            "prefer": obj.get("prefer"),
            "priority": obj.get("priority"),
            "qos": obj.get("qos"),
            "requeue": obj.get("requeue"),
            "reservation": obj.get("reservation"),
            "signal": obj.get("signal"),
            "sockets_per_node": obj.get("sockets_per_node"),
            "spread_job": obj.get("spread_job"),
            "standard_error": obj.get("standard_error"),
            "standard_input": obj.get("standard_input"),
            "standard_output": obj.get("standard_output"),
            "tasks": obj.get("tasks"),
            "tasks_per_core": obj.get("tasks_per_core"),
            "tasks_per_node": obj.get("tasks_per_node"),
            "tasks_per_socket": obj.get("tasks_per_socket"),
            "thread_specification": obj.get("thread_specification"),
            "threads_per_core": obj.get("threads_per_core"),
            "time_limit": obj.get("time_limit"),
            "time_minimum": obj.get("time_minimum"),
            "wait_all_nodes": obj.get("wait_all_nodes"),
            "wckey": obj.get("wckey")
        })
        return _obj


