# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.claim_id import ClaimId
from ...era.types.era import Era
from ...service_lines.resources.v_2.types.service_line import ServiceLine
from .claim_status import ClaimStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Claim(pydantic.BaseModel):
    """
    import datetime
    import uuid

    from candid import (Claim, ClaimStatus, DateRangeOptionalEnd, Era,
                        FacilityTypeCode, Invoice, InvoiceItem, InvoiceStatus,
                        ProcedureModifier, ServiceLineUnits)
    from candid.resources.service_lines.v_2 import (DenialReasonContent,
                                                    ServiceLine,
                                                    ServiceLineAdjustment,
                                                    ServiceLineDenialReason,
                                                    ServiceLineEraData)

    Claim(claim_id=uuid.UUID("dd9d7f82-37b5-449d-aa63-26925398335b", ), status=ClaimStatus.BILLER_RECEIVED, clearinghouse="Change Healthcare", clearinghouse_claim_id="5BA7C3AB-2BC2-496C-8B10-6CAC73D0729D", payer_claim_id="9BB9F259-9756-4F16-8F53-9DBB9F7EB1BB", service_lines=[ServiceLine(modifiers=[ProcedureModifier.22], charge_amount_cents=10000, allowed_amount_cents=8000, insurance_balance_cents=0, patient_balance_cents=2000, paid_amount_cents=8000, patient_responsibility_cents=2000, diagnosis_id_zero=uuid.UUID("4ac84bcd-12f5-4f86-a57b-e06749127c98", ), diagnosis_id_one=uuid.UUID("eea5ca5a-8b43-45fd-8cbd-c6cc1103e759", ), diagnosis_id_two=uuid.UUID("5c4aa029-2db9-4202-916e-e93c708f65ff", ), diagnosis_id_three=uuid.UUID("81795126-a3ac-443c-b47e-7259a16ab4a2", ), service_line_era_data=ServiceLineEraData(service_line_adjustments=[ServiceLineAdjustment(created_at=datetime.datetime.fromisoformat("2023-01-01 00:00:00+00:00", ), adjustment_group_code="CO", adjustment_reason_code="CO", adjustment_amount_cents=1000, adjustment_note="test_note", )], remittance_advice_remark_codes=["N362"], ), service_line_manual_adjustments=[ServiceLineAdjustment(created_at=datetime.datetime.fromisoformat("2023-01-01 00:00:00+00:00", ), adjustment_group_code="CO", adjustment_reason_code="CO", adjustment_amount_cents=1000, adjustment_note="test_note", )], related_invoices=[Invoice(id=uuid.UUID("901be2f1-41bc-456e-9987-4fe2f84f9d75", ), created_at=datetime.datetime.fromisoformat("2023-01-01 00:00:00+00:00", ), updated_at=datetime.datetime.fromisoformat("2023-01-01 00:00:00+00:00", ), organzation_id=uuid.UUID("f13f73d4-4344-46ea-9d93-33bcffbb9f36", ), source_id="9B626577-8808-4F28-9ED1-F0DFF0D49BBC", source_customer_id="624D1972-8C69-4C2F-AEFA-10856F734DB3", patient_external_id="10FED4D6-4C5A-48DF-838A-EEF45A74788D", note="test_note", due_date="2023-10-10", status=InvoiceStatus.DRAFT, url="https://example.com", customer_invoice_url="https://example.com", items=[InvoiceItem(service_line_id=uuid.UUID("ced00f23-6e68-4678-9dbc-f5aa2969a565", ), amount_cents=500, )], )], denial_reason=ServiceLineDenialReason(reason=DenialReasonContent.AUTHORIZATION_REQUIRED, ), place_of_service_code=FacilityTypeCode.01, service_line_id=uuid.UUID("ced00f23-6e68-4678-9dbc-f5aa2969a565", ), procedure_code="99213", quantity="1", units=ServiceLineUnits.MJ, claim_id=uuid.UUID("026a1fb8-748e-4859-a2d7-3ea9e07d25ae", ), date_of_service_range=DateRangeOptionalEnd(start_date="2023-01-01", end_date="2023-01-03", ), date_of_service=datetime.date.fromisoformat("2023-01-01", ), end_date_of_service=datetime.date.fromisoformat("2023-01-03", ), )], eras=[Era(era_id=uuid.UUID("4d844ef1-2253-43cd-a4f1-6db7e65cb54b", ), check_number="CHK12345", check_date="2023-10-12", )], )
    """

    claim_id: ClaimId
    status: ClaimStatus
    clearinghouse: typing.Optional[str] = None
    clearinghouse_claim_id: typing.Optional[str] = None
    payer_claim_id: typing.Optional[str] = None
    service_lines: typing.List[ServiceLine]
    eras: typing.List[Era]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
