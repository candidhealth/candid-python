# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatientTransactionSource(str, enum.Enum):
    MANUAL_ENTRY = "MANUAL_ENTRY"
    CHARGEBEE = "CHARGEBEE"
    SQUARE = "SQUARE"
    STRIPE = "STRIPE"
    ELATION = "ELATION"
    CEDAR = "CEDAR"
    HEALTHIE = "HEALTHIE"
    _UNKNOWN = "__PATIENTTRANSACTIONSOURCE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "PatientTransactionSource":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        manual_entry: typing.Callable[[], T_Result],
        chargebee: typing.Callable[[], T_Result],
        square: typing.Callable[[], T_Result],
        stripe: typing.Callable[[], T_Result],
        elation: typing.Callable[[], T_Result],
        cedar: typing.Callable[[], T_Result],
        healthie: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is PatientTransactionSource.MANUAL_ENTRY:
            return manual_entry()
        if self is PatientTransactionSource.CHARGEBEE:
            return chargebee()
        if self is PatientTransactionSource.SQUARE:
            return square()
        if self is PatientTransactionSource.STRIPE:
            return stripe()
        if self is PatientTransactionSource.ELATION:
            return elation()
        if self is PatientTransactionSource.CEDAR:
            return cedar()
        if self is PatientTransactionSource.HEALTHIE:
            return healthie()
        return _unknown_member(self._value_)
