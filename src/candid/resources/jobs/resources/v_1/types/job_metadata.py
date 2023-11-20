# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .claim_job_metadata import ClaimJobMetadata


class JobMetadata_ClaimJobMetadata(ClaimJobMetadata):
    type: typing_extensions.Literal["claim_job_metadata"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


JobMetadata = typing.Union[JobMetadata_ClaimJobMetadata]
