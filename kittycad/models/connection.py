import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cluster import Cluster
from ..models.gateway import Gateway
from ..models.jetstream import Jetstream
from ..models.leaf_node import LeafNode
from ..types import UNSET, Unset

L = TypeVar("L", bound="Connection")


@attr.s(auto_attribs=True)
class Connection:
    """Metadata about a pub-sub connection.

    This is mostly used for internal purposes and debugging."""  # noqa: E501

    auth_timeout: Union[Unset, int] = UNSET
    cluster: Union[Unset, Cluster] = UNSET
    config_load_time: Union[Unset, datetime.datetime] = UNSET
    connections: Union[Unset, int] = UNSET
    cores: Union[Unset, int] = UNSET
    cpu: Union[Unset, float] = UNSET
    gateway: Union[Unset, Gateway] = UNSET
    git_commit: Union[Unset, str] = UNSET
    go: Union[Unset, str] = UNSET
    gomaxprocs: Union[Unset, int] = UNSET
    host: Union[Unset, str] = UNSET
    http_base_path: Union[Unset, str] = UNSET
    http_host: Union[Unset, str] = UNSET
    http_port: Union[Unset, int] = UNSET
    http_req_stats: Union[Unset, Any] = UNSET
    https_port: Union[Unset, int] = UNSET
    in_bytes: Union[Unset, int] = UNSET
    in_msgs: Union[Unset, int] = UNSET
    jetstream: Union[Unset, Jetstream] = UNSET
    leaf: Union[Unset, LeafNode] = UNSET
    leafnodes: Union[Unset, int] = UNSET
    max_connections: Union[Unset, int] = UNSET
    max_control_line: Union[Unset, int] = UNSET
    max_payload: Union[Unset, int] = UNSET
    max_pending: Union[Unset, int] = UNSET
    mem: Union[Unset, int] = UNSET
    now: Union[Unset, datetime.datetime] = UNSET
    out_bytes: Union[Unset, int] = UNSET
    out_msgs: Union[Unset, int] = UNSET
    ping_interval: Union[Unset, int] = UNSET
    ping_max: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    proto: Union[Unset, int] = UNSET
    remotes: Union[Unset, int] = UNSET
    routes: Union[Unset, int] = UNSET
    server_id: Union[Unset, str] = UNSET
    server_name: Union[Unset, str] = UNSET
    slow_consumers: Union[Unset, int] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    subscriptions: Union[Unset, int] = UNSET
    system_account: Union[Unset, str] = UNSET
    tls_timeout: Union[Unset, int] = UNSET
    total_connections: Union[Unset, int] = UNSET
    uptime: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    write_deadline: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_timeout = self.auth_timeout
        if not isinstance(self.cluster, Unset):
            cluster = self.cluster
        config_load_time: Union[Unset, str] = UNSET
        if not isinstance(self.config_load_time, Unset):
            config_load_time = self.config_load_time.isoformat()
        connections = self.connections
        cores = self.cores
        cpu = self.cpu
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway
        git_commit = self.git_commit
        go = self.go
        gomaxprocs = self.gomaxprocs
        host = self.host
        http_base_path = self.http_base_path
        http_host = self.http_host
        http_port = self.http_port
        http_req_stats = self.http_req_stats
        https_port = self.https_port
        in_bytes = self.in_bytes
        in_msgs = self.in_msgs
        if not isinstance(self.jetstream, Unset):
            jetstream = self.jetstream
        if not isinstance(self.leaf, Unset):
            leaf = self.leaf
        leafnodes = self.leafnodes
        max_connections = self.max_connections
        max_control_line = self.max_control_line
        max_payload = self.max_payload
        max_pending = self.max_pending
        mem = self.mem
        now: Union[Unset, str] = UNSET
        if not isinstance(self.now, Unset):
            now = self.now.isoformat()
        out_bytes = self.out_bytes
        out_msgs = self.out_msgs
        ping_interval = self.ping_interval
        ping_max = self.ping_max
        port = self.port
        proto = self.proto
        remotes = self.remotes
        routes = self.routes
        server_id = self.server_id
        server_name = self.server_name
        slow_consumers = self.slow_consumers
        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()
        subscriptions = self.subscriptions
        system_account = self.system_account
        tls_timeout = self.tls_timeout
        total_connections = self.total_connections
        uptime = self.uptime
        version = self.version
        write_deadline = self.write_deadline

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_timeout is not UNSET:
            field_dict["auth_timeout"] = auth_timeout
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if config_load_time is not UNSET:
            field_dict["config_load_time"] = config_load_time
        if connections is not UNSET:
            field_dict["connections"] = connections
        if cores is not UNSET:
            field_dict["cores"] = cores
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if git_commit is not UNSET:
            field_dict["git_commit"] = git_commit
        if go is not UNSET:
            field_dict["go"] = go
        if gomaxprocs is not UNSET:
            field_dict["gomaxprocs"] = gomaxprocs
        if host is not UNSET:
            field_dict["host"] = host
        if http_base_path is not UNSET:
            field_dict["http_base_path"] = http_base_path
        if http_host is not UNSET:
            field_dict["http_host"] = http_host
        if http_port is not UNSET:
            field_dict["http_port"] = http_port
        if http_req_stats is not UNSET:
            field_dict["http_req_stats"] = http_req_stats
        if https_port is not UNSET:
            field_dict["https_port"] = https_port
        if in_bytes is not UNSET:
            field_dict["in_bytes"] = in_bytes
        if in_msgs is not UNSET:
            field_dict["in_msgs"] = in_msgs
        if jetstream is not UNSET:
            field_dict["jetstream"] = jetstream
        if leaf is not UNSET:
            field_dict["leaf"] = leaf
        if leafnodes is not UNSET:
            field_dict["leafnodes"] = leafnodes
        if max_connections is not UNSET:
            field_dict["max_connections"] = max_connections
        if max_control_line is not UNSET:
            field_dict["max_control_line"] = max_control_line
        if max_payload is not UNSET:
            field_dict["max_payload"] = max_payload
        if max_pending is not UNSET:
            field_dict["max_pending"] = max_pending
        if mem is not UNSET:
            field_dict["mem"] = mem
        if now is not UNSET:
            field_dict["now"] = now
        if out_bytes is not UNSET:
            field_dict["out_bytes"] = out_bytes
        if out_msgs is not UNSET:
            field_dict["out_msgs"] = out_msgs
        if ping_interval is not UNSET:
            field_dict["ping_interval"] = ping_interval
        if ping_max is not UNSET:
            field_dict["ping_max"] = ping_max
        if port is not UNSET:
            field_dict["port"] = port
        if proto is not UNSET:
            field_dict["proto"] = proto
        if remotes is not UNSET:
            field_dict["remotes"] = remotes
        if routes is not UNSET:
            field_dict["routes"] = routes
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if slow_consumers is not UNSET:
            field_dict["slow_consumers"] = slow_consumers
        if start is not UNSET:
            field_dict["start"] = start
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if system_account is not UNSET:
            field_dict["system_account"] = system_account
        if tls_timeout is not UNSET:
            field_dict["tls_timeout"] = tls_timeout
        if total_connections is not UNSET:
            field_dict["total_connections"] = total_connections
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if version is not UNSET:
            field_dict["version"] = version
        if write_deadline is not UNSET:
            field_dict["write_deadline"] = write_deadline

        return field_dict

    @classmethod
    def from_dict(cls: Type[L], src_dict: Dict[str, Any]) -> L:
        d = src_dict.copy()
        auth_timeout = d.pop("auth_timeout", UNSET)

        _cluster = d.pop("cluster", UNSET)
        cluster: Union[Unset, Cluster]
        if isinstance(_cluster, Unset):
            cluster = UNSET
        else:
            cluster = Cluster(_cluster)

        _config_load_time = d.pop("config_load_time", UNSET)
        config_load_time: Union[Unset, datetime.datetime]
        if isinstance(_config_load_time, Unset):
            config_load_time = UNSET
        else:
            config_load_time = isoparse(_config_load_time)

        connections = d.pop("connections", UNSET)

        cores = d.pop("cores", UNSET)

        cpu = d.pop("cpu", UNSET)

        _gateway = d.pop("gateway", UNSET)
        gateway: Union[Unset, Gateway]
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = Gateway(_gateway)

        git_commit = d.pop("git_commit", UNSET)

        go = d.pop("go", UNSET)

        gomaxprocs = d.pop("gomaxprocs", UNSET)

        host = d.pop("host", UNSET)

        http_base_path = d.pop("http_base_path", UNSET)

        http_host = d.pop("http_host", UNSET)

        http_port = d.pop("http_port", UNSET)

        http_req_stats = d.pop("http_req_stats", UNSET)
        https_port = d.pop("https_port", UNSET)

        in_bytes = d.pop("in_bytes", UNSET)

        in_msgs = d.pop("in_msgs", UNSET)

        _jetstream = d.pop("jetstream", UNSET)
        jetstream: Union[Unset, Jetstream]
        if isinstance(_jetstream, Unset):
            jetstream = UNSET
        else:
            jetstream = Jetstream(_jetstream)

        _leaf = d.pop("leaf", UNSET)
        leaf: Union[Unset, LeafNode]
        if isinstance(_leaf, Unset):
            leaf = UNSET
        else:
            leaf = LeafNode(_leaf)

        leafnodes = d.pop("leafnodes", UNSET)

        max_connections = d.pop("max_connections", UNSET)

        max_control_line = d.pop("max_control_line", UNSET)

        max_payload = d.pop("max_payload", UNSET)

        max_pending = d.pop("max_pending", UNSET)

        mem = d.pop("mem", UNSET)

        _now = d.pop("now", UNSET)
        now: Union[Unset, datetime.datetime]
        if isinstance(_now, Unset):
            now = UNSET
        else:
            now = isoparse(_now)

        out_bytes = d.pop("out_bytes", UNSET)

        out_msgs = d.pop("out_msgs", UNSET)

        ping_interval = d.pop("ping_interval", UNSET)

        ping_max = d.pop("ping_max", UNSET)

        port = d.pop("port", UNSET)

        proto = d.pop("proto", UNSET)

        remotes = d.pop("remotes", UNSET)

        routes = d.pop("routes", UNSET)

        server_id = d.pop("server_id", UNSET)

        server_name = d.pop("server_name", UNSET)

        slow_consumers = d.pop("slow_consumers", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        subscriptions = d.pop("subscriptions", UNSET)

        system_account = d.pop("system_account", UNSET)

        tls_timeout = d.pop("tls_timeout", UNSET)

        total_connections = d.pop("total_connections", UNSET)

        uptime = d.pop("uptime", UNSET)

        version = d.pop("version", UNSET)

        write_deadline = d.pop("write_deadline", UNSET)

        connection = cls(
            auth_timeout=auth_timeout,
            cluster=cluster,
            config_load_time=config_load_time,
            connections=connections,
            cores=cores,
            cpu=cpu,
            gateway=gateway,
            git_commit=git_commit,
            go=go,
            gomaxprocs=gomaxprocs,
            host=host,
            http_base_path=http_base_path,
            http_host=http_host,
            http_port=http_port,
            http_req_stats=http_req_stats,
            https_port=https_port,
            in_bytes=in_bytes,
            in_msgs=in_msgs,
            jetstream=jetstream,
            leaf=leaf,
            leafnodes=leafnodes,
            max_connections=max_connections,
            max_control_line=max_control_line,
            max_payload=max_payload,
            max_pending=max_pending,
            mem=mem,
            now=now,
            out_bytes=out_bytes,
            out_msgs=out_msgs,
            ping_interval=ping_interval,
            ping_max=ping_max,
            port=port,
            proto=proto,
            remotes=remotes,
            routes=routes,
            server_id=server_id,
            server_name=server_name,
            slow_consumers=slow_consumers,
            start=start,
            subscriptions=subscriptions,
            system_account=system_account,
            tls_timeout=tls_timeout,
            total_connections=total_connections,
            uptime=uptime,
            version=version,
            write_deadline=write_deadline,
        )

        connection.additional_properties = d
        return connection

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
