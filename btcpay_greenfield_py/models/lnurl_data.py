from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LNURLData")


@_attrs_define
class LNURLData:
    """
    Attributes:
        lnurl_bech_32 (str | Unset): Bech32 representation of LNURL Example: lightning:lnurl1dp68gup69uhnzv3h9cczuvpwxya
            rzdp3xsez7sj5gvh42j2vfe24ynp0wa5hg6rywfshwtmswqhngvntdd6x6uzvx4jrvu2kvvur23n8v46rwjpexcc45563fn53w7.
        lnurl_uri (str | Unset): URI representation of LNURL Example:
            lnurlw://example.com/BTC/UILNURL/withdraw/pp/42kktmpL5d6qVc85Fget7H961ZSQ.
    """

    lnurl_bech_32: str | Unset = UNSET
    lnurl_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lnurl_bech_32 = self.lnurl_bech_32

        lnurl_uri = self.lnurl_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lnurl_bech_32 is not UNSET:
            field_dict["lnurlBech32"] = lnurl_bech_32
        if lnurl_uri is not UNSET:
            field_dict["lnurlUri"] = lnurl_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lnurl_bech_32 = d.pop("lnurlBech32", UNSET)

        lnurl_uri = d.pop("lnurlUri", UNSET)

        lnurl_data = cls(
            lnurl_bech_32=lnurl_bech_32,
            lnurl_uri=lnurl_uri,
        )

        lnurl_data.additional_properties = d
        return lnurl_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
