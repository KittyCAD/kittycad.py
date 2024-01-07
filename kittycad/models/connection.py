import datetime
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.cluster import Cluster
from ..models.gateway import Gateway
from ..models.jetstream import Jetstream
from ..models.leaf_node import LeafNode


class Connection(BaseModel):
    """Metadata about a pub-sub connection.

    This is mostly used for internal purposes and debugging."""

    auth_timeout: Optional[int] = None

    cluster: Optional[Cluster] = None

    config_load_time: datetime.datetime

    connections: Optional[int] = None

    cores: Optional[int] = None

    cpu: Optional[float] = None

    gateway: Optional[Gateway] = None

    git_commit: Optional[str] = None

    go: Optional[str] = None

    gomaxprocs: Optional[int] = None

    host: str

    http_base_path: Optional[str] = None

    http_host: Optional[str] = None

    http_port: Optional[int] = None

    http_req_stats: Dict[str, int]

    https_port: Optional[int] = None

    in_bytes: Optional[int] = None

    in_msgs: Optional[int] = None

    jetstream: Optional[Jetstream] = None

    leaf: Optional[LeafNode] = None

    leafnodes: Optional[int] = None

    max_connections: Optional[int] = None

    max_control_line: Optional[int] = None

    max_payload: Optional[int] = None

    max_pending: Optional[int] = None

    mem: Optional[int] = None

    now: datetime.datetime

    out_bytes: Optional[int] = None

    out_msgs: Optional[int] = None

    ping_interval: Optional[int] = None

    ping_max: Optional[int] = None

    port: Optional[int] = None

    proto: Optional[int] = None

    remotes: Optional[int] = None

    routes: Optional[int] = None

    server_id: Optional[str] = None

    server_name: Optional[str] = None

    slow_consumers: Optional[int] = None

    start: datetime.datetime

    subscriptions: Optional[int] = None

    system_account: Optional[str] = None

    tls_timeout: Optional[int] = None

    total_connections: Optional[int] = None

    uptime: Optional[str] = None

    version: Optional[str] = None

    write_deadline: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
