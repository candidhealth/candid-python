# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AddressType(str, enum.Enum):
    DEFAULT = "DEFAULT"
    _UNKNOWN = "__ADDRESSTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "AddressType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self, default: typing.Callable[[], T_Result], _unknown_member: typing.Callable[[str], T_Result]
    ) -> T_Result:
        if self is AddressType.DEFAULT:
            return default()
        return _unknown_member(self._value_)
