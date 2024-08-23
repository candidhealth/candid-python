# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime
from ........core.pydantic_utilities import deep_union_pydantic_dicts
from .....common.types.organization_id import OrganizationId
from .....common.types.user_id import UserId
from .mutable_patient import MutablePatient
from .patient_id import PatientId


class Patient(MutablePatient):
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

    organization_id: OrganizationId = pydantic.Field()
    """
    The organization that owns this patient.
    """

    deactivated: bool = pydantic.Field()
    """
    True if the patient is deactivated. Deactivated patients are not returned in search results but are returned in all other endpoints including scan.
    """

    version: int = pydantic.Field()
    """
    The version of the patient. Any update to any property of a patient object will create a new version.
    """

    updated_at: dt.datetime
    updating_user_id: UserId = pydantic.Field()
    """
    The user ID of the user who last updated the patient.
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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
