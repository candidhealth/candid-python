# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
from .....commons.types.facility_type_code import FacilityTypeCode
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MatchFacilityTypeCode(UniversalBaseModel):
    """
    Match information for facility type code
    """

    value: typing.Optional[FacilityTypeCode] = None
    match: bool
    explanation: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
