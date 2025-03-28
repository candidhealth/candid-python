# This file was auto-generated by Fern from our API Definition.

from .....common.types.base_model import BaseModel
from .mutable_appointment import MutableAppointment
from .....common.types.appointment_id import AppointmentId
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class Appointment(BaseModel, MutableAppointment):
    """
    An appointment object with immutable server-owned properties.
    """

    id: AppointmentId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
