from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payout_state import PayoutState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payout_payment_proof_type_0 import PayoutPaymentProofType0
    from ..models.payout_payment_proof_type_1 import PayoutPaymentProofType1


T = TypeVar("T", bound="PullPaymentsMarkPayoutBody")


@_attrs_define
class PullPaymentsMarkPayoutBody:
    """
    Attributes:
        state (PayoutState | Unset): The state of the payout (`AwaitingApproval`, `AwaitingPayment`, `InProgress`,
            `Completed`, `Cancelled`) Example: AwaitingPayment.
        payment_proof (PayoutPaymentProofType0 | PayoutPaymentProofType1 | Unset): Additional information around how the
            payout is being or has been paid out. The mentioned properties are all optional (except `proofType`) and you can
            introduce any json format you wish.
    """

    state: PayoutState | Unset = UNSET
    payment_proof: PayoutPaymentProofType0 | PayoutPaymentProofType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payout_payment_proof_type_0 import PayoutPaymentProofType0

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        payment_proof: dict[str, Any] | Unset
        if isinstance(self.payment_proof, Unset):
            payment_proof = UNSET
        elif isinstance(self.payment_proof, PayoutPaymentProofType0):
            payment_proof = self.payment_proof.to_dict()
        else:
            payment_proof = self.payment_proof.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if payment_proof is not UNSET:
            field_dict["paymentProof"] = payment_proof

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payout_payment_proof_type_0 import PayoutPaymentProofType0
        from ..models.payout_payment_proof_type_1 import PayoutPaymentProofType1

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: PayoutState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PayoutState(_state)

        def _parse_payment_proof(data: object) -> PayoutPaymentProofType0 | PayoutPaymentProofType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_payout_payment_proof_type_0 = PayoutPaymentProofType0.from_dict(data)

                return componentsschemas_payout_payment_proof_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_payout_payment_proof_type_1 = PayoutPaymentProofType1.from_dict(data)

            return componentsschemas_payout_payment_proof_type_1

        payment_proof = _parse_payment_proof(d.pop("paymentProof", UNSET))

        pull_payments_mark_payout_body = cls(
            state=state,
            payment_proof=payment_proof,
        )

        pull_payments_mark_payout_body.additional_properties = d
        return pull_payments_mark_payout_body

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
