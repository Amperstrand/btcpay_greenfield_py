from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_chain_wallet_object_link_link_data import OnChainWalletObjectLinkLinkData
    from ..models.on_chain_wallet_object_link_object_data import OnChainWalletObjectLinkObjectData


T = TypeVar("T", bound="OnChainWalletObjectLink")


@_attrs_define
class OnChainWalletObjectLink:
    """
    Attributes:
        type_ (str | Unset): The type of wallet object
        id (str | Unset): The identifier of the wallet object (unique per type, per wallet)
        link_data (OnChainWalletObjectLinkLinkData | Unset): The data of the link
        object_data (OnChainWalletObjectLinkObjectData | Unset): The data of the neighbour's node (`null` if there isn't
            any data or `includeNeighbourData` is `false`)
    """

    type_: str | Unset = UNSET
    id: str | Unset = UNSET
    link_data: OnChainWalletObjectLinkLinkData | Unset = UNSET
    object_data: OnChainWalletObjectLinkObjectData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        link_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_data, Unset):
            link_data = self.link_data.to_dict()

        object_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_data, Unset):
            object_data = self.object_data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if link_data is not UNSET:
            field_dict["linkData"] = link_data
        if object_data is not UNSET:
            field_dict["objectData"] = object_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.on_chain_wallet_object_link_link_data import OnChainWalletObjectLinkLinkData
        from ..models.on_chain_wallet_object_link_object_data import OnChainWalletObjectLinkObjectData

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        _link_data = d.pop("linkData", UNSET)
        link_data: OnChainWalletObjectLinkLinkData | Unset
        if isinstance(_link_data, Unset):
            link_data = UNSET
        else:
            link_data = OnChainWalletObjectLinkLinkData.from_dict(_link_data)

        _object_data = d.pop("objectData", UNSET)
        object_data: OnChainWalletObjectLinkObjectData | Unset
        if isinstance(_object_data, Unset):
            object_data = UNSET
        else:
            object_data = OnChainWalletObjectLinkObjectData.from_dict(_object_data)

        on_chain_wallet_object_link = cls(
            type_=type_,
            id=id,
            link_data=link_data,
            object_data=object_data,
        )

        return on_chain_wallet_object_link
