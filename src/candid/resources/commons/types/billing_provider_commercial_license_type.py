# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BillingProviderCommercialLicenseType(str, enum.Enum):
    LICENSED_CLINICAL_SOCIAL_WORKER = "0"
    LICENSED_PROFESSIONAL_COUNSELOR = "A"
    LICENSED_MARRIAGE_AND_FAMILY_COUNSELOR = "B"
    LICENSED_CLINICAL_ALCOHOL_AND_DRUG_COUNSELOR = "C"
    PSYCHOLOGIST = "D"
    PSYCHIATRIC_NURSE = "E"
    PSYCHIATRIST = "F"
    CHILD_ADOLESCENT_PSYCHIATRIST = "G"
    PHYSICIAN_ASSISTANT = "H"
    NURSE_CNP = "I"

    def visit(
        self,
        licensed_clinical_social_worker: typing.Callable[[], T_Result],
        licensed_professional_counselor: typing.Callable[[], T_Result],
        licensed_marriage_and_family_counselor: typing.Callable[[], T_Result],
        licensed_clinical_alcohol_and_drug_counselor: typing.Callable[[], T_Result],
        psychologist: typing.Callable[[], T_Result],
        psychiatric_nurse: typing.Callable[[], T_Result],
        psychiatrist: typing.Callable[[], T_Result],
        child_adolescent_psychiatrist: typing.Callable[[], T_Result],
        physician_assistant: typing.Callable[[], T_Result],
        nurse_cnp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BillingProviderCommercialLicenseType.LICENSED_CLINICAL_SOCIAL_WORKER:
            return licensed_clinical_social_worker()
        if self is BillingProviderCommercialLicenseType.LICENSED_PROFESSIONAL_COUNSELOR:
            return licensed_professional_counselor()
        if self is BillingProviderCommercialLicenseType.LICENSED_MARRIAGE_AND_FAMILY_COUNSELOR:
            return licensed_marriage_and_family_counselor()
        if self is BillingProviderCommercialLicenseType.LICENSED_CLINICAL_ALCOHOL_AND_DRUG_COUNSELOR:
            return licensed_clinical_alcohol_and_drug_counselor()
        if self is BillingProviderCommercialLicenseType.PSYCHOLOGIST:
            return psychologist()
        if self is BillingProviderCommercialLicenseType.PSYCHIATRIC_NURSE:
            return psychiatric_nurse()
        if self is BillingProviderCommercialLicenseType.PSYCHIATRIST:
            return psychiatrist()
        if self is BillingProviderCommercialLicenseType.CHILD_ADOLESCENT_PSYCHIATRIST:
            return child_adolescent_psychiatrist()
        if self is BillingProviderCommercialLicenseType.PHYSICIAN_ASSISTANT:
            return physician_assistant()
        if self is BillingProviderCommercialLicenseType.NURSE_CNP:
            return nurse_cnp()
