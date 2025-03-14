# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountType(str, enum.Enum):
    PATIENT = "PATIENT"
    INSURANCE = "INSURANCE"
    THIRD_PARTY_PAYER = "THIRD_PARTY_PAYER"
    _UNKNOWN = "__ACCOUNTTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "AccountType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        patient: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        third_party_payer: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is AccountType.PATIENT:
            return patient()
        if self is AccountType.INSURANCE:
            return insurance()
        if self is AccountType.THIRD_PARTY_PAYER:
            return third_party_payer()
        return _unknown_member(self._value_)
