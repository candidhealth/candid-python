# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
import typing
from .eligibility_status import EligibilityStatus
from .plan_metadata import PlanMetadata
from .coverage_benefits import CoverageBenefits
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EligibilityCheck(UniversalBaseModel):
    raw_json: typing.Optional[typing.Any] = None
    errors: typing.Optional[typing.Optional[typing.Any]] = None
    eligibility_status: EligibilityStatus
    plan_metadata: typing.Optional[PlanMetadata] = None
    benefits: typing.Optional[CoverageBenefits] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
