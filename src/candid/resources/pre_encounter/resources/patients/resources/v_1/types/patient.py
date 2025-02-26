# This file was auto-generated by Fern from our API Definition.

from .....common.types.base_model import BaseModel
from .mutable_patient import MutablePatient
from .....common.types.patient_id import PatientId
import pydantic
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Patient(BaseModel, MutablePatient):
    """
    A patient object with immutable server-owned properties.
    """

    id: PatientId = pydantic.Field()
    """
    The unique UUID identifier for a Patient. Patient ID is used in machine contexts.
    """

    mrn: str = pydantic.Field()
    """
    The medical record number for the patient. Human-friendly Candid generated MRNs are of the form "YYMMDDXXXX", where "YYYYMMDD" is the date of patient creation and "XXXX" is a zero-padded incrementing integer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
