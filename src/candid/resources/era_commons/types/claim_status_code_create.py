# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClaimStatusCodeCreate(str, enum.Enum):
    """
    See https://www.stedi.com/edi/x12/element/1029
    """

    PROCESSED_AS_PRIMARY = "1"
    PROCESSED_AS_SECONDARY = "2"
    PROCESSED_AS_TERTIARY = "3"
    DENIED = "4"
    PROCESSED_AS_PRIMARY_FORWARDED = "19"
    PROCESSED_AS_SECONDARY_FORWARDED = "20"
    PROCESSED_AS_TERTIARY_FORWARDED = "21"
    REVERSAL_OF_PREVIOUS_PAYMENT = "22"
    NOT_OUR_CLAIM_FORWARDED = "23"
    _UNKNOWN = "__CLAIMSTATUSCODECREATE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ClaimStatusCodeCreate":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        processed_as_primary: typing.Callable[[], T_Result],
        processed_as_secondary: typing.Callable[[], T_Result],
        processed_as_tertiary: typing.Callable[[], T_Result],
        denied: typing.Callable[[], T_Result],
        processed_as_primary_forwarded: typing.Callable[[], T_Result],
        processed_as_secondary_forwarded: typing.Callable[[], T_Result],
        processed_as_tertiary_forwarded: typing.Callable[[], T_Result],
        reversal_of_previous_payment: typing.Callable[[], T_Result],
        not_our_claim_forwarded: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ClaimStatusCodeCreate.PROCESSED_AS_PRIMARY:
            return processed_as_primary()
        if self is ClaimStatusCodeCreate.PROCESSED_AS_SECONDARY:
            return processed_as_secondary()
        if self is ClaimStatusCodeCreate.PROCESSED_AS_TERTIARY:
            return processed_as_tertiary()
        if self is ClaimStatusCodeCreate.DENIED:
            return denied()
        if self is ClaimStatusCodeCreate.PROCESSED_AS_PRIMARY_FORWARDED:
            return processed_as_primary_forwarded()
        if self is ClaimStatusCodeCreate.PROCESSED_AS_SECONDARY_FORWARDED:
            return processed_as_secondary_forwarded()
        if self is ClaimStatusCodeCreate.PROCESSED_AS_TERTIARY_FORWARDED:
            return processed_as_tertiary_forwarded()
        if self is ClaimStatusCodeCreate.REVERSAL_OF_PREVIOUS_PAYMENT:
            return reversal_of_previous_payment()
        if self is ClaimStatusCodeCreate.NOT_OUR_CLAIM_FORWARDED:
            return not_our_claim_forwarded()
        return _unknown_member(self._value_)
