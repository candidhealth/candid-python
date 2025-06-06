# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ........core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EligibilityCheckErrorDetails(UniversalBaseModel):
    """
    This object is our fern representation of Stedi's EligbilityCheckError object from their API.
    """

    field: typing.Optional[str] = pydantic.Field(alias="field?", default=None)
    description: typing.Optional[str] = pydantic.Field(alias="description?", default=None)
    location: typing.Optional[str] = pydantic.Field(alias="location?", default=None)
    possible_resolutions: typing.Optional[str] = pydantic.Field(alias="possibleResolutions?", default=None)
    code: typing.Optional[str] = pydantic.Field(alias="code?", default=None)
    followup_action: typing.Optional[str] = pydantic.Field(alias="followupAction?", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
