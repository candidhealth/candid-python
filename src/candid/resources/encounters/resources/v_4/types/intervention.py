# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .intervention_category import InterventionCategory
from .lab import Lab
from .medication import Medication


class Intervention(pydantic.BaseModel):
    """
    Examples
    --------
    from candid.resources.encounters.v_4 import (
        Intervention,
        InterventionCategory,
        Lab,
        LabCodeType,
        Medication,
    )

    Intervention(
        name="Physical Therapy Session",
        category=InterventionCategory.LIFESTYLE,
        description="A session focused on improving muscular strength, flexibility, and range of motion post-injury.",
        medication=Medication(
            name="Lisinopril",
            rx_cui="860975",
            dosage="10mg",
            dosage_form="Tablet",
            frequency="Once Daily",
            as_needed=True,
        ),
        labs=[
            Lab(
                name="Genetic Health Labs",
                code="GH12345",
                code_type=LabCodeType.QUEST,
            )
        ],
    )
    """

    name: str
    category: InterventionCategory
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    "Examples: 'Birth Control LAC', 'Tracking', 'Stress Management', 'Supplement', 'Labs'"
    """

    medication: typing.Optional[Medication] = pydantic.Field(default=None)
    """
    Required when `type` is `allopathic`.
    """

    labs: typing.Optional[typing.List[Lab]] = pydantic.Field(default=None)
    """
    Required when `type` is `tests`.
    """

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
