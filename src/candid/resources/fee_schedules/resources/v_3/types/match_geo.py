# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
from .....commons.types.state import State
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MatchGeo(UniversalBaseModel):
    """
    Match information for state or zip code
    """

    zip_code: typing.Optional[str] = None
    state: typing.Optional[State] = None
    match: bool
    explanation: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
