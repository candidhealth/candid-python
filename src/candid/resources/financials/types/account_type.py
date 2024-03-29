# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountType(str, enum.Enum):
    PATIENT = "PATIENT"
    INSURANCE = "INSURANCE"

    def visit(self, patient: typing.Callable[[], T_Result], insurance: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccountType.PATIENT:
            return patient()
        if self is AccountType.INSURANCE:
            return insurance()
