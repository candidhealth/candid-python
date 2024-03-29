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

    def visit(
        self,
        manual_entry: typing.Callable[[], T_Result],
        chargebee: typing.Callable[[], T_Result],
        square: typing.Callable[[], T_Result],
        stripe: typing.Callable[[], T_Result],
        elation: typing.Callable[[], T_Result],
        cedar: typing.Callable[[], T_Result],
        healthie: typing.Callable[[], T_Result],
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
