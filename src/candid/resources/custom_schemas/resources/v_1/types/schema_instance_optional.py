# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.schema_id import SchemaId


class SchemaInstanceOptional(UniversalBaseModel):
    """
    Examples
    --------
    import uuid

    from candid.resources.custom_schemas.resources.v_1 import SchemaInstanceOptional

    SchemaInstanceOptional(
        schema_id=uuid.UUID(
            "ec096b13-f80a-471d-aaeb-54b021c9d582",
        ),
        content={
            "provider_category": "internist",
            "is_urgent_care": True,
            "bmi": 24.2,
            "age": 38,
        },
    )
    """

    schema_id: typing.Optional[SchemaId] = pydantic.Field(default=None)
    """
    The schema to which the content must adhere.
    """

    content: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    A set of key-value pairs that adhere to the naming and type convention of the schema. Not all keys in the schema must be included, but attaching any key that does not exist in the schema or attaching a key with the incorrect value type will result in errors.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
