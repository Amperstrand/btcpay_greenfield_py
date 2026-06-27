from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectToNodeRequest")


@_attrs_define
class ConnectToNodeRequest:
    """
    Attributes:
        node_uri (None | str | Unset): Node URI in the form `pubkey@endpoint[:port]`
    """

    node_uri: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        node_uri: None | str | Unset
        if isinstance(self.node_uri, Unset):
            node_uri = UNSET
        else:
            node_uri = self.node_uri

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if node_uri is not UNSET:
            field_dict["nodeURI"] = node_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_node_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_uri = _parse_node_uri(d.pop("nodeURI", UNSET))

        connect_to_node_request = cls(
            node_uri=node_uri,
        )

        return connect_to_node_request
