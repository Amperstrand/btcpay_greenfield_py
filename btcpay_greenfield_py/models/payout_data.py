from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payout_state import PayoutState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payout_data_general_information import PayoutDataGeneralInformation
    from ..models.payout_payment_proof_type_0 import PayoutPaymentProofType0
    from ..models.payout_payment_proof_type_1 import PayoutPaymentProofType1


T = TypeVar("T", bound="PayoutData")


@_attrs_define
class PayoutData:
    """
    Attributes:
        id (str | Unset): The id of the payout
        revision (int | Unset): The revision number of the payout. This revision number is incremented when the payout
            amount or destination is modified before the approval.
        pull_payment_id (str | Unset): The id of the pull payment this payout belongs to
        date (str | Unset): The creation date of the payout as a unix timestamp
        destination (str | Unset): The destination of the payout (can be an address or a BIP21 url) Example:
            1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.
        amount (str | Unset): The amount of the payout in the currency of the pull payment (eg. USD). Example: 10399.18.
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        crypto_code (str | Unset): Crypto code of the payment method of the payout (e.g., "BTC" or "LTC") Example: BTC.
        payment_method_amount (None | str | Unset): The amount of the payout in the currency of the payment method (eg.
            BTC). This is only available from the `AwaitingPayment` state. Example: 1.12300000.
        state (PayoutState | Unset): The state of the payout (`AwaitingApproval`, `AwaitingPayment`, `InProgress`,
            `Completed`, `Cancelled`) Example: AwaitingPayment.
        payment_proof (PayoutPaymentProofType0 | PayoutPaymentProofType1 | Unset): Additional information around how the
            payout is being or has been paid out. The mentioned properties are all optional (except `proofType`) and you can
            introduce any json format you wish.
        metadata (PayoutDataGeneralInformation | Unset): Additional information around the payout that can be supplied.
            The mentioned properties are all optional and you can introduce any json format you wish. Example: {'source':
            'Payout created through the API'}.
    """

    id: str | Unset = UNSET
    revision: int | Unset = UNSET
    pull_payment_id: str | Unset = UNSET
    date: str | Unset = UNSET
    destination: str | Unset = UNSET
    amount: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    crypto_code: str | Unset = UNSET
    payment_method_amount: None | str | Unset = UNSET
    state: PayoutState | Unset = UNSET
    payment_proof: PayoutPaymentProofType0 | PayoutPaymentProofType1 | Unset = UNSET
    metadata: PayoutDataGeneralInformation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payout_payment_proof_type_0 import PayoutPaymentProofType0

        id = self.id

        revision = self.revision

        pull_payment_id = self.pull_payment_id

        date = self.date

        destination = self.destination

        amount = self.amount

        payment_method = self.payment_method

        crypto_code = self.crypto_code

        payment_method_amount: None | str | Unset
        if isinstance(self.payment_method_amount, Unset):
            payment_method_amount = UNSET
        else:
            payment_method_amount = self.payment_method_amount

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

        metadata: dict[str, Any] | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if pull_payment_id is not UNSET:
            field_dict["pullPaymentId"] = pull_payment_id
        if date is not UNSET:
            field_dict["date"] = date
        if destination is not UNSET:
            field_dict["destination"] = destination
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code
        if payment_method_amount is not UNSET:
            field_dict["paymentMethodAmount"] = payment_method_amount
        if state is not UNSET:
            field_dict["state"] = state
        if payment_proof is not UNSET:
            field_dict["paymentProof"] = payment_proof
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payout_data_general_information import PayoutDataGeneralInformation
        from ..models.payout_payment_proof_type_0 import PayoutPaymentProofType0
        from ..models.payout_payment_proof_type_1 import PayoutPaymentProofType1

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        pull_payment_id = d.pop("pullPaymentId", UNSET)

        date = d.pop("date", UNSET)

        destination = d.pop("destination", UNSET)

        amount = d.pop("amount", UNSET)

        payment_method = d.pop("paymentMethod", UNSET)

        crypto_code = d.pop("cryptoCode", UNSET)

        def _parse_payment_method_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method_amount = _parse_payment_method_amount(d.pop("paymentMethodAmount", UNSET))

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

        def _parse_metadata(data: object) -> PayoutDataGeneralInformation | Unset:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            metadata_general_information = PayoutDataGeneralInformation.from_dict(data)

            return metadata_general_information

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        payout_data = cls(
            id=id,
            revision=revision,
            pull_payment_id=pull_payment_id,
            date=date,
            destination=destination,
            amount=amount,
            payment_method=payment_method,
            crypto_code=crypto_code,
            payment_method_amount=payment_method_amount,
            state=state,
            payment_proof=payment_proof,
            metadata=metadata,
        )

        payout_data.additional_properties = d
        return payout_data

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
