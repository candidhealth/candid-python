# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .payer_uuid import PayerUuid


class Payer(pydantic.BaseModel):
    payer_uuid: PayerUuid = pydantic.Field(description="Auto-generated ID set on creation")
    payer_id: str = pydantic.Field(description="The primary national payer ID of the payer")
    payer_name: str = pydantic.Field(description="The primary display name of the payer")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}