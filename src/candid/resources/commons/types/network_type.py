# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NetworkType(str, enum.Enum):
    PPO = "12"
    """
    Preferred Provider Organization (PPO)
    """

    POS = "13"
    """
    Point of Service (POS)
    """

    EPO = "14"
    """
    Exclusive Provider Organization (EPO)
    """

    INDEMNITY_INSURANCE = "15"
    """
    Indemnity Insurance
    """

    HMO_MEDICARE_RISK = "16"
    """
    Health Maintenance Organization (HMO) Medicare Risk
    """

    DMO = "17"
    """
    Dental Maintenance Organization
    """

    AUTO = "AM"
    """
    Automobile Medical
    """

    CHAMPUS = "CH"
    """
    CHAMPUS
    """

    DISABILITY = "DS"
    """
    Disability
    """

    HMO = "HM"
    """
    Health Maintenance Organization (HMO)
    """

    LIABILITY = "LM"
    """
    Liability Medical
    """

    MEDICARE_PART_A = "MA"
    """
    Medicare Part A
    """

    MEDICARE_PART_B = "MB"
    """
    Medicare Part B
    """

    MEDICAID = "MC"
    """
    Medicaid
    """

    OTHER_FEDERAL_PROGRAM = "OF"
    """
    Other Federal Program
    """

    TITLE_V = "TV"
    """
    Title V
    """

    VETERANS_AFFAIRS_PLAN = "VA"
    """
    Veterans Affairs Plan
    """

    WORKERS_COMP_HEALTH_CLAIM = "WC"
    """
    Workers' Compensation Health Claim
    """

    MUTUALLY_DEFINED = "ZZ"
    """
    Mutually Defined
    """

    COMMERCIAL_INSURANCE_CO = "CI"
    """
    Commercial Insurance
    """

    BLUE_CROSS_BLUE_SHIELD = "BL"
    """
    Blue Cross Blue Shield
    """

    _UNKNOWN = "__NETWORKTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "NetworkType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        ppo: typing.Callable[[], T_Result],
        pos: typing.Callable[[], T_Result],
        epo: typing.Callable[[], T_Result],
        indemnity_insurance: typing.Callable[[], T_Result],
        hmo_medicare_risk: typing.Callable[[], T_Result],
        dmo: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        champus: typing.Callable[[], T_Result],
        disability: typing.Callable[[], T_Result],
        hmo: typing.Callable[[], T_Result],
        liability: typing.Callable[[], T_Result],
        medicare_part_a: typing.Callable[[], T_Result],
        medicare_part_b: typing.Callable[[], T_Result],
        medicaid: typing.Callable[[], T_Result],
        other_federal_program: typing.Callable[[], T_Result],
        title_v: typing.Callable[[], T_Result],
        veterans_affairs_plan: typing.Callable[[], T_Result],
        workers_comp_health_claim: typing.Callable[[], T_Result],
        mutually_defined: typing.Callable[[], T_Result],
        commercial_insurance_co: typing.Callable[[], T_Result],
        blue_cross_blue_shield: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is NetworkType.PPO:
            return ppo()
        if self is NetworkType.POS:
            return pos()
        if self is NetworkType.EPO:
            return epo()
        if self is NetworkType.INDEMNITY_INSURANCE:
            return indemnity_insurance()
        if self is NetworkType.HMO_MEDICARE_RISK:
            return hmo_medicare_risk()
        if self is NetworkType.DMO:
            return dmo()
        if self is NetworkType.AUTO:
            return auto()
        if self is NetworkType.CHAMPUS:
            return champus()
        if self is NetworkType.DISABILITY:
            return disability()
        if self is NetworkType.HMO:
            return hmo()
        if self is NetworkType.LIABILITY:
            return liability()
        if self is NetworkType.MEDICARE_PART_A:
            return medicare_part_a()
        if self is NetworkType.MEDICARE_PART_B:
            return medicare_part_b()
        if self is NetworkType.MEDICAID:
            return medicaid()
        if self is NetworkType.OTHER_FEDERAL_PROGRAM:
            return other_federal_program()
        if self is NetworkType.TITLE_V:
            return title_v()
        if self is NetworkType.VETERANS_AFFAIRS_PLAN:
            return veterans_affairs_plan()
        if self is NetworkType.WORKERS_COMP_HEALTH_CLAIM:
            return workers_comp_health_claim()
        if self is NetworkType.MUTUALLY_DEFINED:
            return mutually_defined()
        if self is NetworkType.COMMERCIAL_INSURANCE_CO:
            return commercial_insurance_co()
        if self is NetworkType.BLUE_CROSS_BLUE_SHIELD:
            return blue_cross_blue_shield()
        return _unknown_member(self._value_)
