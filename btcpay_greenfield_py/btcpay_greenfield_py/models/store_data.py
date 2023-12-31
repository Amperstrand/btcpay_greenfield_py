# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from btcpay_greenfield_py.models.checkout_type import CheckoutType
from btcpay_greenfield_py.models.invoice_data_base_receipt import InvoiceDataBaseReceipt
from btcpay_greenfield_py.models.network_fee_mode import NetworkFeeMode
from btcpay_greenfield_py.models.object import object
from btcpay_greenfield_py.models.payment_method_criteria_data import PaymentMethodCriteriaData
from btcpay_greenfield_py.models.speed_policy import SpeedPolicy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StoreData(BaseModel):
    """
    StoreData
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the store")
    website: Optional[StrictStr] = Field(default=None, description="The absolute url of the store")
    support_url: Optional[StrictStr] = Field(default=None, description="The support URI of the store, can contain the placeholders `{OrderId}` and `{InvoiceId}`. Can be any valid URI, such as a website, email, and nostr.", alias="supportUrl")
    default_currency: Optional[StrictStr] = Field(default='USD', description="The default currency of the store", alias="defaultCurrency")
    invoice_expiration: Optional[object] = Field(default=None, alias="invoiceExpiration")
    display_expiration_timer: Optional[object] = Field(default=None, alias="displayExpirationTimer")
    monitoring_expiration: Optional[object] = Field(default=None, alias="monitoringExpiration")
    speed_policy: Optional[SpeedPolicy] = Field(default=None, alias="speedPolicy")
    lightning_description_template: Optional[StrictStr] = Field(default=None, description="The BOLT11 description of the lightning invoice in the checkout. You can use placeholders '{StoreName}', '{ItemDescription}' and '{OrderId}'.", alias="lightningDescriptionTemplate")
    payment_tolerance: Optional[Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=0, description="Consider an invoice fully paid, even if the payment is missing 'x' % of the full amount.", alias="paymentTolerance")
    archived: Optional[StrictBool] = Field(default=False, description="If true, the store does not appear in the stores list by default.")
    anyone_can_create_invoice: Optional[StrictBool] = Field(default=False, description="If true, then no authentication is needed to create invoices on this store.", alias="anyoneCanCreateInvoice")
    requires_refund_email: Optional[StrictBool] = Field(default=False, description="If true, the checkout page will ask to enter an email address before accessing payment information.", alias="requiresRefundEmail")
    checkout_type: Optional[CheckoutType] = Field(default=None, alias="checkoutType")
    receipt: Optional[InvoiceDataBaseReceipt] = None
    lightning_amount_in_satoshi: Optional[StrictBool] = Field(default=False, description="If true, lightning payment methods show amount in satoshi in the checkout page.", alias="lightningAmountInSatoshi")
    lightning_private_route_hints: Optional[StrictBool] = Field(default=False, description="Should private route hints be included in the lightning payment of the checkout page.", alias="lightningPrivateRouteHints")
    on_chain_with_ln_invoice_fallback: Optional[StrictBool] = Field(default=False, description="Unify on-chain and lightning payment URL.", alias="onChainWithLnInvoiceFallback")
    redirect_automatically: Optional[StrictBool] = Field(default=False, description="After successfull payment, should the checkout page redirect the user automatically to the redirect URL of the invoice?", alias="redirectAutomatically")
    show_recommended_fee: Optional[StrictBool] = Field(default=True, alias="showRecommendedFee")
    recommended_fee_block_target: Optional[StrictInt] = Field(default=1, description="The fee rate recommendation in the checkout page for the on-chain payment to be confirmed after 'x' blocks.", alias="recommendedFeeBlockTarget")
    default_lang: Optional[StrictStr] = Field(default='en', description="The default language to use in the checkout page. (The different translations available are listed [here](https://github.com/btcpayserver/btcpayserver/tree/master/BTCPayServer/wwwroot/locales)", alias="defaultLang")
    custom_logo: Optional[StrictStr] = Field(default=None, description="URL to a logo to include in the checkout page.", alias="customLogo")
    custom_css: Optional[StrictStr] = Field(default=None, description="URL to a CSS stylesheet to include in the checkout page", alias="customCSS")
    html_title: Optional[StrictStr] = Field(default=None, description="The HTML title of the checkout page (when you over the tab in your browser)", alias="htmlTitle")
    network_fee_mode: Optional[NetworkFeeMode] = Field(default=None, alias="networkFeeMode")
    pay_join_enabled: Optional[StrictBool] = Field(default=False, description="If true, payjoin will be proposed in the checkout page if possible. ([More information](https://docs.btcpayserver.org/Payjoin/))", alias="payJoinEnabled")
    auto_detect_language: Optional[StrictBool] = Field(default=False, description="If true, the language on the checkout page will adapt to the language defined by the user's browser settings", alias="autoDetectLanguage")
    show_pay_in_wallet_button: Optional[StrictBool] = Field(default=True, description="If true, the \"Pay in wallet\" button will be shown on the checkout page (Checkout V2)", alias="showPayInWalletButton")
    show_store_header: Optional[StrictBool] = Field(default=True, description="If true, the store header will be shown on the checkout page (Checkout V2)", alias="showStoreHeader")
    celebrate_payment: Optional[StrictBool] = Field(default=True, description="If true, payments on the checkout page will be celebrated with confetti (Checkout V2)", alias="celebratePayment")
    play_sound_on_payment: Optional[StrictBool] = Field(default=False, description="If true, sounds on the checkout page will be enabled (Checkout V2)", alias="playSoundOnPayment")
    lazy_payment_methods: Optional[StrictBool] = Field(default=False, description="If true, payment methods are enabled individually upon user interaction in the invoice", alias="lazyPaymentMethods")
    default_payment_method: Optional[StrictStr] = Field(default=None, description="Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - `\"BTC-OnChain\"` (with the equivalent of `\"BTC\"`)    -`\"BTC-LightningLike\"`: Any supported LN-based payment method (Lightning or LNURL)    - `\"BTC-LightningNetwork\"`: Lightning    - `\"BTC-LNURLPAY\"`: LNURL        Note: Separator can be either `-` or `_`.", alias="defaultPaymentMethod")
    payment_method_criteria: Optional[List[PaymentMethodCriteriaData]] = Field(default=None, description="The criteria required to activate specific payment methods.", alias="paymentMethodCriteria")
    id: Optional[StrictStr] = Field(default=None, description="The id of the store")
    __properties: ClassVar[List[str]] = ["name", "website", "supportUrl", "defaultCurrency", "invoiceExpiration", "displayExpirationTimer", "monitoringExpiration", "speedPolicy", "lightningDescriptionTemplate", "paymentTolerance", "archived", "anyoneCanCreateInvoice", "requiresRefundEmail", "checkoutType", "receipt", "lightningAmountInSatoshi", "lightningPrivateRouteHints", "onChainWithLnInvoiceFallback", "redirectAutomatically", "showRecommendedFee", "recommendedFeeBlockTarget", "defaultLang", "customLogo", "customCSS", "htmlTitle", "networkFeeMode", "payJoinEnabled", "autoDetectLanguage", "showPayInWalletButton", "showStoreHeader", "celebratePayment", "playSoundOnPayment", "lazyPaymentMethods", "defaultPaymentMethod", "paymentMethodCriteria", "id"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StoreData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of receipt
        if self.receipt:
            _dict['receipt'] = self.receipt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payment_method_criteria (list)
        _items = []
        if self.payment_method_criteria:
            for _item in self.payment_method_criteria:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paymentMethodCriteria'] = _items
        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if support_url (nullable) is None
        # and model_fields_set contains the field
        if self.support_url is None and "support_url" in self.model_fields_set:
            _dict['supportUrl'] = None

        # set to None if lightning_description_template (nullable) is None
        # and model_fields_set contains the field
        if self.lightning_description_template is None and "lightning_description_template" in self.model_fields_set:
            _dict['lightningDescriptionTemplate'] = None

        # set to None if checkout_type (nullable) is None
        # and model_fields_set contains the field
        if self.checkout_type is None and "checkout_type" in self.model_fields_set:
            _dict['checkoutType'] = None

        # set to None if receipt (nullable) is None
        # and model_fields_set contains the field
        if self.receipt is None and "receipt" in self.model_fields_set:
            _dict['receipt'] = None

        # set to None if custom_logo (nullable) is None
        # and model_fields_set contains the field
        if self.custom_logo is None and "custom_logo" in self.model_fields_set:
            _dict['customLogo'] = None

        # set to None if custom_css (nullable) is None
        # and model_fields_set contains the field
        if self.custom_css is None and "custom_css" in self.model_fields_set:
            _dict['customCSS'] = None

        # set to None if html_title (nullable) is None
        # and model_fields_set contains the field
        if self.html_title is None and "html_title" in self.model_fields_set:
            _dict['htmlTitle'] = None

        # set to None if payment_method_criteria (nullable) is None
        # and model_fields_set contains the field
        if self.payment_method_criteria is None and "payment_method_criteria" in self.model_fields_set:
            _dict['paymentMethodCriteria'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of StoreData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "website": obj.get("website"),
            "supportUrl": obj.get("supportUrl"),
            "defaultCurrency": obj.get("defaultCurrency") if obj.get("defaultCurrency") is not None else 'USD',
            "invoiceExpiration": obj.get("invoiceExpiration"),
            "displayExpirationTimer": obj.get("displayExpirationTimer"),
            "monitoringExpiration": obj.get("monitoringExpiration"),
            "speedPolicy": obj.get("speedPolicy"),
            "lightningDescriptionTemplate": obj.get("lightningDescriptionTemplate"),
            "paymentTolerance": obj.get("paymentTolerance") if obj.get("paymentTolerance") is not None else 0,
            "archived": obj.get("archived") if obj.get("archived") is not None else False,
            "anyoneCanCreateInvoice": obj.get("anyoneCanCreateInvoice") if obj.get("anyoneCanCreateInvoice") is not None else False,
            "requiresRefundEmail": obj.get("requiresRefundEmail") if obj.get("requiresRefundEmail") is not None else False,
            "checkoutType": obj.get("checkoutType"),
            "receipt": InvoiceDataBaseReceipt.from_dict(obj.get("receipt")) if obj.get("receipt") is not None else None,
            "lightningAmountInSatoshi": obj.get("lightningAmountInSatoshi") if obj.get("lightningAmountInSatoshi") is not None else False,
            "lightningPrivateRouteHints": obj.get("lightningPrivateRouteHints") if obj.get("lightningPrivateRouteHints") is not None else False,
            "onChainWithLnInvoiceFallback": obj.get("onChainWithLnInvoiceFallback") if obj.get("onChainWithLnInvoiceFallback") is not None else False,
            "redirectAutomatically": obj.get("redirectAutomatically") if obj.get("redirectAutomatically") is not None else False,
            "showRecommendedFee": obj.get("showRecommendedFee") if obj.get("showRecommendedFee") is not None else True,
            "recommendedFeeBlockTarget": obj.get("recommendedFeeBlockTarget") if obj.get("recommendedFeeBlockTarget") is not None else 1,
            "defaultLang": obj.get("defaultLang") if obj.get("defaultLang") is not None else 'en',
            "customLogo": obj.get("customLogo"),
            "customCSS": obj.get("customCSS"),
            "htmlTitle": obj.get("htmlTitle"),
            "networkFeeMode": obj.get("networkFeeMode"),
            "payJoinEnabled": obj.get("payJoinEnabled") if obj.get("payJoinEnabled") is not None else False,
            "autoDetectLanguage": obj.get("autoDetectLanguage") if obj.get("autoDetectLanguage") is not None else False,
            "showPayInWalletButton": obj.get("showPayInWalletButton") if obj.get("showPayInWalletButton") is not None else True,
            "showStoreHeader": obj.get("showStoreHeader") if obj.get("showStoreHeader") is not None else True,
            "celebratePayment": obj.get("celebratePayment") if obj.get("celebratePayment") is not None else True,
            "playSoundOnPayment": obj.get("playSoundOnPayment") if obj.get("playSoundOnPayment") is not None else False,
            "lazyPaymentMethods": obj.get("lazyPaymentMethods") if obj.get("lazyPaymentMethods") is not None else False,
            "defaultPaymentMethod": obj.get("defaultPaymentMethod"),
            "paymentMethodCriteria": [PaymentMethodCriteriaData.from_dict(_item) for _item in obj.get("paymentMethodCriteria")] if obj.get("paymentMethodCriteria") is not None else None,
            "id": obj.get("id")
        })
        return _obj


