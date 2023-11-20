# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .human_user_metadata import HumanUserMetadata
from .machine_user_metadata import MachineUserMetadata


class UserMetadata_MachineUserMetadata(MachineUserMetadata):
    type: typing_extensions.Literal["machine_user_metadata"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class UserMetadata_HumanUserMetadata(HumanUserMetadata):
    type: typing_extensions.Literal["human_user_metadata"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


UserMetadata = typing.Union[UserMetadata_MachineUserMetadata, UserMetadata_HumanUserMetadata]
