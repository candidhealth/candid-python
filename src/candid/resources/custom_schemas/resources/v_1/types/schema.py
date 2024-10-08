# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.schema_id import SchemaId
from .schema_field import SchemaField


class Schema(pydantic.BaseModel):
    """
    Examples
    --------
    import uuid

    from candid import Primitive
    from candid.resources.custom_schemas.v_1 import Schema, SchemaField

    Schema(
        id=uuid.UUID(
            "ec096b13-f80a-471d-aaeb-54b021c9d582",
        ),
        name="General Medicine",
        description="Values associated with a generic visit",
        fields=[
            SchemaField(
                key="provider_category",
                type=Primitive.STRING,
            ),
            SchemaField(
                key="is_urgent_care",
                type=Primitive.BOOLEAN,
            ),
            SchemaField(
                key="bmi",
                type=Primitive.DOUBLE,
            ),
            SchemaField(
                key="age",
                type=Primitive.INTEGER,
            ),
        ],
    )
    """

    id: SchemaId
    name: str
    description: typing.Optional[str] = None
    fields: typing.List[SchemaField]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
