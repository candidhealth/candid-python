# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
from .eligibility_status import EligibilityStatus
import datetime as dt
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class LatestEligibilityCheck(UniversalBaseModel):
    """
    A type to represent the latest eligibility check status of a coverage.
    """

    check_id: str
    status: EligibilityStatus
    initiated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
