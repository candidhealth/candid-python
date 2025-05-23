# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.schema_id import SchemaId
from .schema_field import SchemaField


class Schema(UniversalBaseModel):
    """
    Examples
    --------
    import uuid

    from candid.resources.commons import Primitive
    from candid.resources.custom_schemas.resources.v_1 import Schema, SchemaField

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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
