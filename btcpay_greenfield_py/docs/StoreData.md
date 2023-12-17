# StoreData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the store | [optional] 
**website** | **str** | The absolute url of the store | [optional] 
**support_url** | **str** | The support URI of the store, can contain the placeholders &#x60;{OrderId}&#x60; and &#x60;{InvoiceId}&#x60;. Can be any valid URI, such as a website, email, and nostr. | [optional] 
**default_currency** | **str** | The default currency of the store | [optional] [default to 'USD']
**invoice_expiration** | **object** |  | [optional] 
**display_expiration_timer** | **object** |  | [optional] 
**monitoring_expiration** | **object** |  | [optional] 
**speed_policy** | [**SpeedPolicy**](SpeedPolicy.md) |  | [optional] 
**lightning_description_template** | **str** | The BOLT11 description of the lightning invoice in the checkout. You can use placeholders &#39;{StoreName}&#39;, &#39;{ItemDescription}&#39; and &#39;{OrderId}&#39;. | [optional] 
**payment_tolerance** | **float** | Consider an invoice fully paid, even if the payment is missing &#39;x&#39; % of the full amount. | [optional] [default to 0]
**archived** | **bool** | If true, the store does not appear in the stores list by default. | [optional] [default to False]
**anyone_can_create_invoice** | **bool** | If true, then no authentication is needed to create invoices on this store. | [optional] [default to False]
**requires_refund_email** | **bool** | If true, the checkout page will ask to enter an email address before accessing payment information. | [optional] [default to False]
**checkout_type** | [**CheckoutType**](CheckoutType.md) |  | [optional] 
**receipt** | [**InvoiceDataBaseReceipt**](InvoiceDataBaseReceipt.md) |  | [optional] 
**lightning_amount_in_satoshi** | **bool** | If true, lightning payment methods show amount in satoshi in the checkout page. | [optional] [default to False]
**lightning_private_route_hints** | **bool** | Should private route hints be included in the lightning payment of the checkout page. | [optional] [default to False]
**on_chain_with_ln_invoice_fallback** | **bool** | Unify on-chain and lightning payment URL. | [optional] [default to False]
**redirect_automatically** | **bool** | After successfull payment, should the checkout page redirect the user automatically to the redirect URL of the invoice? | [optional] [default to False]
**show_recommended_fee** | **bool** |  | [optional] [default to True]
**recommended_fee_block_target** | **int** | The fee rate recommendation in the checkout page for the on-chain payment to be confirmed after &#39;x&#39; blocks. | [optional] [default to 1]
**default_lang** | **str** | The default language to use in the checkout page. (The different translations available are listed [here](https://github.com/btcpayserver/btcpayserver/tree/master/BTCPayServer/wwwroot/locales) | [optional] [default to 'en']
**custom_logo** | **str** | URL to a logo to include in the checkout page. | [optional] 
**custom_css** | **str** | URL to a CSS stylesheet to include in the checkout page | [optional] 
**html_title** | **str** | The HTML title of the checkout page (when you over the tab in your browser) | [optional] 
**network_fee_mode** | [**NetworkFeeMode**](NetworkFeeMode.md) |  | [optional] 
**pay_join_enabled** | **bool** | If true, payjoin will be proposed in the checkout page if possible. ([More information](https://docs.btcpayserver.org/Payjoin/)) | [optional] [default to False]
**auto_detect_language** | **bool** | If true, the language on the checkout page will adapt to the language defined by the user&#39;s browser settings | [optional] [default to False]
**show_pay_in_wallet_button** | **bool** | If true, the \&quot;Pay in wallet\&quot; button will be shown on the checkout page (Checkout V2) | [optional] [default to True]
**show_store_header** | **bool** | If true, the store header will be shown on the checkout page (Checkout V2) | [optional] [default to True]
**celebrate_payment** | **bool** | If true, payments on the checkout page will be celebrated with confetti (Checkout V2) | [optional] [default to True]
**play_sound_on_payment** | **bool** | If true, sounds on the checkout page will be enabled (Checkout V2) | [optional] [default to False]
**lazy_payment_methods** | **bool** | If true, payment methods are enabled individually upon user interaction in the invoice | [optional] [default to False]
**default_payment_method** | **str** | Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - &#x60;\&quot;BTC-OnChain\&quot;&#x60; (with the equivalent of &#x60;\&quot;BTC\&quot;&#x60;)    -&#x60;\&quot;BTC-LightningLike\&quot;&#x60;: Any supported LN-based payment method (Lightning or LNURL)    - &#x60;\&quot;BTC-LightningNetwork\&quot;&#x60;: Lightning    - &#x60;\&quot;BTC-LNURLPAY\&quot;&#x60;: LNURL        Note: Separator can be either &#x60;-&#x60; or &#x60;_&#x60;. | [optional] 
**payment_method_criteria** | [**List[PaymentMethodCriteriaData]**](PaymentMethodCriteriaData.md) | The criteria required to activate specific payment methods. | [optional] 
**id** | **str** | The id of the store | [optional] 

## Example

```python
from openapi_client.models.store_data import StoreData

# TODO update the JSON string below
json = "{}"
# create an instance of StoreData from a JSON string
store_data_instance = StoreData.from_json(json)
# print the JSON string representation of the object
print StoreData.to_json()

# convert the object into a dict
store_data_dict = store_data_instance.to_dict()
# create an instance of StoreData from a dict
store_data_form_dict = store_data.from_dict(store_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


