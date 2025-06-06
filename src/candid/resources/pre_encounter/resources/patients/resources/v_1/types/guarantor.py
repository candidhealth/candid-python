# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ........core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....common.types.address import Address
from .....common.types.contact_point import ContactPoint
from .....common.types.human_name import HumanName


class Guarantor(UniversalBaseModel):
    name: HumanName
    telecom: typing.Optional[ContactPoint] = None
    email: typing.Optional[str] = None
    birth_date: dt.date
    address: Address

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
