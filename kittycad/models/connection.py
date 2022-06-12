import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.cluster import Cluster
from ..models.gateway import Gateway
from ..models.jetstream import Jetstream
from ..models.leaf_node import LeafNode
from ..models.duration import Duration
from ..types import UNSET, Unset

T = TypeVar("T", bound="Connection")


@attr.s(auto_attribs=True)
class Connection:
    """ """
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
