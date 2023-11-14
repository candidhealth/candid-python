# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskSortOptions(str, enum.Enum):
    UPDATED_AT_ASC = "updated_at:asc"
    UPDATED_AT_DESC = "updated_at:desc"
    PATIENT_NAME_ASC = "patient_name:asc"
    PATIENT_NAME_DESC = "patient_name:desc"
    PATIENT_EXTERNAL_ID_ASC = "patient_external_id:asc"
    PATIENT_EXTERNAL_ID_DESC = "patient_external_id:desc"
    PAYER_NAME_ASC = "payer_name:asc"
    PAYER_NAME_DESC = "payer_name:desc"
    PAYER_ID_ASC = "payer_id:asc"
    PAYER_ID_DESC = "payer_id:desc"
    STATUS_ASC = "status:asc"
    STATUS_DESC = "status:desc"
    TASK_TYPE_ASC = "task_type:asc"
    TASK_TYPE_DESC = "task_type:desc"
    CATEGORY_ASC = "category:asc"
    CATEGORY_DESC = "category:desc"
    AGG_UPDATED_AT_ASC = "agg_updated_at:asc"
    AGG_UPDATED_AT_DESC = "agg_updated_at:desc"
    DATE_OF_SERVICE_ASC = "date_of_service:asc"
    DATE_OF_SERVICE_DESC = "date_of_service:desc"
    BLOCKS_CLAIM_SUBMISSION_ASC = "blocks_claim_submission:asc"
    BLOCKS_CLAIM_SUBMISSION_DESC = "blocks_claim_submission:desc"

    def visit(
        self,
        updated_at_asc: typing.Callable[[], T_Result],
        updated_at_desc: typing.Callable[[], T_Result],
        patient_name_asc: typing.Callable[[], T_Result],
        patient_name_desc: typing.Callable[[], T_Result],
        patient_external_id_asc: typing.Callable[[], T_Result],
        patient_external_id_desc: typing.Callable[[], T_Result],
        payer_name_asc: typing.Callable[[], T_Result],
        payer_name_desc: typing.Callable[[], T_Result],
        payer_id_asc: typing.Callable[[], T_Result],
        payer_id_desc: typing.Callable[[], T_Result],
        status_asc: typing.Callable[[], T_Result],
        status_desc: typing.Callable[[], T_Result],
        task_type_asc: typing.Callable[[], T_Result],
        task_type_desc: typing.Callable[[], T_Result],
        category_asc: typing.Callable[[], T_Result],
        category_desc: typing.Callable[[], T_Result],
        agg_updated_at_asc: typing.Callable[[], T_Result],
        agg_updated_at_desc: typing.Callable[[], T_Result],
        date_of_service_asc: typing.Callable[[], T_Result],
        date_of_service_desc: typing.Callable[[], T_Result],
        blocks_claim_submission_asc: typing.Callable[[], T_Result],
        blocks_claim_submission_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskSortOptions.UPDATED_AT_ASC:
            return updated_at_asc()
        if self is TaskSortOptions.UPDATED_AT_DESC:
            return updated_at_desc()
        if self is TaskSortOptions.PATIENT_NAME_ASC:
            return patient_name_asc()
        if self is TaskSortOptions.PATIENT_NAME_DESC:
            return patient_name_desc()
        if self is TaskSortOptions.PATIENT_EXTERNAL_ID_ASC:
            return patient_external_id_asc()
        if self is TaskSortOptions.PATIENT_EXTERNAL_ID_DESC:
            return patient_external_id_desc()
        if self is TaskSortOptions.PAYER_NAME_ASC:
            return payer_name_asc()
        if self is TaskSortOptions.PAYER_NAME_DESC:
            return payer_name_desc()
        if self is TaskSortOptions.PAYER_ID_ASC:
            return payer_id_asc()
        if self is TaskSortOptions.PAYER_ID_DESC:
            return payer_id_desc()
        if self is TaskSortOptions.STATUS_ASC:
            return status_asc()
        if self is TaskSortOptions.STATUS_DESC:
            return status_desc()
        if self is TaskSortOptions.TASK_TYPE_ASC:
            return task_type_asc()
        if self is TaskSortOptions.TASK_TYPE_DESC:
            return task_type_desc()
        if self is TaskSortOptions.CATEGORY_ASC:
            return category_asc()
        if self is TaskSortOptions.CATEGORY_DESC:
            return category_desc()
        if self is TaskSortOptions.AGG_UPDATED_AT_ASC:
            return agg_updated_at_asc()
        if self is TaskSortOptions.AGG_UPDATED_AT_DESC:
            return agg_updated_at_desc()
        if self is TaskSortOptions.DATE_OF_SERVICE_ASC:
            return date_of_service_asc()
        if self is TaskSortOptions.DATE_OF_SERVICE_DESC:
            return date_of_service_desc()
        if self is TaskSortOptions.BLOCKS_CLAIM_SUBMISSION_ASC:
            return blocks_claim_submission_asc()
        if self is TaskSortOptions.BLOCKS_CLAIM_SUBMISSION_DESC:
            return blocks_claim_submission_desc()
