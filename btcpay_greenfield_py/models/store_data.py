from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkout_type import CheckoutType
from ..models.network_fee_mode import NetworkFeeMode
from ..models.speed_policy import SpeedPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_criteria_data import PaymentMethodCriteriaData
    from ..models.receipt_options import ReceiptOptions


T = TypeVar("T", bound="StoreData")


@_attrs_define
class StoreData:
    """
    Attributes:
        name (str | Unset): The name of the store
        website (None | str | Unset): The absolute url of the store
        support_url (None | str | Unset): The support URI of the store, can contain the placeholders `{OrderId}` and
            `{InvoiceId}`. Can be any valid URI, such as a website, email, and nostr.
        default_currency (str | Unset): The default currency of the store Default: 'USD'. Example: USD.
        invoice_expiration (float | Unset):  Default: 900.0. Example: 90.
        display_expiration_timer (float | Unset):  Default: 300.0. Example: 90.
        monitoring_expiration (float | Unset):  Default: 3600.0. Example: 90.
        speed_policy (SpeedPolicy | Unset): This is a risk mitigation parameter for the merchant to configure how they
            want to fulfill orders depending on the number of block confirmations for the transaction made by the consumer
            on the selected cryptocurrency.
            `"HighSpeed"`: 0 confirmations (1 confirmation if RBF enabled in transaction)
            `"MediumSpeed"`: 1 confirmation
            `"LowMediumSpeed"`: 2 confirmations
            `"LowSpeed"`: 6 confirmations
        lightning_description_template (None | str | Unset): The BOLT11 description of the lightning invoice in the
            checkout. You can use placeholders '{StoreName}', '{ItemDescription}' and '{OrderId}'.
        payment_tolerance (float | Unset): Consider an invoice fully paid, even if the payment is missing 'x' % of the
            full amount. Default: 0.0.
        archived (bool | Unset): If true, the store does not appear in the stores list by default. Default: False.
        anyone_can_create_invoice (bool | Unset): If true, then no authentication is needed to create invoices on this
            store. Default: False.
        requires_refund_email (bool | Unset): If true, the checkout page will ask to enter an email address before
            accessing payment information. Default: False.
        checkout_type (CheckoutType | Unset): `"V1"`: The original checkout form
            `"V2"`: The new experimental checkout form
        receipt (None | ReceiptOptions | Unset): Additional settings to customize the public receipt
        lightning_amount_in_satoshi (bool | Unset): If true, lightning payment methods show amount in satoshi in the
            checkout page. Default: False.
        lightning_private_route_hints (bool | Unset): Should private route hints be included in the lightning payment of
            the checkout page. Default: False.
        on_chain_with_ln_invoice_fallback (bool | Unset): Unify on-chain and lightning payment URL. Default: False.
        redirect_automatically (bool | Unset): After successfull payment, should the checkout page redirect the user
            automatically to the redirect URL of the invoice? Default: False.
        show_recommended_fee (bool | Unset):  Default: True.
        recommended_fee_block_target (int | Unset): The fee rate recommendation in the checkout page for the on-chain
            payment to be confirmed after 'x' blocks. Default: 1.
        default_lang (str | Unset): The default language to use in the checkout page. (The different translations
            available are listed
            [here](https://github.com/btcpayserver/btcpayserver/tree/master/BTCPayServer/wwwroot/locales) Default: 'en'.
        custom_logo (None | str | Unset): URL to a logo to include in the checkout page.
        custom_css (None | str | Unset): URL to a CSS stylesheet to include in the checkout page
        html_title (None | str | Unset): The HTML title of the checkout page (when you over the tab in your browser)
        network_fee_mode (NetworkFeeMode | Unset): Check whether network fee should be added to the invoice if on-chain
            payment is used. ([More information](https://docs.btcpayserver.org/FAQ/Stores/#add-network-fee-to-invoice-vary-
            with-mining-fees))
        pay_join_enabled (bool | Unset): If true, payjoin will be proposed in the checkout page if possible. ([More
            information](https://docs.btcpayserver.org/Payjoin/)) Default: False.
        auto_detect_language (bool | Unset): If true, the language on the checkout page will adapt to the language
            defined by the user's browser settings Default: False.
        show_pay_in_wallet_button (bool | Unset): If true, the "Pay in wallet" button will be shown on the checkout page
            (Checkout V2) Default: True.
        show_store_header (bool | Unset): If true, the store header will be shown on the checkout page (Checkout V2)
            Default: True.
        celebrate_payment (bool | Unset): If true, payments on the checkout page will be celebrated with confetti
            (Checkout V2) Default: True.
        play_sound_on_payment (bool | Unset): If true, sounds on the checkout page will be enabled (Checkout V2)
            Default: False.
        lazy_payment_methods (bool | Unset): If true, payment methods are enabled individually upon user interaction in
            the invoice Default: False.
        default_payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type.
            Available payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        payment_method_criteria (list[PaymentMethodCriteriaData] | None | Unset): The criteria required to activate
            specific payment methods.
        id (str | Unset): The id of the store
    """

    name: str | Unset = UNSET
    website: None | str | Unset = UNSET
    support_url: None | str | Unset = UNSET
    default_currency: str | Unset = "USD"
    invoice_expiration: float | Unset = 900.0
    display_expiration_timer: float | Unset = 300.0
    monitoring_expiration: float | Unset = 3600.0
    speed_policy: SpeedPolicy | Unset = UNSET
    lightning_description_template: None | str | Unset = UNSET
    payment_tolerance: float | Unset = 0.0
    archived: bool | Unset = False
    anyone_can_create_invoice: bool | Unset = False
    requires_refund_email: bool | Unset = False
    checkout_type: CheckoutType | Unset = UNSET
    receipt: None | ReceiptOptions | Unset = UNSET
    lightning_amount_in_satoshi: bool | Unset = False
    lightning_private_route_hints: bool | Unset = False
    on_chain_with_ln_invoice_fallback: bool | Unset = False
    redirect_automatically: bool | Unset = False
    show_recommended_fee: bool | Unset = True
    recommended_fee_block_target: int | Unset = 1
    default_lang: str | Unset = "en"
    custom_logo: None | str | Unset = UNSET
    custom_css: None | str | Unset = UNSET
    html_title: None | str | Unset = UNSET
    network_fee_mode: NetworkFeeMode | Unset = UNSET
    pay_join_enabled: bool | Unset = False
    auto_detect_language: bool | Unset = False
    show_pay_in_wallet_button: bool | Unset = True
    show_store_header: bool | Unset = True
    celebrate_payment: bool | Unset = True
    play_sound_on_payment: bool | Unset = False
    lazy_payment_methods: bool | Unset = False
    default_payment_method: str | Unset = UNSET
    payment_method_criteria: list[PaymentMethodCriteriaData] | None | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.receipt_options import ReceiptOptions

        name = self.name

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        support_url: None | str | Unset
        if isinstance(self.support_url, Unset):
            support_url = UNSET
        else:
            support_url = self.support_url

        default_currency = self.default_currency

        invoice_expiration = self.invoice_expiration

        display_expiration_timer = self.display_expiration_timer

        monitoring_expiration = self.monitoring_expiration

        speed_policy: str | Unset = UNSET
        if not isinstance(self.speed_policy, Unset):
            speed_policy = self.speed_policy.value

        lightning_description_template: None | str | Unset
        if isinstance(self.lightning_description_template, Unset):
            lightning_description_template = UNSET
        else:
            lightning_description_template = self.lightning_description_template

        payment_tolerance = self.payment_tolerance

        archived = self.archived

        anyone_can_create_invoice = self.anyone_can_create_invoice

        requires_refund_email = self.requires_refund_email

        checkout_type: str | Unset = UNSET
        if not isinstance(self.checkout_type, Unset):
            checkout_type = self.checkout_type.value

        receipt: dict[str, Any] | None | Unset
        if isinstance(self.receipt, Unset):
            receipt = UNSET
        elif isinstance(self.receipt, ReceiptOptions):
            receipt = self.receipt.to_dict()
        else:
            receipt = self.receipt

        lightning_amount_in_satoshi = self.lightning_amount_in_satoshi

        lightning_private_route_hints = self.lightning_private_route_hints

        on_chain_with_ln_invoice_fallback = self.on_chain_with_ln_invoice_fallback

        redirect_automatically = self.redirect_automatically

        show_recommended_fee = self.show_recommended_fee

        recommended_fee_block_target = self.recommended_fee_block_target

        default_lang = self.default_lang

        custom_logo: None | str | Unset
        if isinstance(self.custom_logo, Unset):
            custom_logo = UNSET
        else:
            custom_logo = self.custom_logo

        custom_css: None | str | Unset
        if isinstance(self.custom_css, Unset):
            custom_css = UNSET
        else:
            custom_css = self.custom_css

        html_title: None | str | Unset
        if isinstance(self.html_title, Unset):
            html_title = UNSET
        else:
            html_title = self.html_title

        network_fee_mode: str | Unset = UNSET
        if not isinstance(self.network_fee_mode, Unset):
            network_fee_mode = self.network_fee_mode.value

        pay_join_enabled = self.pay_join_enabled

        auto_detect_language = self.auto_detect_language

        show_pay_in_wallet_button = self.show_pay_in_wallet_button

        show_store_header = self.show_store_header

        celebrate_payment = self.celebrate_payment

        play_sound_on_payment = self.play_sound_on_payment

        lazy_payment_methods = self.lazy_payment_methods

        default_payment_method = self.default_payment_method

        payment_method_criteria: list[dict[str, Any]] | None | Unset
        if isinstance(self.payment_method_criteria, Unset):
            payment_method_criteria = UNSET
        elif isinstance(self.payment_method_criteria, list):
            payment_method_criteria = []
            for payment_method_criteria_type_0_item_data in self.payment_method_criteria:
                payment_method_criteria_type_0_item = payment_method_criteria_type_0_item_data.to_dict()
                payment_method_criteria.append(payment_method_criteria_type_0_item)

        else:
            payment_method_criteria = self.payment_method_criteria

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if website is not UNSET:
            field_dict["website"] = website
        if support_url is not UNSET:
            field_dict["supportUrl"] = support_url
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if invoice_expiration is not UNSET:
            field_dict["invoiceExpiration"] = invoice_expiration
        if display_expiration_timer is not UNSET:
            field_dict["displayExpirationTimer"] = display_expiration_timer
        if monitoring_expiration is not UNSET:
            field_dict["monitoringExpiration"] = monitoring_expiration
        if speed_policy is not UNSET:
            field_dict["speedPolicy"] = speed_policy
        if lightning_description_template is not UNSET:
            field_dict["lightningDescriptionTemplate"] = lightning_description_template
        if payment_tolerance is not UNSET:
            field_dict["paymentTolerance"] = payment_tolerance
        if archived is not UNSET:
            field_dict["archived"] = archived
        if anyone_can_create_invoice is not UNSET:
            field_dict["anyoneCanCreateInvoice"] = anyone_can_create_invoice
        if requires_refund_email is not UNSET:
            field_dict["requiresRefundEmail"] = requires_refund_email
        if checkout_type is not UNSET:
            field_dict["checkoutType"] = checkout_type
        if receipt is not UNSET:
            field_dict["receipt"] = receipt
        if lightning_amount_in_satoshi is not UNSET:
            field_dict["lightningAmountInSatoshi"] = lightning_amount_in_satoshi
        if lightning_private_route_hints is not UNSET:
            field_dict["lightningPrivateRouteHints"] = lightning_private_route_hints
        if on_chain_with_ln_invoice_fallback is not UNSET:
            field_dict["onChainWithLnInvoiceFallback"] = on_chain_with_ln_invoice_fallback
        if redirect_automatically is not UNSET:
            field_dict["redirectAutomatically"] = redirect_automatically
        if show_recommended_fee is not UNSET:
            field_dict["showRecommendedFee"] = show_recommended_fee
        if recommended_fee_block_target is not UNSET:
            field_dict["recommendedFeeBlockTarget"] = recommended_fee_block_target
        if default_lang is not UNSET:
            field_dict["defaultLang"] = default_lang
        if custom_logo is not UNSET:
            field_dict["customLogo"] = custom_logo
        if custom_css is not UNSET:
            field_dict["customCSS"] = custom_css
        if html_title is not UNSET:
            field_dict["htmlTitle"] = html_title
        if network_fee_mode is not UNSET:
            field_dict["networkFeeMode"] = network_fee_mode
        if pay_join_enabled is not UNSET:
            field_dict["payJoinEnabled"] = pay_join_enabled
        if auto_detect_language is not UNSET:
            field_dict["autoDetectLanguage"] = auto_detect_language
        if show_pay_in_wallet_button is not UNSET:
            field_dict["showPayInWalletButton"] = show_pay_in_wallet_button
        if show_store_header is not UNSET:
            field_dict["showStoreHeader"] = show_store_header
        if celebrate_payment is not UNSET:
            field_dict["celebratePayment"] = celebrate_payment
        if play_sound_on_payment is not UNSET:
            field_dict["playSoundOnPayment"] = play_sound_on_payment
        if lazy_payment_methods is not UNSET:
            field_dict["lazyPaymentMethods"] = lazy_payment_methods
        if default_payment_method is not UNSET:
            field_dict["defaultPaymentMethod"] = default_payment_method
        if payment_method_criteria is not UNSET:
            field_dict["paymentMethodCriteria"] = payment_method_criteria
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_method_criteria_data import PaymentMethodCriteriaData
        from ..models.receipt_options import ReceiptOptions

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_support_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_url = _parse_support_url(d.pop("supportUrl", UNSET))

        default_currency = d.pop("defaultCurrency", UNSET)

        invoice_expiration = d.pop("invoiceExpiration", UNSET)

        display_expiration_timer = d.pop("displayExpirationTimer", UNSET)

        monitoring_expiration = d.pop("monitoringExpiration", UNSET)

        _speed_policy = d.pop("speedPolicy", UNSET)
        speed_policy: SpeedPolicy | Unset
        if isinstance(_speed_policy, Unset):
            speed_policy = UNSET
        else:
            speed_policy = SpeedPolicy(_speed_policy)

        def _parse_lightning_description_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lightning_description_template = _parse_lightning_description_template(
            d.pop("lightningDescriptionTemplate", UNSET)
        )

        payment_tolerance = d.pop("paymentTolerance", UNSET)

        archived = d.pop("archived", UNSET)

        anyone_can_create_invoice = d.pop("anyoneCanCreateInvoice", UNSET)

        requires_refund_email = d.pop("requiresRefundEmail", UNSET)

        _checkout_type = d.pop("checkoutType", UNSET)
        checkout_type: CheckoutType | Unset
        if isinstance(_checkout_type, Unset):
            checkout_type = UNSET
        else:
            checkout_type = CheckoutType(_checkout_type)

        def _parse_receipt(data: object) -> None | ReceiptOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                receipt_type_1 = ReceiptOptions.from_dict(data)

                return receipt_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReceiptOptions | Unset, data)

        receipt = _parse_receipt(d.pop("receipt", UNSET))

        lightning_amount_in_satoshi = d.pop("lightningAmountInSatoshi", UNSET)

        lightning_private_route_hints = d.pop("lightningPrivateRouteHints", UNSET)

        on_chain_with_ln_invoice_fallback = d.pop("onChainWithLnInvoiceFallback", UNSET)

        redirect_automatically = d.pop("redirectAutomatically", UNSET)

        show_recommended_fee = d.pop("showRecommendedFee", UNSET)

        recommended_fee_block_target = d.pop("recommendedFeeBlockTarget", UNSET)

        default_lang = d.pop("defaultLang", UNSET)

        def _parse_custom_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_logo = _parse_custom_logo(d.pop("customLogo", UNSET))

        def _parse_custom_css(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_css = _parse_custom_css(d.pop("customCSS", UNSET))

        def _parse_html_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        html_title = _parse_html_title(d.pop("htmlTitle", UNSET))

        _network_fee_mode = d.pop("networkFeeMode", UNSET)
        network_fee_mode: NetworkFeeMode | Unset
        if isinstance(_network_fee_mode, Unset):
            network_fee_mode = UNSET
        else:
            network_fee_mode = NetworkFeeMode(_network_fee_mode)

        pay_join_enabled = d.pop("payJoinEnabled", UNSET)

        auto_detect_language = d.pop("autoDetectLanguage", UNSET)

        show_pay_in_wallet_button = d.pop("showPayInWalletButton", UNSET)

        show_store_header = d.pop("showStoreHeader", UNSET)

        celebrate_payment = d.pop("celebratePayment", UNSET)

        play_sound_on_payment = d.pop("playSoundOnPayment", UNSET)

        lazy_payment_methods = d.pop("lazyPaymentMethods", UNSET)

        default_payment_method = d.pop("defaultPaymentMethod", UNSET)

        def _parse_payment_method_criteria(data: object) -> list[PaymentMethodCriteriaData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_method_criteria_type_0 = []
                _payment_method_criteria_type_0 = data
                for payment_method_criteria_type_0_item_data in _payment_method_criteria_type_0:
                    payment_method_criteria_type_0_item = PaymentMethodCriteriaData.from_dict(
                        payment_method_criteria_type_0_item_data
                    )

                    payment_method_criteria_type_0.append(payment_method_criteria_type_0_item)

                return payment_method_criteria_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PaymentMethodCriteriaData] | None | Unset, data)

        payment_method_criteria = _parse_payment_method_criteria(d.pop("paymentMethodCriteria", UNSET))

        id = d.pop("id", UNSET)

        store_data = cls(
            name=name,
            website=website,
            support_url=support_url,
            default_currency=default_currency,
            invoice_expiration=invoice_expiration,
            display_expiration_timer=display_expiration_timer,
            monitoring_expiration=monitoring_expiration,
            speed_policy=speed_policy,
            lightning_description_template=lightning_description_template,
            payment_tolerance=payment_tolerance,
            archived=archived,
            anyone_can_create_invoice=anyone_can_create_invoice,
            requires_refund_email=requires_refund_email,
            checkout_type=checkout_type,
            receipt=receipt,
            lightning_amount_in_satoshi=lightning_amount_in_satoshi,
            lightning_private_route_hints=lightning_private_route_hints,
            on_chain_with_ln_invoice_fallback=on_chain_with_ln_invoice_fallback,
            redirect_automatically=redirect_automatically,
            show_recommended_fee=show_recommended_fee,
            recommended_fee_block_target=recommended_fee_block_target,
            default_lang=default_lang,
            custom_logo=custom_logo,
            custom_css=custom_css,
            html_title=html_title,
            network_fee_mode=network_fee_mode,
            pay_join_enabled=pay_join_enabled,
            auto_detect_language=auto_detect_language,
            show_pay_in_wallet_button=show_pay_in_wallet_button,
            show_store_header=show_store_header,
            celebrate_payment=celebrate_payment,
            play_sound_on_payment=play_sound_on_payment,
            lazy_payment_methods=lazy_payment_methods,
            default_payment_method=default_payment_method,
            payment_method_criteria=payment_method_criteria,
            id=id,
        )

        store_data.additional_properties = d
        return store_data

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
