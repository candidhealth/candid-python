# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .successful_generate_clinical_notes_pdf_response import SuccessfulGenerateClinicalNotesPdfResponse


class GenerateClinicalNotesPdfResponse_Success(SuccessfulGenerateClinicalNotesPdfResponse):
    result: typing_extensions.Literal["success"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


GenerateClinicalNotesPdfResponse = typing.Union[GenerateClinicalNotesPdfResponse_Success]
