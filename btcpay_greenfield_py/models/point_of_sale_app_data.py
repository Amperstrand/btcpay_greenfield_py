from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.point_of_sale_app_data_default_view import PointOfSaleAppDataDefaultView
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point_of_sale_app_data_items import PointOfSaleAppDataItems


T = TypeVar("T", bound="PointOfSaleAppData")


@_attrs_define
class PointOfSaleAppData:
    """
    Attributes:
        id (str | Unset): Id of the app Example: 3ki4jsAkN4u9rv1PUzj1odX4Nx7s.
        name (str | Unset): Name given to the app when it was created Example: my test app.
        store_id (str | Unset): Id of the store to which the app belongs Example:
            9CiNzKoANXxmk5ayZngSXrHTiVvvgCrwrpFQd4m2K776.
        created (int | Unset): UNIX timestamp for when the app was created Example: 1651554744.
        app_type (str | Unset): Type of the app which was created Example: PointOfSale.
        archived (bool | None | Unset): If true, the app does not appear in the apps list by default. Default: False.
        title (str | Unset): Display title of the app Example: My PoS app.
        description (str | Unset): App description Example: This is my amazing PoS app.
        default_view (PointOfSaleAppDataDefaultView | Unset): App view type (e.g., static, cart, etc...) Example: Cart.
        show_custom_amount (bool | Unset): Whether the option to enter a custom amount is shown Example: True.
        show_discount (bool | Unset): Whether the option to enter a discount is shown
        enable_tips (bool | Unset): Whether the option to enter a tip is shown Example: True.
        currency (str | Unset): Currency used for the app Example: BTC.
        items (PointOfSaleAppDataItems | Unset): JSON object of app items Example: [{'description': "Lovely, fresh and
            tender, Meng Ding Gan Lu ('sweet dew') is grown in the lush Meng Ding Mountains of the southwestern province of
            Sichuan where it has been cultivated for over a thousand years.", 'id': 'green tea', 'image': '~/img/pos-
            sample/green-tea.jpg', 'price': {'type': 2, 'formatted': '$1.00', 'value': 1}, 'title': 'Green Tea',
            'buyButtonText': None, 'inventory': 5, 'paymentMethods': None, 'disabled': False}, {'description': "Tian Jian
            Tian Jian means 'heavenly tippy tea' in Chinese, and it describes the finest grade of dark tea. Our Tian Jian
            dark tea is from Hunan province which is famous for making some of the best dark teas available.", 'id': 'black
            tea', 'image': '~/img/pos-sample/black-tea.jpg', 'price': {'type': 2, 'formatted': '$1.00', 'value': 1},
            'title': 'Black Tea', 'buyButtonText': 'Test Buy Button Text', 'inventory': None, 'paymentMethods': None,
            'disabled': False}].
        fixed_amount_pay_button_text (str | Unset): Payment button text template for items with a set price Example: Buy
            for {0}.
        custom_amount_pay_button_text (str | Unset): Payment button text which appears for items which allow user to
            input a custom amount Example: Pay.
        tip_text (str | Unset): Prompt which appears next to the tip amount field if tipping is enabled Example: Do you
            want to leave a tip?.
        custom_css_link (str | Unset): Link to a custom CSS stylesheet to be used in the app Example:
            https://bootswatch.com/4/slate/bootstrap.min.css.
        notification_url (str | Unset): Callback notification url to POST to once when invoice is paid for and once when
            there are enough blockchain confirmations
        redirect_url (str | Unset): URL user is redirected to once invoice is paid
        embedded_css (str | Unset): Custom CSS embedded into the app
        redirect_automatically (bool | Unset): Whether user is redirected to specified redirect URL automatically after
            the invoice is paid Example: True.
        requires_refund_email (bool | None | Unset): Whether refund email is required when paying the invoice. Defaults
            to `null` if not explicitly set.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    store_id: str | Unset = UNSET
    created: int | Unset = UNSET
    app_type: str | Unset = UNSET
    archived: bool | None | Unset = False
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    default_view: PointOfSaleAppDataDefaultView | Unset = UNSET
    show_custom_amount: bool | Unset = UNSET
    show_discount: bool | Unset = UNSET
    enable_tips: bool | Unset = UNSET
    currency: str | Unset = UNSET
    items: PointOfSaleAppDataItems | Unset = UNSET
    fixed_amount_pay_button_text: str | Unset = UNSET
    custom_amount_pay_button_text: str | Unset = UNSET
    tip_text: str | Unset = UNSET
    custom_css_link: str | Unset = UNSET
    notification_url: str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    embedded_css: str | Unset = UNSET
    redirect_automatically: bool | Unset = UNSET
    requires_refund_email: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        store_id = self.store_id

        created = self.created

        app_type = self.app_type

        archived: bool | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        title = self.title

        description = self.description

        default_view: str | Unset = UNSET
        if not isinstance(self.default_view, Unset):
            default_view = self.default_view.value

        show_custom_amount = self.show_custom_amount

        show_discount = self.show_discount

        enable_tips = self.enable_tips

        currency = self.currency

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        fixed_amount_pay_button_text = self.fixed_amount_pay_button_text

        custom_amount_pay_button_text = self.custom_amount_pay_button_text

        tip_text = self.tip_text

        custom_css_link = self.custom_css_link

        notification_url = self.notification_url

        redirect_url = self.redirect_url

        embedded_css = self.embedded_css

        redirect_automatically = self.redirect_automatically

        requires_refund_email: bool | None | Unset
        if isinstance(self.requires_refund_email, Unset):
            requires_refund_email = UNSET
        else:
            requires_refund_email = self.requires_refund_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if created is not UNSET:
            field_dict["created"] = created
        if app_type is not UNSET:
            field_dict["appType"] = app_type
        if archived is not UNSET:
            field_dict["archived"] = archived
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if default_view is not UNSET:
            field_dict["defaultView"] = default_view
        if show_custom_amount is not UNSET:
            field_dict["showCustomAmount"] = show_custom_amount
        if show_discount is not UNSET:
            field_dict["showDiscount"] = show_discount
        if enable_tips is not UNSET:
            field_dict["enableTips"] = enable_tips
        if currency is not UNSET:
            field_dict["currency"] = currency
        if items is not UNSET:
            field_dict["items"] = items
        if fixed_amount_pay_button_text is not UNSET:
            field_dict["fixedAmountPayButtonText"] = fixed_amount_pay_button_text
        if custom_amount_pay_button_text is not UNSET:
            field_dict["customAmountPayButtonText"] = custom_amount_pay_button_text
        if tip_text is not UNSET:
            field_dict["tipText"] = tip_text
        if custom_css_link is not UNSET:
            field_dict["customCSSLink"] = custom_css_link
        if notification_url is not UNSET:
            field_dict["notificationUrl"] = notification_url
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if embedded_css is not UNSET:
            field_dict["embeddedCSS"] = embedded_css
        if redirect_automatically is not UNSET:
            field_dict["redirectAutomatically"] = redirect_automatically
        if requires_refund_email is not UNSET:
            field_dict["requiresRefundEmail"] = requires_refund_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point_of_sale_app_data_items import PointOfSaleAppDataItems

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        store_id = d.pop("storeId", UNSET)

        created = d.pop("created", UNSET)

        app_type = d.pop("appType", UNSET)

        def _parse_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _default_view = d.pop("defaultView", UNSET)
        default_view: PointOfSaleAppDataDefaultView | Unset
        if isinstance(_default_view, Unset):
            default_view = UNSET
        else:
            default_view = PointOfSaleAppDataDefaultView(_default_view)

        show_custom_amount = d.pop("showCustomAmount", UNSET)

        show_discount = d.pop("showDiscount", UNSET)

        enable_tips = d.pop("enableTips", UNSET)

        currency = d.pop("currency", UNSET)

        _items = d.pop("items", UNSET)
        items: PointOfSaleAppDataItems | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = PointOfSaleAppDataItems.from_dict(_items)

        fixed_amount_pay_button_text = d.pop("fixedAmountPayButtonText", UNSET)

        custom_amount_pay_button_text = d.pop("customAmountPayButtonText", UNSET)

        tip_text = d.pop("tipText", UNSET)

        custom_css_link = d.pop("customCSSLink", UNSET)

        notification_url = d.pop("notificationUrl", UNSET)

        redirect_url = d.pop("redirectUrl", UNSET)

        embedded_css = d.pop("embeddedCSS", UNSET)

        redirect_automatically = d.pop("redirectAutomatically", UNSET)

        def _parse_requires_refund_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        requires_refund_email = _parse_requires_refund_email(d.pop("requiresRefundEmail", UNSET))

        point_of_sale_app_data = cls(
            id=id,
            name=name,
            store_id=store_id,
            created=created,
            app_type=app_type,
            archived=archived,
            title=title,
            description=description,
            default_view=default_view,
            show_custom_amount=show_custom_amount,
            show_discount=show_discount,
            enable_tips=enable_tips,
            currency=currency,
            items=items,
            fixed_amount_pay_button_text=fixed_amount_pay_button_text,
            custom_amount_pay_button_text=custom_amount_pay_button_text,
            tip_text=tip_text,
            custom_css_link=custom_css_link,
            notification_url=notification_url,
            redirect_url=redirect_url,
            embedded_css=embedded_css,
            redirect_automatically=redirect_automatically,
            requires_refund_email=requires_refund_email,
        )

        point_of_sale_app_data.additional_properties = d
        return point_of_sale_app_data

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
