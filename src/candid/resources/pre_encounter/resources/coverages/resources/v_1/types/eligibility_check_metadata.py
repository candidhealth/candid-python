# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
from .service_type_code import ServiceTypeCode
from .eligibility_check_status import EligibilityCheckStatus
from .....common.types.user_id import UserId
import datetime as dt
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class EligibilityCheckMetadata(UniversalBaseModel):
    check_id: str
    service_code: ServiceTypeCode
    status: EligibilityCheckStatus
    initiated_by: UserId
    initiated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
