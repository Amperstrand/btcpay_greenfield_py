from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainAutomatedTransferSettings")


@_attrs_define
class OnChainAutomatedTransferSettings:
    """
    Attributes:
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        fee_target_block (float | Unset): How many blocks should the fee rate calculation target to confirm in.
        interval_seconds (float | Unset):  Example: 90.
        threshold (str | Unset): Only process payouts when this payout sum is reached. Example: 0.1.
        process_new_payouts_instantly (bool | Unset): Skip the interval when ane eligible payout has been approved (or
            created with pre-approval) Default: False.
    """

    payment_method: str | Unset = UNSET
    fee_target_block: float | Unset = UNSET
    interval_seconds: float | Unset = UNSET
    threshold: str | Unset = UNSET
    process_new_payouts_instantly: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        payment_method = self.payment_method

        fee_target_block = self.fee_target_block

        interval_seconds = self.interval_seconds

        threshold = self.threshold

        process_new_payouts_instantly = self.process_new_payouts_instantly

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
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
        payment_method = d.pop("paymentMethod", UNSET)

        fee_target_block = d.pop("feeTargetBlock", UNSET)

        interval_seconds = d.pop("intervalSeconds", UNSET)

        threshold = d.pop("threshold", UNSET)

        process_new_payouts_instantly = d.pop("processNewPayoutsInstantly", UNSET)

        on_chain_automated_transfer_settings = cls(
            payment_method=payment_method,
            fee_target_block=fee_target_block,
            interval_seconds=interval_seconds,
            threshold=threshold,
            process_new_payouts_instantly=process_new_payouts_instantly,
        )

        return on_chain_automated_transfer_settings
