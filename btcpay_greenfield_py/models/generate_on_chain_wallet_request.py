from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.generate_on_chain_wallet_request_script_pub_key_type import GenerateOnChainWalletRequestScriptPubKeyType
from ..models.generate_on_chain_wallet_request_word_count import GenerateOnChainWalletRequestWordCount
from ..models.generate_on_chain_wallet_request_word_list import GenerateOnChainWalletRequestWordList
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateOnChainWalletRequest")


@_attrs_define
class GenerateOnChainWalletRequest:
    """
    Attributes:
        existing_mnemonic (str | Unset): An existing BIP39 mnemonic seed to generate the wallet with
        passphrase (str | Unset): A passphrase for the BIP39 mnemonic seed
        account_number (float | Unset): The account to derive from the BIP39 mnemonic seed Default: 0.0.
        save_private_keys (bool | Unset): Whether to store the seed inside BTCPay Server to enable some additional
            services. IF `false` AND `existingMnemonic` IS NOT SPECIFIED, BE SURE TO SECURELY STORE THE SEED IN THE
            RESPONSE! Default: False.
        import_keys_to_rpc (bool | Unset): Whether to import all addresses generated via BTCPay Server into the
            underlying node wallet. (Private keys will also be imported if `savePrivateKeys` is set to true. Default: False.
        word_list (GenerateOnChainWalletRequestWordList | Unset): If `existingMnemonic` is not set, a mnemonic is
            generated using the specified wordList. Default: GenerateOnChainWalletRequestWordList.ENGLISH.
        word_count (GenerateOnChainWalletRequestWordCount | Unset): If `existingMnemonic` is not set, a mnemonic is
            generated using the specified wordCount. Default: GenerateOnChainWalletRequestWordCount.VALUE_12.
        script_pub_key_type (GenerateOnChainWalletRequestScriptPubKeyType | Unset): the type of wallet to generate
            Default: GenerateOnChainWalletRequestScriptPubKeyType.SEGWIT.
    """

    existing_mnemonic: str | Unset = UNSET
    passphrase: str | Unset = UNSET
    account_number: float | Unset = 0.0
    save_private_keys: bool | Unset = False
    import_keys_to_rpc: bool | Unset = False
    word_list: GenerateOnChainWalletRequestWordList | Unset = GenerateOnChainWalletRequestWordList.ENGLISH
    word_count: GenerateOnChainWalletRequestWordCount | Unset = GenerateOnChainWalletRequestWordCount.VALUE_12
    script_pub_key_type: GenerateOnChainWalletRequestScriptPubKeyType | Unset = (
        GenerateOnChainWalletRequestScriptPubKeyType.SEGWIT
    )

    def to_dict(self) -> dict[str, Any]:
        existing_mnemonic = self.existing_mnemonic

        passphrase = self.passphrase

        account_number = self.account_number

        save_private_keys = self.save_private_keys

        import_keys_to_rpc = self.import_keys_to_rpc

        word_list: str | Unset = UNSET
        if not isinstance(self.word_list, Unset):
            word_list = self.word_list.value

        word_count: int | Unset = UNSET
        if not isinstance(self.word_count, Unset):
            word_count = self.word_count.value

        script_pub_key_type: str | Unset = UNSET
        if not isinstance(self.script_pub_key_type, Unset):
            script_pub_key_type = self.script_pub_key_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if existing_mnemonic is not UNSET:
            field_dict["existingMnemonic"] = existing_mnemonic
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if save_private_keys is not UNSET:
            field_dict["savePrivateKeys"] = save_private_keys
        if import_keys_to_rpc is not UNSET:
            field_dict["importKeysToRPC"] = import_keys_to_rpc
        if word_list is not UNSET:
            field_dict["wordList"] = word_list
        if word_count is not UNSET:
            field_dict["wordCount"] = word_count
        if script_pub_key_type is not UNSET:
            field_dict["scriptPubKeyType"] = script_pub_key_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        existing_mnemonic = d.pop("existingMnemonic", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        save_private_keys = d.pop("savePrivateKeys", UNSET)

        import_keys_to_rpc = d.pop("importKeysToRPC", UNSET)

        _word_list = d.pop("wordList", UNSET)
        word_list: GenerateOnChainWalletRequestWordList | Unset
        if isinstance(_word_list, Unset):
            word_list = UNSET
        else:
            word_list = GenerateOnChainWalletRequestWordList(_word_list)

        _word_count = d.pop("wordCount", UNSET)
        word_count: GenerateOnChainWalletRequestWordCount | Unset
        if isinstance(_word_count, Unset):
            word_count = UNSET
        else:
            word_count = GenerateOnChainWalletRequestWordCount(_word_count)

        _script_pub_key_type = d.pop("scriptPubKeyType", UNSET)
        script_pub_key_type: GenerateOnChainWalletRequestScriptPubKeyType | Unset
        if isinstance(_script_pub_key_type, Unset):
            script_pub_key_type = UNSET
        else:
            script_pub_key_type = GenerateOnChainWalletRequestScriptPubKeyType(_script_pub_key_type)

        generate_on_chain_wallet_request = cls(
            existing_mnemonic=existing_mnemonic,
            passphrase=passphrase,
            account_number=account_number,
            save_private_keys=save_private_keys,
            import_keys_to_rpc=import_keys_to_rpc,
            word_list=word_list,
            word_count=word_count,
            script_pub_key_type=script_pub_key_type,
        )

        return generate_on_chain_wallet_request
