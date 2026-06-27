from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkout_type import CheckoutType
from ..models.create_point_of_sale_app_request_default_view import CreatePointOfSaleAppRequestDefaultView
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePointOfSaleAppRequest")


@_attrs_define
class CreatePointOfSaleAppRequest:
    """
    Attributes:
        app_name (str | Unset): The name of the app (shown in admin UI)
        title (None | str | Unset): The title of the app (shown to the user)
        description (None | str | Unset): The description of the app
        template (None | str | Unset): Template for items available in the app
        default_view (CreatePointOfSaleAppRequestDefaultView | Unset): Template for items available in the app
        currency (None | str | Unset): Currency to use for the app. Defaults to the currency used by the store if not
            specified Example: BTC.
        show_custom_amount (bool | None | Unset): Whether to include a special item in the store which allows user to
            input a custom payment amount Default: False.
        show_discount (bool | None | Unset): Whether to allow user to input a discount amount. Applies to Cart view
            only. Not recommended for customer self-checkout Default: True.
        enable_tips (bool | None | Unset): Whether to allow user to input a tip amount. Applies to Cart and Light views
            only Default: True.
        custom_amount_pay_button_text (None | str | Unset): Payment button text which appears for items which allow user
            to input a custom amount Default: 'Pay'.
        fixed_amount_pay_button_text (None | str | Unset): Payment button text which appears for items which have a
            fixed price Default: 'Buy for {PRICE_HERE}'.
        tip_text (None | str | Unset): Prompt which appears next to the tip amount field if tipping is enabled Default:
            'Do you want to leave a tip?'.
        custom_css_link (None | str | Unset): Link to a custom CSS stylesheet to be used in the app
        embedded_css (None | str | Unset): Custom CSS to embed into the app
        notification_url (None | str | Unset): Callback notification url to POST to once when invoice is paid for and
            once when there are enough blockchain confirmations
        redirect_url (None | str | Unset): URL to redirect user to once invoice is paid
        redirect_automatically (bool | None | Unset): Whether to redirect user to redirect URL automatically once
            invoice is paid. Defaults to what is set in the store settings
        requires_refund_email (bool | None | Unset): Whether refund email is required when paying the invoice. Defaults
            to what is set in the store settings
        checkout_type (CheckoutType | Unset): `"V1"`: The original checkout form
            `"V2"`: The new experimental checkout form
        form_id (None | str | Unset): Form ID to request customer data
    """

    app_name: str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    template: None | str | Unset = UNSET
    default_view: CreatePointOfSaleAppRequestDefaultView | Unset = UNSET
    currency: None | str | Unset = UNSET
    show_custom_amount: bool | None | Unset = False
    show_discount: bool | None | Unset = True
    enable_tips: bool | None | Unset = True
    custom_amount_pay_button_text: None | str | Unset = "Pay"
    fixed_amount_pay_button_text: None | str | Unset = "Buy for {PRICE_HERE}"
    tip_text: None | str | Unset = "Do you want to leave a tip?"
    custom_css_link: None | str | Unset = UNSET
    embedded_css: None | str | Unset = UNSET
    notification_url: None | str | Unset = UNSET
    redirect_url: None | str | Unset = UNSET
    redirect_automatically: bool | None | Unset = UNSET
    requires_refund_email: bool | None | Unset = UNSET
    checkout_type: CheckoutType | Unset = UNSET
    form_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        default_view: str | Unset = UNSET
        if not isinstance(self.default_view, Unset):
            default_view = self.default_view.value

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        show_custom_amount: bool | None | Unset
        if isinstance(self.show_custom_amount, Unset):
            show_custom_amount = UNSET
        else:
            show_custom_amount = self.show_custom_amount

        show_discount: bool | None | Unset
        if isinstance(self.show_discount, Unset):
            show_discount = UNSET
        else:
            show_discount = self.show_discount

        enable_tips: bool | None | Unset
        if isinstance(self.enable_tips, Unset):
            enable_tips = UNSET
        else:
            enable_tips = self.enable_tips

        custom_amount_pay_button_text: None | str | Unset
        if isinstance(self.custom_amount_pay_button_text, Unset):
            custom_amount_pay_button_text = UNSET
        else:
            custom_amount_pay_button_text = self.custom_amount_pay_button_text

        fixed_amount_pay_button_text: None | str | Unset
        if isinstance(self.fixed_amount_pay_button_text, Unset):
            fixed_amount_pay_button_text = UNSET
        else:
            fixed_amount_pay_button_text = self.fixed_amount_pay_button_text

        tip_text: None | str | Unset
        if isinstance(self.tip_text, Unset):
            tip_text = UNSET
        else:
            tip_text = self.tip_text

        custom_css_link: None | str | Unset
        if isinstance(self.custom_css_link, Unset):
            custom_css_link = UNSET
        else:
            custom_css_link = self.custom_css_link

        embedded_css: None | str | Unset
        if isinstance(self.embedded_css, Unset):
            embedded_css = UNSET
        else:
            embedded_css = self.embedded_css

        notification_url: None | str | Unset
        if isinstance(self.notification_url, Unset):
            notification_url = UNSET
        else:
            notification_url = self.notification_url

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

        checkout_type: str | Unset = UNSET
        if not isinstance(self.checkout_type, Unset):
            checkout_type = self.checkout_type.value

        form_id: None | str | Unset
        if isinstance(self.form_id, Unset):
            form_id = UNSET
        else:
            form_id = self.form_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if template is not UNSET:
            field_dict["template"] = template
        if default_view is not UNSET:
            field_dict["defaultView"] = default_view
        if currency is not UNSET:
            field_dict["currency"] = currency
        if show_custom_amount is not UNSET:
            field_dict["showCustomAmount"] = show_custom_amount
        if show_discount is not UNSET:
            field_dict["showDiscount"] = show_discount
        if enable_tips is not UNSET:
            field_dict["enableTips"] = enable_tips
        if custom_amount_pay_button_text is not UNSET:
            field_dict["customAmountPayButtonText"] = custom_amount_pay_button_text
        if fixed_amount_pay_button_text is not UNSET:
            field_dict["fixedAmountPayButtonText"] = fixed_amount_pay_button_text
        if tip_text is not UNSET:
            field_dict["tipText"] = tip_text
        if custom_css_link is not UNSET:
            field_dict["customCSSLink"] = custom_css_link
        if embedded_css is not UNSET:
            field_dict["embeddedCSS"] = embedded_css
        if notification_url is not UNSET:
            field_dict["notificationUrl"] = notification_url
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if redirect_automatically is not UNSET:
            field_dict["redirectAutomatically"] = redirect_automatically
        if requires_refund_email is not UNSET:
            field_dict["requiresRefundEmail"] = requires_refund_email
        if checkout_type is not UNSET:
            field_dict["checkoutType"] = checkout_type
        if form_id is not UNSET:
            field_dict["formId"] = form_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_name = d.pop("appName", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        _default_view = d.pop("defaultView", UNSET)
        default_view: CreatePointOfSaleAppRequestDefaultView | Unset
        if isinstance(_default_view, Unset):
            default_view = UNSET
        else:
            default_view = CreatePointOfSaleAppRequestDefaultView(_default_view)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_show_custom_amount(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_custom_amount = _parse_show_custom_amount(d.pop("showCustomAmount", UNSET))

        def _parse_show_discount(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_discount = _parse_show_discount(d.pop("showDiscount", UNSET))

        def _parse_enable_tips(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_tips = _parse_enable_tips(d.pop("enableTips", UNSET))

        def _parse_custom_amount_pay_button_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_amount_pay_button_text = _parse_custom_amount_pay_button_text(d.pop("customAmountPayButtonText", UNSET))

        def _parse_fixed_amount_pay_button_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fixed_amount_pay_button_text = _parse_fixed_amount_pay_button_text(d.pop("fixedAmountPayButtonText", UNSET))

        def _parse_tip_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tip_text = _parse_tip_text(d.pop("tipText", UNSET))

        def _parse_custom_css_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_css_link = _parse_custom_css_link(d.pop("customCSSLink", UNSET))

        def _parse_embedded_css(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedded_css = _parse_embedded_css(d.pop("embeddedCSS", UNSET))

        def _parse_notification_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_url = _parse_notification_url(d.pop("notificationUrl", UNSET))

        def _parse_redirect_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_url = _parse_redirect_url(d.pop("redirectUrl", UNSET))

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

        _checkout_type = d.pop("checkoutType", UNSET)
        checkout_type: CheckoutType | Unset
        if isinstance(_checkout_type, Unset):
            checkout_type = UNSET
        else:
            checkout_type = CheckoutType(_checkout_type)

        def _parse_form_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_id = _parse_form_id(d.pop("formId", UNSET))

        create_point_of_sale_app_request = cls(
            app_name=app_name,
            title=title,
            description=description,
            template=template,
            default_view=default_view,
            currency=currency,
            show_custom_amount=show_custom_amount,
            show_discount=show_discount,
            enable_tips=enable_tips,
            custom_amount_pay_button_text=custom_amount_pay_button_text,
            fixed_amount_pay_button_text=fixed_amount_pay_button_text,
            tip_text=tip_text,
            custom_css_link=custom_css_link,
            embedded_css=embedded_css,
            notification_url=notification_url,
            redirect_url=redirect_url,
            redirect_automatically=redirect_automatically,
            requires_refund_email=requires_refund_email,
            checkout_type=checkout_type,
            form_id=form_id,
        )

        create_point_of_sale_app_request.additional_properties = d
        return create_point_of_sale_app_request

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
