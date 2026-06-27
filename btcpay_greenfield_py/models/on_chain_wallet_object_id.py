from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainWalletObjectId")


@_attrs_define
class OnChainWalletObjectId:
    """
    Attributes:
        type_ (str | Unset): The type of wallet object
        id (str | Unset): The identifier of the wallet object (unique per type, per wallet)
    """

    type_: str | Unset = UNSET
    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        on_chain_wallet_object_id = cls(
            type_=type_,
            id=id,
        )

        return on_chain_wallet_object_id
