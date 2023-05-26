from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.commit import Commit
from ..models.plugins_info import PluginsInfo
from ..models.registry_service_config import RegistryServiceConfig
from ..models.system_info_cgroup_driver_enum import SystemInfoCgroupDriverEnum
from ..models.system_info_cgroup_version_enum import SystemInfoCgroupVersionEnum
from ..models.system_info_isolation_enum import SystemInfoIsolationEnum
from ..types import UNSET, Unset

V = TypeVar("V", bound="DockerSystemInfo")


@attr.s(auto_attribs=True)
class DockerSystemInfo:
    """Docker system info."""  # noqa: E501

    architecture: Union[Unset, str] = UNSET
    bridge_nf_ip6tables: Union[Unset, bool] = False
    bridge_nf_iptables: Union[Unset, bool] = False
    cgroup_driver: Union[Unset, SystemInfoCgroupDriverEnum] = UNSET
    cgroup_version: Union[Unset, SystemInfoCgroupVersionEnum] = UNSET
    cluster_advertise: Union[Unset, str] = UNSET
    cluster_store: Union[Unset, str] = UNSET
    containerd_commit: Union[Unset, Commit] = UNSET
    containers: Union[Unset, int] = UNSET
    containers_paused: Union[Unset, int] = UNSET
    containers_running: Union[Unset, int] = UNSET
    containers_stopped: Union[Unset, int] = UNSET
    cpu_cfs_period: Union[Unset, bool] = False
    cpu_cfs_quota: Union[Unset, bool] = False
    cpu_set: Union[Unset, bool] = False
    cpu_shares: Union[Unset, bool] = False
    debug: Union[Unset, bool] = False
    from ..models.system_info_default_address_pools import SystemInfoDefaultAddressPools

    default_address_pools: Union[Unset, List[SystemInfoDefaultAddressPools]] = UNSET
    default_runtime: Union[Unset, str] = UNSET
    docker_root_dir: Union[Unset, str] = UNSET
    driver: Union[Unset, str] = UNSET
    driver_status: Union[Unset, List[List[str]]] = UNSET
    experimental_build: Union[Unset, bool] = False
    http_proxy: Union[Unset, str] = UNSET
    https_proxy: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    images: Union[Unset, int] = UNSET
    index_server_address: Union[Unset, str] = UNSET
    init_binary: Union[Unset, str] = UNSET
    init_commit: Union[Unset, Commit] = UNSET
    ipv4_forwarding: Union[Unset, bool] = False
    isolation: Union[Unset, SystemInfoIsolationEnum] = UNSET
    kernel_memory: Union[Unset, bool] = False
    kernel_memory_tcp: Union[Unset, bool] = False
    kernel_version: Union[Unset, str] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    live_restore_enabled: Union[Unset, bool] = False
    logging_driver: Union[Unset, str] = UNSET
    mem_total: Union[Unset, int] = UNSET
    memory_limit: Union[Unset, bool] = False
    n_events_listener: Union[Unset, int] = UNSET
    n_fd: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    ncpu: Union[Unset, int] = UNSET
    no_proxy: Union[Unset, str] = UNSET
    oom_kill_disable: Union[Unset, bool] = False
    operating_system: Union[Unset, str] = UNSET
    os_type: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    pids_limit: Union[Unset, bool] = False
    plugins: Union[Unset, PluginsInfo] = UNSET
    product_license: Union[Unset, str] = UNSET
    registry_config: Union[Unset, RegistryServiceConfig] = UNSET
    runc_commit: Union[Unset, Commit] = UNSET
    runtimes: Union[Unset, Any] = UNSET
    security_options: Union[Unset, List[str]] = UNSET
    server_version: Union[Unset, str] = UNSET
    swap_limit: Union[Unset, bool] = False
    system_time: Union[Unset, str] = UNSET
    warnings: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        architecture = self.architecture
        bridge_nf_ip6tables = self.bridge_nf_ip6tables
        bridge_nf_iptables = self.bridge_nf_iptables
        if not isinstance(self.cgroup_driver, Unset):
            cgroup_driver = self.cgroup_driver
        if not isinstance(self.cgroup_version, Unset):
            cgroup_version = self.cgroup_version
        cluster_advertise = self.cluster_advertise
        cluster_store = self.cluster_store
        if not isinstance(self.containerd_commit, Unset):
            containerd_commit = self.containerd_commit
        containers = self.containers
        containers_paused = self.containers_paused
        containers_running = self.containers_running
        containers_stopped = self.containers_stopped
        cpu_cfs_period = self.cpu_cfs_period
        cpu_cfs_quota = self.cpu_cfs_quota
        cpu_set = self.cpu_set
        cpu_shares = self.cpu_shares
        debug = self.debug
        from ..models.system_info_default_address_pools import (
            SystemInfoDefaultAddressPools,
        )

        default_address_pools: Union[Unset, List[SystemInfoDefaultAddressPools]] = UNSET
        if not isinstance(self.default_address_pools, Unset):
            default_address_pools = self.default_address_pools
        default_runtime = self.default_runtime
        docker_root_dir = self.docker_root_dir
        driver = self.driver
        driver_status: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.driver_status, Unset):
            driver_status = self.driver_status
        experimental_build = self.experimental_build
        http_proxy = self.http_proxy
        https_proxy = self.https_proxy
        id = self.id
        images = self.images
        index_server_address = self.index_server_address
        init_binary = self.init_binary
        if not isinstance(self.init_commit, Unset):
            init_commit = self.init_commit
        ipv4_forwarding = self.ipv4_forwarding
        if not isinstance(self.isolation, Unset):
            isolation = self.isolation
        kernel_memory = self.kernel_memory
        kernel_memory_tcp = self.kernel_memory_tcp
        kernel_version = self.kernel_version
        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels
        live_restore_enabled = self.live_restore_enabled
        logging_driver = self.logging_driver
        mem_total = self.mem_total
        memory_limit = self.memory_limit
        n_events_listener = self.n_events_listener
        n_fd = self.n_fd
        name = self.name
        ncpu = self.ncpu
        no_proxy = self.no_proxy
        oom_kill_disable = self.oom_kill_disable
        operating_system = self.operating_system
        os_type = self.os_type
        os_version = self.os_version
        pids_limit = self.pids_limit
        if not isinstance(self.plugins, Unset):
            plugins = self.plugins
        product_license = self.product_license
        if not isinstance(self.registry_config, Unset):
            registry_config = self.registry_config
        if not isinstance(self.runc_commit, Unset):
            runc_commit = self.runc_commit
        runtimes = self.runtimes
        security_options: Union[Unset, List[str]] = UNSET
        if not isinstance(self.security_options, Unset):
            security_options = self.security_options
        server_version = self.server_version
        swap_limit = self.swap_limit
        system_time = self.system_time
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if bridge_nf_ip6tables is not UNSET:
            field_dict["bridge_nf_ip6tables"] = bridge_nf_ip6tables
        if bridge_nf_iptables is not UNSET:
            field_dict["bridge_nf_iptables"] = bridge_nf_iptables
        if cgroup_driver is not UNSET:
            field_dict["cgroup_driver"] = cgroup_driver
        if cgroup_version is not UNSET:
            field_dict["cgroup_version"] = cgroup_version
        if cluster_advertise is not UNSET:
            field_dict["cluster_advertise"] = cluster_advertise
        if cluster_store is not UNSET:
            field_dict["cluster_store"] = cluster_store
        if containerd_commit is not UNSET:
            field_dict["containerd_commit"] = containerd_commit
        if containers is not UNSET:
            field_dict["containers"] = containers
        if containers_paused is not UNSET:
            field_dict["containers_paused"] = containers_paused
        if containers_running is not UNSET:
            field_dict["containers_running"] = containers_running
        if containers_stopped is not UNSET:
            field_dict["containers_stopped"] = containers_stopped
        if cpu_cfs_period is not UNSET:
            field_dict["cpu_cfs_period"] = cpu_cfs_period
        if cpu_cfs_quota is not UNSET:
            field_dict["cpu_cfs_quota"] = cpu_cfs_quota
        if cpu_set is not UNSET:
            field_dict["cpu_set"] = cpu_set
        if cpu_shares is not UNSET:
            field_dict["cpu_shares"] = cpu_shares
        if debug is not UNSET:
            field_dict["debug"] = debug
        if default_address_pools is not UNSET:
            field_dict["default_address_pools"] = default_address_pools
        if default_runtime is not UNSET:
            field_dict["default_runtime"] = default_runtime
        if docker_root_dir is not UNSET:
            field_dict["docker_root_dir"] = docker_root_dir
        if driver is not UNSET:
            field_dict["driver"] = driver
        if driver_status is not UNSET:
            field_dict["driver_status"] = driver_status
        if experimental_build is not UNSET:
            field_dict["experimental_build"] = experimental_build
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy
        if https_proxy is not UNSET:
            field_dict["https_proxy"] = https_proxy
        if id is not UNSET:
            field_dict["id"] = id
        if images is not UNSET:
            field_dict["images"] = images
        if index_server_address is not UNSET:
            field_dict["index_server_address"] = index_server_address
        if init_binary is not UNSET:
            field_dict["init_binary"] = init_binary
        if init_commit is not UNSET:
            field_dict["init_commit"] = init_commit
        if ipv4_forwarding is not UNSET:
            field_dict["ipv4_forwarding"] = ipv4_forwarding
        if isolation is not UNSET:
            field_dict["isolation"] = isolation
        if kernel_memory is not UNSET:
            field_dict["kernel_memory"] = kernel_memory
        if kernel_memory_tcp is not UNSET:
            field_dict["kernel_memory_tcp"] = kernel_memory_tcp
        if kernel_version is not UNSET:
            field_dict["kernel_version"] = kernel_version
        if labels is not UNSET:
            field_dict["labels"] = labels
        if live_restore_enabled is not UNSET:
            field_dict["live_restore_enabled"] = live_restore_enabled
        if logging_driver is not UNSET:
            field_dict["logging_driver"] = logging_driver
        if mem_total is not UNSET:
            field_dict["mem_total"] = mem_total
        if memory_limit is not UNSET:
            field_dict["memory_limit"] = memory_limit
        if n_events_listener is not UNSET:
            field_dict["n_events_listener"] = n_events_listener
        if n_fd is not UNSET:
            field_dict["n_fd"] = n_fd
        if name is not UNSET:
            field_dict["name"] = name
        if ncpu is not UNSET:
            field_dict["ncpu"] = ncpu
        if no_proxy is not UNSET:
            field_dict["no_proxy"] = no_proxy
        if oom_kill_disable is not UNSET:
            field_dict["oom_kill_disable"] = oom_kill_disable
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if os_type is not UNSET:
            field_dict["os_type"] = os_type
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if pids_limit is not UNSET:
            field_dict["pids_limit"] = pids_limit
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if product_license is not UNSET:
            field_dict["product_license"] = product_license
        if registry_config is not UNSET:
            field_dict["registry_config"] = registry_config
        if runc_commit is not UNSET:
            field_dict["runc_commit"] = runc_commit
        if runtimes is not UNSET:
            field_dict["runtimes"] = runtimes
        if security_options is not UNSET:
            field_dict["security_options"] = security_options
        if server_version is not UNSET:
            field_dict["server_version"] = server_version
        if swap_limit is not UNSET:
            field_dict["swap_limit"] = swap_limit
        if system_time is not UNSET:
            field_dict["system_time"] = system_time
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[V], src_dict: Dict[str, Any]) -> V:
        d = src_dict.copy()
        architecture = d.pop("architecture", UNSET)

        bridge_nf_ip6tables = d.pop("bridge_nf_ip6tables", UNSET)

        bridge_nf_iptables = d.pop("bridge_nf_iptables", UNSET)

        _cgroup_driver = d.pop("cgroup_driver", UNSET)
        cgroup_driver: Union[Unset, SystemInfoCgroupDriverEnum]
        if isinstance(_cgroup_driver, Unset):
            cgroup_driver = UNSET
        else:
            cgroup_driver = SystemInfoCgroupDriverEnum(_cgroup_driver)

        _cgroup_version = d.pop("cgroup_version", UNSET)
        cgroup_version: Union[Unset, SystemInfoCgroupVersionEnum]
        if isinstance(_cgroup_version, Unset):
            cgroup_version = UNSET
        else:
            cgroup_version = SystemInfoCgroupVersionEnum(_cgroup_version)

        cluster_advertise = d.pop("cluster_advertise", UNSET)

        cluster_store = d.pop("cluster_store", UNSET)

        _containerd_commit = d.pop("containerd_commit", UNSET)
        containerd_commit: Union[Unset, Commit]
        if isinstance(_containerd_commit, Unset):
            containerd_commit = UNSET
        else:
            containerd_commit = Commit(_containerd_commit)

        containers = d.pop("containers", UNSET)

        containers_paused = d.pop("containers_paused", UNSET)

        containers_running = d.pop("containers_running", UNSET)

        containers_stopped = d.pop("containers_stopped", UNSET)

        cpu_cfs_period = d.pop("cpu_cfs_period", UNSET)

        cpu_cfs_quota = d.pop("cpu_cfs_quota", UNSET)

        cpu_set = d.pop("cpu_set", UNSET)

        cpu_shares = d.pop("cpu_shares", UNSET)

        debug = d.pop("debug", UNSET)

        from ..models.system_info_default_address_pools import (
            SystemInfoDefaultAddressPools,
        )

        default_address_pools = cast(
            List[SystemInfoDefaultAddressPools], d.pop("default_address_pools", UNSET)
        )

        default_runtime = d.pop("default_runtime", UNSET)

        docker_root_dir = d.pop("docker_root_dir", UNSET)

        driver = d.pop("driver", UNSET)

        driver_status = cast(List[List[str]], d.pop("driver_status", UNSET))

        experimental_build = d.pop("experimental_build", UNSET)

        http_proxy = d.pop("http_proxy", UNSET)

        https_proxy = d.pop("https_proxy", UNSET)

        id = d.pop("id", UNSET)

        images = d.pop("images", UNSET)

        index_server_address = d.pop("index_server_address", UNSET)

        init_binary = d.pop("init_binary", UNSET)

        _init_commit = d.pop("init_commit", UNSET)
        init_commit: Union[Unset, Commit]
        if isinstance(_init_commit, Unset):
            init_commit = UNSET
        else:
            init_commit = Commit(_init_commit)

        ipv4_forwarding = d.pop("ipv4_forwarding", UNSET)

        _isolation = d.pop("isolation", UNSET)
        isolation: Union[Unset, SystemInfoIsolationEnum]
        if isinstance(_isolation, Unset):
            isolation = UNSET
        else:
            isolation = SystemInfoIsolationEnum(_isolation)

        kernel_memory = d.pop("kernel_memory", UNSET)

        kernel_memory_tcp = d.pop("kernel_memory_tcp", UNSET)

        kernel_version = d.pop("kernel_version", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        live_restore_enabled = d.pop("live_restore_enabled", UNSET)

        logging_driver = d.pop("logging_driver", UNSET)

        mem_total = d.pop("mem_total", UNSET)

        memory_limit = d.pop("memory_limit", UNSET)

        n_events_listener = d.pop("n_events_listener", UNSET)

        n_fd = d.pop("n_fd", UNSET)

        name = d.pop("name", UNSET)

        ncpu = d.pop("ncpu", UNSET)

        no_proxy = d.pop("no_proxy", UNSET)

        oom_kill_disable = d.pop("oom_kill_disable", UNSET)

        operating_system = d.pop("operating_system", UNSET)

        os_type = d.pop("os_type", UNSET)

        os_version = d.pop("os_version", UNSET)

        pids_limit = d.pop("pids_limit", UNSET)

        _plugins = d.pop("plugins", UNSET)
        plugins: Union[Unset, PluginsInfo]
        if isinstance(_plugins, Unset):
            plugins = UNSET
        else:
            plugins = PluginsInfo(_plugins)

        product_license = d.pop("product_license", UNSET)

        _registry_config = d.pop("registry_config", UNSET)
        registry_config: Union[Unset, RegistryServiceConfig]
        if isinstance(_registry_config, Unset):
            registry_config = UNSET
        else:
            registry_config = RegistryServiceConfig(_registry_config)

        _runc_commit = d.pop("runc_commit", UNSET)
        runc_commit: Union[Unset, Commit]
        if isinstance(_runc_commit, Unset):
            runc_commit = UNSET
        else:
            runc_commit = Commit(_runc_commit)

        runtimes = d.pop("runtimes", UNSET)
        security_options = cast(List[str], d.pop("security_options", UNSET))

        server_version = d.pop("server_version", UNSET)

        swap_limit = d.pop("swap_limit", UNSET)

        system_time = d.pop("system_time", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        docker_system_info = cls(
            architecture=architecture,
            bridge_nf_ip6tables=bridge_nf_ip6tables,
            bridge_nf_iptables=bridge_nf_iptables,
            cgroup_driver=cgroup_driver,
            cgroup_version=cgroup_version,
            cluster_advertise=cluster_advertise,
            cluster_store=cluster_store,
            containerd_commit=containerd_commit,
            containers=containers,
            containers_paused=containers_paused,
            containers_running=containers_running,
            containers_stopped=containers_stopped,
            cpu_cfs_period=cpu_cfs_period,
            cpu_cfs_quota=cpu_cfs_quota,
            cpu_set=cpu_set,
            cpu_shares=cpu_shares,
            debug=debug,
            default_address_pools=default_address_pools,
            default_runtime=default_runtime,
            docker_root_dir=docker_root_dir,
            driver=driver,
            driver_status=driver_status,
            experimental_build=experimental_build,
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            id=id,
            images=images,
            index_server_address=index_server_address,
            init_binary=init_binary,
            init_commit=init_commit,
            ipv4_forwarding=ipv4_forwarding,
            isolation=isolation,
            kernel_memory=kernel_memory,
            kernel_memory_tcp=kernel_memory_tcp,
            kernel_version=kernel_version,
            labels=labels,
            live_restore_enabled=live_restore_enabled,
            logging_driver=logging_driver,
            mem_total=mem_total,
            memory_limit=memory_limit,
            n_events_listener=n_events_listener,
            n_fd=n_fd,
            name=name,
            ncpu=ncpu,
            no_proxy=no_proxy,
            oom_kill_disable=oom_kill_disable,
            operating_system=operating_system,
            os_type=os_type,
            os_version=os_version,
            pids_limit=pids_limit,
            plugins=plugins,
            product_license=product_license,
            registry_config=registry_config,
            runc_commit=runc_commit,
            runtimes=runtimes,
            security_options=security_options,
            server_version=server_version,
            swap_limit=swap_limit,
            system_time=system_time,
            warnings=warnings,
        )

        docker_system_info.additional_properties = d
        return docker_system_info

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
