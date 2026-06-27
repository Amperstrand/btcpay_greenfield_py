from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLightningAutomatedTransferSettings")


@_attrs_define
class UpdateLightningAutomatedTransferSettings:
    """
    Attributes:
        interval_seconds (float | Unset):  Example: 90.
        cancel_payout_after_failures (float | None | Unset): How many failures should the processor tolerate before
            cancelling the payout
        process_new_payouts_instantly (bool | Unset): Skip the interval when ane eligible payout has been approved (or
            created with pre-approval) Default: False.
    """

    interval_seconds: float | Unset = UNSET
    cancel_payout_after_failures: float | None | Unset = UNSET
    process_new_payouts_instantly: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        interval_seconds = self.interval_seconds

        cancel_payout_after_failures: float | None | Unset
        if isinstance(self.cancel_payout_after_failures, Unset):
            cancel_payout_after_failures = UNSET
        else:
            cancel_payout_after_failures = self.cancel_payout_after_failures

        process_new_payouts_instantly = self.process_new_payouts_instantly

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if interval_seconds is not UNSET:
            field_dict["intervalSeconds"] = interval_seconds
        if cancel_payout_after_failures is not UNSET:
            field_dict["cancelPayoutAfterFailures"] = cancel_payout_after_failures
        if process_new_payouts_instantly is not UNSET:
            field_dict["processNewPayoutsInstantly"] = process_new_payouts_instantly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval_seconds = d.pop("intervalSeconds", UNSET)

        def _parse_cancel_payout_after_failures(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cancel_payout_after_failures = _parse_cancel_payout_after_failures(d.pop("cancelPayoutAfterFailures", UNSET))

        process_new_payouts_instantly = d.pop("processNewPayoutsInstantly", UNSET)

        update_lightning_automated_transfer_settings = cls(
            interval_seconds=interval_seconds,
            cancel_payout_after_failures=cancel_payout_after_failures,
            process_new_payouts_instantly=process_new_payouts_instantly,
        )

        return update_lightning_automated_transfer_settings
