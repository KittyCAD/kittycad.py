import datetime
from typing import Dict

from pydantic import BaseModel, ConfigDict

from ..models.cluster import Cluster
from ..models.gateway import Gateway
from ..models.jetstream import Jetstream
from ..models.leaf_node import LeafNode


class Connection(BaseModel):
    """Metadata about a pub-sub connection.

    This is mostly used for internal purposes and debugging."""

    auth_timeout: int = 0

    cluster: Cluster = {
        "addr": None,
        "auth_timeout": 0,
        "cluster_port": 0,
        "name": "",
        "tls_timeout": 0,
        "urls": [],
    }

    config_load_time: datetime.datetime

    connections: int = 0

    cores: int = 0

    cpu: float = 0.0

    gateway: Gateway = {
        "auth_timeout": 0,
        "host": "",
        "name": "",
        "port": 0,
        "tls_timeout": 0,
    }

    git_commit: str = ""

    go: str = ""

    gomaxprocs: int = 0

    host: str

    http_base_path: str = ""

    http_host: str = ""

    http_port: int = 0

    http_req_stats: Dict[str, int]

    https_port: int = 0

    in_bytes: int = 0

    in_msgs: int = 0

    jetstream: Jetstream = {
        "config": {"domain": "", "max_memory": 0, "max_storage": 0, "store_dir": ""},
        "meta": {"cluster_size": 0, "leader": "", "name": ""},
        "stats": {
            "accounts": 0,
            "api": {"errors": 0, "inflight": 0, "total": 0},
            "ha_assets": 0,
            "memory": 0,
            "reserved_memory": 0,
            "reserved_store": 0,
            "store": 0,
        },
    }

    leaf: LeafNode = {"auth_timeout": 0, "host": "", "port": 0, "tls_timeout": 0}

    leafnodes: int = 0

    max_connections: int = 0

    max_control_line: int = 0

    max_payload: int = 0

    max_pending: int = 0

    mem: int = 0

    now: datetime.datetime

    out_bytes: int = 0

    out_msgs: int = 0

    ping_interval: int = 0

    ping_max: int = 0

    port: int = 0

    proto: int = 0

    remotes: int = 0

    routes: int = 0

    server_id: str = ""

    server_name: str = ""

    slow_consumers: int = 0

    start: datetime.datetime

    subscriptions: int = 0

    system_account: str = ""

    tls_timeout: int = 0

    total_connections: int = 0

    uptime: str = ""

    version: str = ""

    write_deadline: int = 0

    model_config = ConfigDict(protected_namespaces=())
