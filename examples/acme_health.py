from candid import (
    CandidApiEnvironment,
    EncounterExternalId,
    Date,
    PatientCreate,
    Gender,
    StreetAddressShortZip,
    State,
    StreetAddressLongZip,
    DiagnosisCreate,
    DiagnosisTypeCode,
    FacilityTypeCode,
    ServiceLineCreate,
    ServiceLineUnits,
)
from candid.candid_api_client import CandidApiClient, CandidApiClientOptions
from candid.resources.encounter_providers.resources.v_2 import BillingProvider, RenderingProvider


def client_options() -> CandidApiClientOptions:
    import os
    return CandidApiClientOptions(client_id=os.environ["CLIENT_ID"], client_secret=os.environ["CLIENT_SECRET"])


def main() -> None:
    client = CandidApiClient(environment=CandidApiEnvironment.STAGING, options=client_options())

    created_encounter = client.encounters.v_4.create(
        external_id=EncounterExternalId("emr-claim-id-abc"),
        date_of_service=Date("2023-05-23"),
        patient=PatientCreate(
            external_id="emr-patient-id-123",
            first_name="Loki",
            last_name="Laufeyson",
            date_of_birth=Date("1983-12-17"),
            gender=Gender.MALE,
            address=StreetAddressShortZip(
                address_1="1234 Main St",
                address_2="Apt 9876",
                city="Asgard",
                state=State.CA,
                zip_code="94109",
                zip_plus_four_code="1234",
            ),
        ),
        patient_authorized_release=True,
        billing_provider=BillingProvider(
            organization_name="Acme Health PC",
            npi="1234567890",
            tax_id="123456789",
            address=StreetAddressLongZip(
                address_1="1234 Main St",
                address_2="Apt 9876",
                city="Asgard",
                state=State.CA,
                zip_code="94109",
                zip_plus_four_code="1234",
            ),
        ),
        rendering_provider=RenderingProvider(
            first_name="Doctor",
            last_name="Strange",
            npi="9876543210",
        ),
        diagnoses=[
            DiagnosisCreate(code_type=DiagnosisTypeCode.ABF, code="Z63.88"),
            DiagnosisCreate(code_type=DiagnosisTypeCode.ABF, code="E66.66"),
        ],
        place_of_service_code=FacilityTypeCode.TELEHEALTH,
        service_lines=[
            ServiceLineCreate(
                procedure_code="99212",
                modifiers=[],
                quantity="1",
                units=ServiceLineUnits.UN,
                charge_amount_cents=1500,
                diagnosis_pointers=[0, 1],
            ),
        ],
        clinical_notes=[],
        provider_accepts_assignment=True,
        benefits_assigned_to_provider=True,
    )

    print("Encounter ID:", created_encounter.encounter_id)


if __name__ == "__main__":
    main()
