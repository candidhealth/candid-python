# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ......core.pydantic_utilities import UniversalBaseModel
from .....commons.types.insurance_type_code import InsuranceTypeCode
import typing
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class InsuranceTypeCodes_InsuranceTypeCode(UniversalBaseModel):
    value: InsuranceTypeCode
    type: typing.Literal["insurance_type_code"] = "insurance_type_code"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


class InsuranceTypeCodes_UnknownInsuranceTypeCode(UniversalBaseModel):
    type: typing.Literal["unknown_insurance_type_code"] = "unknown_insurance_type_code"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InsuranceTypeCodes_NotApplicable(UniversalBaseModel):
    type: typing.Literal["not_applicable"] = "not_applicable"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InsuranceTypeCodes = typing.Union[
    InsuranceTypeCodes_InsuranceTypeCode, InsuranceTypeCodes_UnknownInsuranceTypeCode, InsuranceTypeCodes_NotApplicable
]
