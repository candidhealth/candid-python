# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitCode(str, enum.Enum):
    MILLILITERS = "ML"
    UNITS = "UN"
    GRAMS = "GR"
    INTERNATIONAL_UNIT = "F2"
    MILLIGRAM = "ME"
    _UNKNOWN = "__MEASUREMENTUNITCODE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "MeasurementUnitCode":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        milliliters: typing.Callable[[], T_Result],
        units: typing.Callable[[], T_Result],
        grams: typing.Callable[[], T_Result],
        international_unit: typing.Callable[[], T_Result],
        milligram: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitCode.MILLILITERS:
            return milliliters()
        if self is MeasurementUnitCode.UNITS:
            return units()
        if self is MeasurementUnitCode.GRAMS:
            return grams()
        if self is MeasurementUnitCode.INTERNATIONAL_UNIT:
            return international_unit()
        if self is MeasurementUnitCode.MILLIGRAM:
            return milligram()
        return _unknown_member(self._value_)
