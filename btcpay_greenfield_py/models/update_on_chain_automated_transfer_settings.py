from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOnChainAutomatedTransferSettings")


@_attrs_define
class UpdateOnChainAutomatedTransferSettings:
    """
    Attributes:
        fee_target_block (float | None | Unset): How many blocks should the fee rate calculation target to confirm in.
            Set to 1 if not provided
        interval_seconds (float | Unset):  Example: 90.
        threshold (str | Unset): Only process payouts when this payout sum is reached. Example: 0.1.
        process_new_payouts_instantly (bool | Unset): Skip the interval when ane eligible payout has been approved (or
            created with pre-approval) Default: False.
    """

    fee_target_block: float | None | Unset = UNSET
    interval_seconds: float | Unset = UNSET
    threshold: str | Unset = UNSET
    process_new_payouts_instantly: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        fee_target_block: float | None | Unset
        if isinstance(self.fee_target_block, Unset):
            fee_target_block = UNSET
        else:
            fee_target_block = self.fee_target_block

        interval_seconds = self.interval_seconds

        threshold = self.threshold

        process_new_payouts_instantly = self.process_new_payouts_instantly

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fee_target_block is not UNSET:
            field_dict["feeTargetBlock"] = fee_target_block
        if interval_seconds is not UNSET:
            field_dict["intervalSeconds"] = interval_seconds
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if process_new_payouts_instantly is not UNSET:
            field_dict["processNewPayoutsInstantly"] = process_new_payouts_instantly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fee_target_block(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fee_target_block = _parse_fee_target_block(d.pop("feeTargetBlock", UNSET))

        interval_seconds = d.pop("intervalSeconds", UNSET)

        threshold = d.pop("threshold", UNSET)

        process_new_payouts_instantly = d.pop("processNewPayoutsInstantly", UNSET)

        update_on_chain_automated_transfer_settings = cls(
            fee_target_block=fee_target_block,
            interval_seconds=interval_seconds,
            threshold=threshold,
            process_new_payouts_instantly=process_new_payouts_instantly,
        )

        return update_on_chain_automated_transfer_settings
