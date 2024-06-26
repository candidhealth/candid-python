# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IntendedSubmissionMedium(str, enum.Enum):
    """
    The medium (paper or electronic) via which we intended to submit the claim. The clearinghouse to which we sent the claim may use a different medium in certain cases, e.g., if the payer does not support electronic claims.
    """

    PAPER = "paper"
    ELECTRONIC = "electronic"

    def visit(self, paper: typing.Callable[[], T_Result], electronic: typing.Callable[[], T_Result]) -> T_Result:
        if self is IntendedSubmissionMedium.PAPER:
            return paper()
        if self is IntendedSubmissionMedium.ELECTRONIC:
            return electronic()
