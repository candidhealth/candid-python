# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Sex(str, enum.Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    UNKNOWN = "UNKNOWN"
    REFUSED = "REFUSED"

    def visit(
        self,
        female: typing.Callable[[], T_Result],
        male: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        refused: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Sex.FEMALE:
            return female()
        if self is Sex.MALE:
            return male()
        if self is Sex.UNKNOWN:
            return unknown()
        if self is Sex.REFUSED:
            return refused()