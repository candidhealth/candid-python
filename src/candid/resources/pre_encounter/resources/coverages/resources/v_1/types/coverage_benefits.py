# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
import typing
from .plan_coverage import PlanCoverage
from .service_coverage import ServiceCoverage
from .benefits_related_entity import BenefitsRelatedEntity
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CoverageBenefits(UniversalBaseModel):
    plan_coverage: typing.Optional[PlanCoverage] = None
    service_specific_coverage: typing.Optional[typing.List[ServiceCoverage]] = None
    benefits_related_entities: typing.Optional[typing.List[BenefitsRelatedEntity]] = None
    notes: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
