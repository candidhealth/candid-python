# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .plan_date import PlanDate
from .expanded_member_info import ExpandedMemberInfo
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PlanMetadata(UniversalBaseModel):
    payer_name: typing.Optional[str] = None
    insurance_type: typing.Optional[str] = None
    insurance_type_code: typing.Optional[str] = None
    plan_name: typing.Optional[str] = None
    member_id: typing.Optional[str] = None
    group_number: typing.Optional[str] = None
    start_date: typing.Optional[dt.date] = None
    end_date: typing.Optional[dt.date] = None
    plan_dates: typing.Optional[typing.List[PlanDate]] = None
    subscriber: typing.Optional[ExpandedMemberInfo] = None
    dependent: typing.Optional[ExpandedMemberInfo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
