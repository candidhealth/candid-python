# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
from .eligibility_check_metadata import EligibilityCheckMetadata
import typing
from .eligibility_check import EligibilityCheck
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CoverageEligibilityCheckResponse(UniversalBaseModel):
    metadata: EligibilityCheckMetadata
    check: typing.Optional[EligibilityCheck] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
