# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DiagnosisTypeCode(str, enum.Enum):
    ABF = "ABF"
    """
    ICD-10 Diagnosis
    """

    ABJ = "ABJ"
    """
    ICD-10 Admitting Diagnosis
    """

    ABK = "ABK"
    """
    ICD-10 Principal Diagnosis
    """

    APR = "APR"
    """
    ICD-10 Patient Reason for Visit
    """

    BF = "BF"
    """
    ICD-9 Diagnosis
    """

    BJ = "BJ"
    """
    ICD-9 Admitting Diagnosis
    """

    BK = "BK"
    """
    ICD-9 Principal Diagnosis
    """

    PR = "PR"
    """
    ICD-9 Patient Reason for Visit
    """

    DR = "DR"
    """
    Diagnosis Related Group (DRG)
    """

    LOI = "LOI"
    """
    Logical Observation Identifier Names and Codes (LOINC<190>) Codes
    """

    _UNKNOWN = "__DIAGNOSISTYPECODE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "DiagnosisTypeCode":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        abf: typing.Callable[[], T_Result],
        abj: typing.Callable[[], T_Result],
        abk: typing.Callable[[], T_Result],
        apr: typing.Callable[[], T_Result],
        bf: typing.Callable[[], T_Result],
        bj: typing.Callable[[], T_Result],
        bk: typing.Callable[[], T_Result],
        pr: typing.Callable[[], T_Result],
        dr: typing.Callable[[], T_Result],
        loi: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is DiagnosisTypeCode.ABF:
            return abf()
        if self is DiagnosisTypeCode.ABJ:
            return abj()
        if self is DiagnosisTypeCode.ABK:
            return abk()
        if self is DiagnosisTypeCode.APR:
            return apr()
        if self is DiagnosisTypeCode.BF:
            return bf()
        if self is DiagnosisTypeCode.BJ:
            return bj()
        if self is DiagnosisTypeCode.BK:
            return bk()
        if self is DiagnosisTypeCode.PR:
            return pr()
        if self is DiagnosisTypeCode.DR:
            return dr()
        if self is DiagnosisTypeCode.LOI:
            return loi()
        return _unknown_member(self._value_)
