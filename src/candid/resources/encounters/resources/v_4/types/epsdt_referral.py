# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .....commons.types.epsdt_referral_condition_indicator_code import EpsdtReferralConditionIndicatorCode
import pydantic
import typing
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class EpsdtReferral(UniversalBaseModel):
    condition_indicator_1: EpsdtReferralConditionIndicatorCode = pydantic.Field(alias="condition_indicator1")
    condition_indicator_2: typing.Optional[EpsdtReferralConditionIndicatorCode] = pydantic.Field(
        alias="condition_indicator2", default=None
    )
    condition_indicator_3: typing.Optional[EpsdtReferralConditionIndicatorCode] = pydantic.Field(
        alias="condition_indicator3", default=None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
