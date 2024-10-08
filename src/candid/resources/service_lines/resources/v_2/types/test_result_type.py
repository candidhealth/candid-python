# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TestResultType(str, enum.Enum):
    HEMATOCRIT = "HEMATOCRIT"
    HEMOGLOBIN = "HEMOGLOBIN"

    def visit(self, hematocrit: typing.Callable[[], T_Result], hemoglobin: typing.Callable[[], T_Result]) -> T_Result:
        if self is TestResultType.HEMATOCRIT:
            return hematocrit()
        if self is TestResultType.HEMOGLOBIN:
            return hemoglobin()
