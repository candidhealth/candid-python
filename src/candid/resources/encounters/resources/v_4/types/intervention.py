# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .intervention_category import InterventionCategory
import typing
import pydantic
from .medication import Medication
from .lab import Lab
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class Intervention(UniversalBaseModel):
    """
    Examples
    --------
    from candid.resources.encounters.resources.v_4 import (
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
