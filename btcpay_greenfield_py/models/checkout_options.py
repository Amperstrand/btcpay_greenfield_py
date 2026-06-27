from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.checkout_options_checkout_type_type_1 import CheckoutOptionsCheckoutTypeType1
from ..models.checkout_options_checkout_type_type_2_type_1 import CheckoutOptionsCheckoutTypeType2Type1
from ..models.checkout_options_checkout_type_type_3_type_1 import CheckoutOptionsCheckoutTypeType3Type1
from ..models.speed_policy import SpeedPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutOptions")


@_attrs_define
class CheckoutOptions:
    """
    Attributes:
        speed_policy (None | SpeedPolicy | Unset):
        payment_methods (list[str] | None | Unset): A specific set of payment methods to use for this invoice (ie. BTC,
            BTC-LightningNetwork). By default, select all payment methods enabled in the store.
        default_payment_method (None | str | Unset): Default payment type for the invoice (e.g., BTC, BTC-
            LightningNetwork). Default payment method set for the store is used if this parameter is not specified.
        lazy_payment_methods (bool | None | Unset): If true, payment methods are enabled individually upon user
            interaction in the invoice. Default to store's settings'
        expiration_minutes (float | None | Unset): The number of minutes after which an invoice becomes expired.
            Defaults to the store's settings. (The default store settings is 15)
        monitoring_minutes (float | Unset):  Example: 90.
        payment_tolerance (float | None | Unset): A percentage determining whether to count the invoice as paid when the
            invoice is paid within the specified margin of error. Defaults to the store's settings. (The default store
            settings is 100)
        redirect_url (None | str | Unset): When the customer has paid the invoice, the URL where the customer will be
            redirected when clicking on the `return to store` button. You can use placeholders `{InvoiceId}` or `{OrderId}`
            in the URL, BTCPay Server will replace those with this invoice `id` or `metadata.orderId` respectively.
        redirect_automatically (bool | None | Unset): When the customer has paid the invoice, and a `redirectURL` is
            set, the checkout is redirected to `redirectURL` automatically if `redirectAutomatically` is true. Defaults to
            the store's settings. (The default store settings is false)
        requires_refund_email (bool | None | Unset): Invoice will require user to provide a refund email if this option
            is set to `true`. Has no effect if `buyerEmail` metadata is set as there is no email to collect in this case.
        checkout_type (CheckoutOptionsCheckoutTypeType1 | CheckoutOptionsCheckoutTypeType2Type1 |
            CheckoutOptionsCheckoutTypeType3Type1 | None | Unset): `"V1"`: The original checkout form
            `"V2"`: The new experimental checkout form.
            If `null` or unspecified, the store's settings will be used.
        default_language (None | str | Unset): The language code (eg. en-US, en, fr-FR...) of the language presented to
            your customer in the checkout page. BTCPay Server tries to match the best language available. If null or not
            set, will fallback on the store's default language. You can see the list of language codes with [this
            operation](#operation/langCodes).
    """

    speed_policy: None | SpeedPolicy | Unset = UNSET
    payment_methods: list[str] | None | Unset = UNSET
    default_payment_method: None | str | Unset = UNSET
    lazy_payment_methods: bool | None | Unset = UNSET
    expiration_minutes: float | None | Unset = UNSET
    monitoring_minutes: float | Unset = UNSET
    payment_tolerance: float | None | Unset = UNSET
    redirect_url: None | str | Unset = UNSET
    redirect_automatically: bool | None | Unset = UNSET
    requires_refund_email: bool | None | Unset = UNSET
    checkout_type: (
        CheckoutOptionsCheckoutTypeType1
        | CheckoutOptionsCheckoutTypeType2Type1
        | CheckoutOptionsCheckoutTypeType3Type1
        | None
        | Unset
    ) = UNSET
    default_language: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        speed_policy: None | str | Unset
        if isinstance(self.speed_policy, Unset):
            speed_policy = UNSET
        elif isinstance(self.speed_policy, SpeedPolicy):
            speed_policy = self.speed_policy.value
        else:
            speed_policy = self.speed_policy

        payment_methods: list[str] | None | Unset
        if isinstance(self.payment_methods, Unset):
            payment_methods = UNSET
        elif isinstance(self.payment_methods, list):
            payment_methods = self.payment_methods

        else:
            payment_methods = self.payment_methods

        default_payment_method: None | str | Unset
        if isinstance(self.default_payment_method, Unset):
            default_payment_method = UNSET
        else:
            default_payment_method = self.default_payment_method

        lazy_payment_methods: bool | None | Unset
        if isinstance(self.lazy_payment_methods, Unset):
            lazy_payment_methods = UNSET
        else:
            lazy_payment_methods = self.lazy_payment_methods

        expiration_minutes: float | None | Unset
        if isinstance(self.expiration_minutes, Unset):
            expiration_minutes = UNSET
        else:
            expiration_minutes = self.expiration_minutes

        monitoring_minutes = self.monitoring_minutes

        payment_tolerance: float | None | Unset
        if isinstance(self.payment_tolerance, Unset):
            payment_tolerance = UNSET
        else:
            payment_tolerance = self.payment_tolerance

        redirect_url: None | str | Unset
        if isinstance(self.redirect_url, Unset):
            redirect_url = UNSET
        else:
            redirect_url = self.redirect_url

        redirect_automatically: bool | None | Unset
        if isinstance(self.redirect_automatically, Unset):
            redirect_automatically = UNSET
        else:
            redirect_automatically = self.redirect_automatically

        requires_refund_email: bool | None | Unset
        if isinstance(self.requires_refund_email, Unset):
            requires_refund_email = UNSET
        else:
            requires_refund_email = self.requires_refund_email

        checkout_type: None | str | Unset
        if isinstance(self.checkout_type, Unset):
            checkout_type = UNSET
        elif isinstance(self.checkout_type, CheckoutOptionsCheckoutTypeType1):
            checkout_type = self.checkout_type.value
        elif isinstance(self.checkout_type, CheckoutOptionsCheckoutTypeType2Type1):
            checkout_type = self.checkout_type.value
        elif isinstance(self.checkout_type, CheckoutOptionsCheckoutTypeType3Type1):
            checkout_type = self.checkout_type.value
        else:
            checkout_type = self.checkout_type

        default_language: None | str | Unset
        if isinstance(self.default_language, Unset):
            default_language = UNSET
        else:
            default_language = self.default_language

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if speed_policy is not UNSET:
            field_dict["speedPolicy"] = speed_policy
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods
        if default_payment_method is not UNSET:
            field_dict["defaultPaymentMethod"] = default_payment_method
        if lazy_payment_methods is not UNSET:
            field_dict["lazyPaymentMethods"] = lazy_payment_methods
        if expiration_minutes is not UNSET:
            field_dict["expirationMinutes"] = expiration_minutes
        if monitoring_minutes is not UNSET:
            field_dict["monitoringMinutes"] = monitoring_minutes
        if payment_tolerance is not UNSET:
            field_dict["paymentTolerance"] = payment_tolerance
        if redirect_url is not UNSET:
            field_dict["redirectURL"] = redirect_url
        if redirect_automatically is not UNSET:
            field_dict["redirectAutomatically"] = redirect_automatically
        if requires_refund_email is not UNSET:
            field_dict["requiresRefundEmail"] = requires_refund_email
        if checkout_type is not UNSET:
            field_dict["checkoutType"] = checkout_type
        if default_language is not UNSET:
            field_dict["defaultLanguage"] = default_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_speed_policy(data: object) -> None | SpeedPolicy | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                speed_policy_type_1 = SpeedPolicy(data)

                return speed_policy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpeedPolicy | Unset, data)

        speed_policy = _parse_speed_policy(d.pop("speedPolicy", UNSET))

        def _parse_payment_methods(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_methods_type_0 = cast(list[str], data)

                return payment_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        payment_methods = _parse_payment_methods(d.pop("paymentMethods", UNSET))

        def _parse_default_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_payment_method = _parse_default_payment_method(d.pop("defaultPaymentMethod", UNSET))

        def _parse_lazy_payment_methods(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        lazy_payment_methods = _parse_lazy_payment_methods(d.pop("lazyPaymentMethods", UNSET))

        def _parse_expiration_minutes(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expiration_minutes = _parse_expiration_minutes(d.pop("expirationMinutes", UNSET))

        monitoring_minutes = d.pop("monitoringMinutes", UNSET)

        def _parse_payment_tolerance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payment_tolerance = _parse_payment_tolerance(d.pop("paymentTolerance", UNSET))

        def _parse_redirect_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_url = _parse_redirect_url(d.pop("redirectURL", UNSET))

        def _parse_redirect_automatically(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        redirect_automatically = _parse_redirect_automatically(d.pop("redirectAutomatically", UNSET))

        def _parse_requires_refund_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        requires_refund_email = _parse_requires_refund_email(d.pop("requiresRefundEmail", UNSET))

        def _parse_checkout_type(
            data: object,
        ) -> (
            CheckoutOptionsCheckoutTypeType1
            | CheckoutOptionsCheckoutTypeType2Type1
            | CheckoutOptionsCheckoutTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkout_type_type_1 = CheckoutOptionsCheckoutTypeType1(data)

                return checkout_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkout_type_type_2_type_1 = CheckoutOptionsCheckoutTypeType2Type1(data)

                return checkout_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkout_type_type_3_type_1 = CheckoutOptionsCheckoutTypeType3Type1(data)

                return checkout_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CheckoutOptionsCheckoutTypeType1
                | CheckoutOptionsCheckoutTypeType2Type1
                | CheckoutOptionsCheckoutTypeType3Type1
                | None
                | Unset,
                data,
            )

        checkout_type = _parse_checkout_type(d.pop("checkoutType", UNSET))

        def _parse_default_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_language = _parse_default_language(d.pop("defaultLanguage", UNSET))

        checkout_options = cls(
            speed_policy=speed_policy,
            payment_methods=payment_methods,
            default_payment_method=default_payment_method,
            lazy_payment_methods=lazy_payment_methods,
            expiration_minutes=expiration_minutes,
            monitoring_minutes=monitoring_minutes,
            payment_tolerance=payment_tolerance,
            redirect_url=redirect_url,
            redirect_automatically=redirect_automatically,
            requires_refund_email=requires_refund_email,
            checkout_type=checkout_type,
            default_language=default_language,
        )

        return checkout_options
