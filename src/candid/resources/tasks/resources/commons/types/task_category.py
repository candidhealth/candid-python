# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskCategory(str, enum.Enum):
    OTHER = "other"
    PROVIDER_CREDENTIALING = "provider_credentialing"
    AUTHORIZATION_REQUIRED = "authorization_required"
    INACTIVE_COVERAGE = "inactive_coverage"
    UNKNOWN_ELIGIBILITY_OR_PATIENT_NOT_FOUND = "unknown_eligibility_or_patient_not_found"
    INCORRECT_MEMBER_ID = "incorrect_member_id"
    DOCUMENTATION_ADDENDUM_REQUEST = "documentation_addendum_request"
    COORDINATION_OF_BENEFITS = "coordination_of_benefits"
    MISSING_OR_INCORRECT_GENDER = "missing_or_incorrect_gender"
    INCORRECT_DATE_OF_BIRTH = "incorrect_date_of_birth"
    INCORRECT_PAYER = "incorrect_payer"
    INCORRECT_NAME = "incorrect_name"
    INVALID_DIAGNOSIS_CODE = "invalid_diagnosis_code"
    NON_COVERED_DIAGNOSIS_CODES = "non_covered_diagnosis_codes"
    INFORMATION_REQUESTED_FROM_PATIENT = "information_requested_from_patient"
    INCORRECT_RENDERING_PROVIDER_INFO = "incorrect_rendering_provider_info"
    MISSING_OR_INCORRECT_MODIFIER = "missing_or_incorrect_modifier"
    CODING_FREQUENCY_ERROR = "coding_frequency_error"
    INCORRECT_PATIENT_ADDRESS = "incorrect_patient_address"
    MULTIPLE_EM_CLAIMS = "multiple_em_claims"
    MISSING_OR_INCORRECT_CHARGE_AMOUNT = "missing_or_incorrect_charge_amount"
    MEDICAL_RECORDS_REQUEST = "medical_records_request"
    PROVIDER_ENROLLMENT_OR_CONTRACTING = "provider_enrollment_or_contracting"
    MISSING_OR_INCORRECT_GROUP_NUMBER = "missing_or_incorrect_group_number"
    MISSING_DIAGNOSIS_CODES = "missing_diagnosis_codes"
    MISSING_PATIENT_AUTHORIZATION = "missing_patient_authorization"
    INCORRECT_BILLING_PROVIDER_INFO = "incorrect_billing_provider_info"
    INCORRECT_PROCEDURE_CODE = "incorrect_procedure_code"
    INCORRECT_QUANTITY = "incorrect_quantity"
    INCORRECT_PLACE_OF_SERVICE_CODE = "incorrect_place_of_service_code"
    INCORRECT_SERVICE_FACILITY_INFO = "incorrect_service_facility_info"
    INCORRECT_DATE_OF_SERVICE = "incorrect_date_of_service"
    MISSING_OR_INCORRECT_NDC = "missing_or_incorrect_ndc"
    PATIENT_COLLECTIONS = "patient_collections"
    SUBMIT_TO_SECONDARY = "submit_to_secondary"
    TRANSIENT_SERVER_ERROR = "transient_server_error"
    MISSING_REMITTANCE_ENROLLMENT = "missing_remittance_enrollment"
    MISSING_CLAIMS_ENROLLMENT = "missing_claims_enrollment"
    HELD_BY_CUSTOMER = "held_by_customer"
    PENDING_MANUAL_REMIT_POSTING = "pending_manual_remit_posting"
    INCORRECT_REFERRING_PROVIDER_INFO = "incorrect_referring_provider_info"
    PAYER_CONFIGURATION_ERROR = "payer_configuration_error"
    _UNKNOWN = "__TASKCATEGORY_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "TaskCategory":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        other: typing.Callable[[], T_Result],
        provider_credentialing: typing.Callable[[], T_Result],
        authorization_required: typing.Callable[[], T_Result],
        inactive_coverage: typing.Callable[[], T_Result],
        unknown_eligibility_or_patient_not_found: typing.Callable[[], T_Result],
        incorrect_member_id: typing.Callable[[], T_Result],
        documentation_addendum_request: typing.Callable[[], T_Result],
        coordination_of_benefits: typing.Callable[[], T_Result],
        missing_or_incorrect_gender: typing.Callable[[], T_Result],
        incorrect_date_of_birth: typing.Callable[[], T_Result],
        incorrect_payer: typing.Callable[[], T_Result],
        incorrect_name: typing.Callable[[], T_Result],
        invalid_diagnosis_code: typing.Callable[[], T_Result],
        non_covered_diagnosis_codes: typing.Callable[[], T_Result],
        information_requested_from_patient: typing.Callable[[], T_Result],
        incorrect_rendering_provider_info: typing.Callable[[], T_Result],
        missing_or_incorrect_modifier: typing.Callable[[], T_Result],
        coding_frequency_error: typing.Callable[[], T_Result],
        incorrect_patient_address: typing.Callable[[], T_Result],
        multiple_em_claims: typing.Callable[[], T_Result],
        missing_or_incorrect_charge_amount: typing.Callable[[], T_Result],
        medical_records_request: typing.Callable[[], T_Result],
        provider_enrollment_or_contracting: typing.Callable[[], T_Result],
        missing_or_incorrect_group_number: typing.Callable[[], T_Result],
        missing_diagnosis_codes: typing.Callable[[], T_Result],
        missing_patient_authorization: typing.Callable[[], T_Result],
        incorrect_billing_provider_info: typing.Callable[[], T_Result],
        incorrect_procedure_code: typing.Callable[[], T_Result],
        incorrect_quantity: typing.Callable[[], T_Result],
        incorrect_place_of_service_code: typing.Callable[[], T_Result],
        incorrect_service_facility_info: typing.Callable[[], T_Result],
        incorrect_date_of_service: typing.Callable[[], T_Result],
        missing_or_incorrect_ndc: typing.Callable[[], T_Result],
        patient_collections: typing.Callable[[], T_Result],
        submit_to_secondary: typing.Callable[[], T_Result],
        transient_server_error: typing.Callable[[], T_Result],
        missing_remittance_enrollment: typing.Callable[[], T_Result],
        missing_claims_enrollment: typing.Callable[[], T_Result],
        held_by_customer: typing.Callable[[], T_Result],
        pending_manual_remit_posting: typing.Callable[[], T_Result],
        incorrect_referring_provider_info: typing.Callable[[], T_Result],
        payer_configuration_error: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is TaskCategory.OTHER:
            return other()
        if self is TaskCategory.PROVIDER_CREDENTIALING:
            return provider_credentialing()
        if self is TaskCategory.AUTHORIZATION_REQUIRED:
            return authorization_required()
        if self is TaskCategory.INACTIVE_COVERAGE:
            return inactive_coverage()
        if self is TaskCategory.UNKNOWN_ELIGIBILITY_OR_PATIENT_NOT_FOUND:
            return unknown_eligibility_or_patient_not_found()
        if self is TaskCategory.INCORRECT_MEMBER_ID:
            return incorrect_member_id()
        if self is TaskCategory.DOCUMENTATION_ADDENDUM_REQUEST:
            return documentation_addendum_request()
        if self is TaskCategory.COORDINATION_OF_BENEFITS:
            return coordination_of_benefits()
        if self is TaskCategory.MISSING_OR_INCORRECT_GENDER:
            return missing_or_incorrect_gender()
        if self is TaskCategory.INCORRECT_DATE_OF_BIRTH:
            return incorrect_date_of_birth()
        if self is TaskCategory.INCORRECT_PAYER:
            return incorrect_payer()
        if self is TaskCategory.INCORRECT_NAME:
            return incorrect_name()
        if self is TaskCategory.INVALID_DIAGNOSIS_CODE:
            return invalid_diagnosis_code()
        if self is TaskCategory.NON_COVERED_DIAGNOSIS_CODES:
            return non_covered_diagnosis_codes()
        if self is TaskCategory.INFORMATION_REQUESTED_FROM_PATIENT:
            return information_requested_from_patient()
        if self is TaskCategory.INCORRECT_RENDERING_PROVIDER_INFO:
            return incorrect_rendering_provider_info()
        if self is TaskCategory.MISSING_OR_INCORRECT_MODIFIER:
            return missing_or_incorrect_modifier()
        if self is TaskCategory.CODING_FREQUENCY_ERROR:
            return coding_frequency_error()
        if self is TaskCategory.INCORRECT_PATIENT_ADDRESS:
            return incorrect_patient_address()
        if self is TaskCategory.MULTIPLE_EM_CLAIMS:
            return multiple_em_claims()
        if self is TaskCategory.MISSING_OR_INCORRECT_CHARGE_AMOUNT:
            return missing_or_incorrect_charge_amount()
        if self is TaskCategory.MEDICAL_RECORDS_REQUEST:
            return medical_records_request()
        if self is TaskCategory.PROVIDER_ENROLLMENT_OR_CONTRACTING:
            return provider_enrollment_or_contracting()
        if self is TaskCategory.MISSING_OR_INCORRECT_GROUP_NUMBER:
            return missing_or_incorrect_group_number()
        if self is TaskCategory.MISSING_DIAGNOSIS_CODES:
            return missing_diagnosis_codes()
        if self is TaskCategory.MISSING_PATIENT_AUTHORIZATION:
            return missing_patient_authorization()
        if self is TaskCategory.INCORRECT_BILLING_PROVIDER_INFO:
            return incorrect_billing_provider_info()
        if self is TaskCategory.INCORRECT_PROCEDURE_CODE:
            return incorrect_procedure_code()
        if self is TaskCategory.INCORRECT_QUANTITY:
            return incorrect_quantity()
        if self is TaskCategory.INCORRECT_PLACE_OF_SERVICE_CODE:
            return incorrect_place_of_service_code()
        if self is TaskCategory.INCORRECT_SERVICE_FACILITY_INFO:
            return incorrect_service_facility_info()
        if self is TaskCategory.INCORRECT_DATE_OF_SERVICE:
            return incorrect_date_of_service()
        if self is TaskCategory.MISSING_OR_INCORRECT_NDC:
            return missing_or_incorrect_ndc()
        if self is TaskCategory.PATIENT_COLLECTIONS:
            return patient_collections()
        if self is TaskCategory.SUBMIT_TO_SECONDARY:
            return submit_to_secondary()
        if self is TaskCategory.TRANSIENT_SERVER_ERROR:
            return transient_server_error()
        if self is TaskCategory.MISSING_REMITTANCE_ENROLLMENT:
            return missing_remittance_enrollment()
        if self is TaskCategory.MISSING_CLAIMS_ENROLLMENT:
            return missing_claims_enrollment()
        if self is TaskCategory.HELD_BY_CUSTOMER:
            return held_by_customer()
        if self is TaskCategory.PENDING_MANUAL_REMIT_POSTING:
            return pending_manual_remit_posting()
        if self is TaskCategory.INCORRECT_REFERRING_PROVIDER_INFO:
            return incorrect_referring_provider_info()
        if self is TaskCategory.PAYER_CONFIGURATION_ERROR:
            return payer_configuration_error()
        return _unknown_member(self._value_)
