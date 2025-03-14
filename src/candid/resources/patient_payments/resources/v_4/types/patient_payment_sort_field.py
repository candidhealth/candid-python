# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatientPaymentSortField(str, enum.Enum):
    PAYMENT_SOURCE = "payment_source"
    AMOUNT_CENTS = "amount_cents"
    PAYMENT_TIMESTAMP = "payment_timestamp"
    PAYMENT_NOTE = "payment_note"
    _UNKNOWN = "__PATIENTPAYMENTSORTFIELD_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "PatientPaymentSortField":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        payment_source: typing.Callable[[], T_Result],
        amount_cents: typing.Callable[[], T_Result],
        payment_timestamp: typing.Callable[[], T_Result],
        payment_note: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is PatientPaymentSortField.PAYMENT_SOURCE:
            return payment_source()
        if self is PatientPaymentSortField.AMOUNT_CENTS:
            return amount_cents()
        if self is PatientPaymentSortField.PAYMENT_TIMESTAMP:
            return payment_timestamp()
        if self is PatientPaymentSortField.PAYMENT_NOTE:
            return payment_note()
        return _unknown_member(self._value_)
