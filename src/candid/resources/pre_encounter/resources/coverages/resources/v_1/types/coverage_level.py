# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CoverageLevel(str, enum.Enum):
    EMPLOYEE_AND_CHILDREN = "EMPLOYEE_AND_CHILDREN"
    EMPLOYEE_ONLY = "EMPLOYEE_ONLY"
    EMPLOYEE_AND_SPOUSE = "EMPLOYEE_AND_SPOUSE"
    FAMILY = "FAMILY"
    INDIVIDUAL = "INDIVIDUAL"
    _UNKNOWN = "__COVERAGELEVEL_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "CoverageLevel":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        employee_and_children: typing.Callable[[], T_Result],
        employee_only: typing.Callable[[], T_Result],
        employee_and_spouse: typing.Callable[[], T_Result],
        family: typing.Callable[[], T_Result],
        individual: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is CoverageLevel.EMPLOYEE_AND_CHILDREN:
            return employee_and_children()
        if self is CoverageLevel.EMPLOYEE_ONLY:
            return employee_only()
        if self is CoverageLevel.EMPLOYEE_AND_SPOUSE:
            return employee_and_spouse()
        if self is CoverageLevel.FAMILY:
            return family()
        if self is CoverageLevel.INDIVIDUAL:
            return individual()
        return _unknown_member(self._value_)
