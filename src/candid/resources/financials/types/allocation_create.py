# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .allocation_target_create import AllocationTargetCreate


class AllocationCreate(UniversalBaseModel):
    """
    Allocations are portions of payments that are applied to specific resources, known as targets. Each allocation has
    and amount, defined in cents, and a target.
    """

    amount_cents: int
    target: AllocationTargetCreate

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
