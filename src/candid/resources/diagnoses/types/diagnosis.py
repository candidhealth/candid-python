# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .diagnosis_id import DiagnosisId
from .standalone_diagnosis_create import StandaloneDiagnosisCreate


class Diagnosis(StandaloneDiagnosisCreate):
    """
    Examples
    --------
    import datetime
    import uuid

    from candid.resources.diagnoses import Diagnosis, DiagnosisTypeCode

    Diagnosis(
        diagnosis_id=uuid.UUID(
            "5c770e00-4bbf-42af-a73f-99c5e91fc0db",
        ),
        created_at=datetime.datetime.fromisoformat(
            "2023-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2023-01-01 00:00:00+00:00",
        ),
        encounter_id=uuid.UUID(
            "3f63985b-51a4-4dd4-9418-7d50b2520792",
        ),
        name="John Doe",
        code_type=DiagnosisTypeCode.ABF,
        code="I10",
    )
    """

    diagnosis_id: DiagnosisId
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
