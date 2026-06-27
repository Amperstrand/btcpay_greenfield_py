from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenLightningChannelRequest")


@_attrs_define
class OpenLightningChannelRequest:
    """
    Attributes:
        node_uri (str | Unset): Node URI in the form `pubkey@endpoint[:port]`
        channel_amount (str | Unset): The amount to fund (in satoshi)
        fee_rate (float | Unset): The amount to fund (in satoshi per byte)
    """

    node_uri: str | Unset = UNSET
    channel_amount: str | Unset = UNSET
    fee_rate: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        node_uri = self.node_uri

        channel_amount = self.channel_amount

        fee_rate = self.fee_rate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if node_uri is not UNSET:
            field_dict["nodeURI"] = node_uri
        if channel_amount is not UNSET:
            field_dict["channelAmount"] = channel_amount
        if fee_rate is not UNSET:
            field_dict["feeRate"] = fee_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_uri = d.pop("nodeURI", UNSET)

        channel_amount = d.pop("channelAmount", UNSET)

        fee_rate = d.pop("feeRate", UNSET)

        open_lightning_channel_request = cls(
            node_uri=node_uri,
            channel_amount=channel_amount,
            fee_rate=fee_rate,
        )

        return open_lightning_channel_request
