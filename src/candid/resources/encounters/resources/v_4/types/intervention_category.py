# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterventionCategory(str, enum.Enum):
    ALLOPATHIC = "allopathic"
    NATUROPATHIC = "naturopathic"
    TESTS = "tests"
    LIFESTYLE = "lifestyle"
    _UNKNOWN = "__INTERVENTIONCATEGORY_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "InterventionCategory":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        allopathic: typing.Callable[[], T_Result],
        naturopathic: typing.Callable[[], T_Result],
        tests: typing.Callable[[], T_Result],
        lifestyle: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is InterventionCategory.ALLOPATHIC:
            return allopathic()
        if self is InterventionCategory.NATUROPATHIC:
            return naturopathic()
        if self is InterventionCategory.TESTS:
            return tests()
        if self is InterventionCategory.LIFESTYLE:
            return lifestyle()
        return _unknown_member(self._value_)
