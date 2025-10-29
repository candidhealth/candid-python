# Reference
## Auth Default
<details><summary><code>client.auth.default.<a href="src/candid/resources/auth/resources/default/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Callout intent="info">
Candid Health SDKs automatically handle authentication workflows after configuring them with the `client_id` and
`client_secret`.
</Callout>

Candid Health utilizes the [OAuth 2.0 bearer token authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) in our auth flow. You obtain the bearer token for all
subsequent API requests via the `/auth/v2/token` endpoint defined below, which requires you to provide your `client_id` and `client_secret`. Your `client_id` and `client_secret` can be [generated](https://support.joincandidhealth.com/hc/en-us/articles/23065219476244--Generating-Candid-API-Keys) from the "Users & Credentials" tab by your org admin.

The `/auth/v2/token` endpoint accepts both `Content-Type: application/json` and `Content-Type: application/x-www-form-urlencoded`. The request body should contain the `client_id` and `client_secret` as follows:

```json
{
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```
or as URL-encoded form data:

```
client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET
```

The bearer token is a signed [JWT](https://jwt.io/). The public key for the JWT can be found [here](https://candidhealth.auth0.com/pem) for any verification workflows.

The bearer token should be provided in the `Authorization` header for all subsequent API calls.

<Callout intent="warning">
The bearer token expires 5 hours after it has been created. After it has expired, the client will receive an "HTTP 401
Unauthorized" error, at which point the client should generate a new token. It is important that tokens be reused between
requests; if the client attempts to generate a token too often, it will be rate-limited and will receive an `HTTP 429 Too Many Requests` error.
</Callout>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.auth.default.get_token(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Your application's Client ID.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Your application's Client Secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BillingNotes V2
<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.create(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.delete(
    billing_note_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_note_id:** `BillingNoteId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.update(
    billing_note_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_note_id:** `BillingNoteId` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ChargeCaptureBundles V1
<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.get(
    charge_capture_claim_creation_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_claim_creation_id:** `ChargeCaptureClaimCreationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">get_summary</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.get_summary()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">resolve_charge_creation_error</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.resolve_charge_creation_error(
    charge_capture_bundle_error_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_bundle_error_id:** `uuid.UUID` 
    
</dd>
</dl>

<dl>
<dd>

**resolved_by:** `typing.Optional[str]` — A string, denoting who resolved the error for audit trail purposes.
    
</dd>
</dl>

<dl>
<dd>

**resolution_reason:** `typing.Optional[str]` — A string denoting why or how the error was dealt with for audit trail purposes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ChargeCaptureClaimCreationSortField]` — Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_status:** `typing.Optional[ChargeCaptureClaimCreationStatus]` — the status of the charge capture Claim Creation, refers to whether it was able to create a claim.
    
</dd>
</dl>

<dl>
<dd>

**charge_status:** `typing.Optional[ChargeCaptureStatus]` — the status of the charge captures
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**claim_ids:** `typing.Optional[typing.Union[EncounterId, typing.Sequence[EncounterId]]]` — A list of claim IDs to filter by. This will return all charge capture claim_creations that have a resulting claim with one of the IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_ids:** `typing.Optional[
    typing.Union[
        ChargeCaptureClaimCreationId,
        typing.Sequence[ChargeCaptureClaimCreationId],
    ]
]` — A list of Claim Creation IDs to filter by.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of billing provider NPIs to filter by. This will return all charge capture claim_creations which include one or more charges with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_name:** `typing.Optional[str]` — A string to filter by. This will return all charge capture claim_creations which include one or more charges with this service facility name.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer IDs to filter by. This will return all charge capture claim_creations which include one or more charges with one of the primary payer IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider NPIs to filter by. This will return all charge capture claim_creations which include one or more charges with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider names to filter by. This will return all charge capture claim_creations which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider NPIs to filter by. This will return all charge capture claim_creations which include one or more charges with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider names to filter by. This will return all charge capture claim_creations which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**claim_status:** `typing.Optional[ClaimStatus]` — the status of the claim to filter by created from charge capture bundle.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_category:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of claim creation categories to filter by. This will return all charge capture claim_creations which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of tags to filter by. This will return all charge captures with one of the tags.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer names to filter by. This will return all charge captures with one of the names.
    
</dd>
</dl>

<dl>
<dd>

**patient_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of patient names to filter by. This will return all charge captures with one of the names.
    
</dd>
</dl>

<dl>
<dd>

**has_charge_capture_updates:** `typing.Optional[bool]` — If true, only return claim_creations that have charge captures that have been updated since the Claim Creation has had a status of BILLED. See the updates property on ChargeCapture for more details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ChargeCapture V1
<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.charge_capture.resources.v_1 import (
    ChargeCaptureData,
    ChargeCaptureStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.create(
    data=ChargeCaptureData(),
    charge_external_id="charge_external_id",
    patient_external_id="patient_external_id",
    status=ChargeCaptureStatus.PLANNED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `ChargeCaptureData` — Charge Capture data contains all the fields needed to create an encounter, but listed as optional. Candid will use this data when attempting to bundle multiple Charge Captures into a single encounter.
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `str` — A client-specified unique ID to associate with this encounter; for example, your internal encounter ID or a Dr. Chrono encounter ID. This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `str` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status:** `ChargeCaptureStatus` — the status of the charge capture
    
</dd>
</dl>

<dl>
<dd>

**originating_system:** `typing.Optional[str]` — An optional string field denoting the originating system of the charge.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_category:** `typing.Optional[str]` — An optional string field denoting the user defined category of the claim creation.
    
</dd>
</dl>

<dl>
<dd>

**ehr_source_url:** `typing.Optional[str]` — External URL reference that links to Charge Capture details within the external system (e.g. the EHR visit page). Send full URL format for the external link (e.g. https://emr_charge_capture_url.com/123).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">create_from_pre_encounter_patient</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Charge Capture from a pre-encounter patient and appointment. This endpoint is intended to be used by consumers who are managing
patients and appointments in the pre-encounter service and is currently under development. Consumers who are not taking advantage
of the pre-encounter service should use the standard create endpoint.

At encounter creation time, information from the provided patient and appointment objects will be populated
where applicable. In particular, the following fields are populated from the patient and appointment objects:
  - Patient
  - Referring Provider
  - Subscriber Primary
  - Subscriber Secondary
  - Referral Number
  - Responsible Party
  - Guarantor

Note that these fields should not be populated in the ChargeCaptureData property of this endpoint, as they will be overwritten at encounter creation time.

Utilizing this endpoint opts you into automatic updating of the encounter when the patient or appointment is updated, assuming the
encounter has not already been submitted or adjudicated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.charge_capture.resources.v_1 import (
    ChargeCaptureData,
    ChargeCaptureStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.create_from_pre_encounter_patient(
    data=ChargeCaptureData(),
    charge_external_id="charge_external_id",
    pre_encounter_patient_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    pre_encounter_appointment_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ],
    status=ChargeCaptureStatus.PLANNED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `ChargeCaptureData` — Charge Capture data contains all the fields needed to create an encounter, but listed as optional. Candid will use this data when attempting to bundle multiple Charge Captures into a single encounter.
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `str` — A client-specified unique ID to associate with this encounter; for example, your internal encounter ID or a Dr. Chrono encounter ID. This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**pre_encounter_patient_id:** `PreEncounterPatientId` 
    
</dd>
</dl>

<dl>
<dd>

**pre_encounter_appointment_ids:** `typing.Sequence[PreEncounterAppointmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `ChargeCaptureStatus` — the status of the charge capture
    
</dd>
</dl>

<dl>
<dd>

**originating_system:** `typing.Optional[str]` — An optional string field denoting the originating system of the charge.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_category:** `typing.Optional[str]` — An optional string field denoting the user defined category of the claim creation.
    
</dd>
</dl>

<dl>
<dd>

**ehr_source_url:** `typing.Optional[str]` — External URL reference that links to Charge Capture details within the external system (e.g. the EHR visit page). Send full URL format for the external link (e.g. https://emr_charge_capture_url.com/123).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.update(
    charge_capture_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_id:** `ChargeCaptureId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[ChargeCaptureData]` 
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**ehr_source_url:** `typing.Optional[str]` 

External URL reference that links to Charge Capture details within the external system (e.g. the EHR visit page).
Send full URL format for the external link (e.g. https://emr_charge_capture_url.com/123).
    
</dd>
</dl>

<dl>
<dd>

**originating_system:** `typing.Optional[str]` — An optional string field denoting the originating system of the charge.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_category:** `typing.Optional[str]` — An optional string field denoting the user defined category of the claim creation.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ChargeCaptureStatus]` — the status of the charge capture
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.get(
    charge_capture_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_id:** `ChargeCaptureId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ChargeCaptureSortField]` — Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ChargeCaptureStatus]` — the status of the charge captures
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**claim_ids:** `typing.Optional[typing.Union[EncounterId, typing.Sequence[EncounterId]]]` — A list of claim IDs to filter by. This will return all charge captures that have a resulting claim with one of the IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_ids:** `typing.Optional[
    typing.Union[
        ChargeCaptureClaimCreationId,
        typing.Sequence[ChargeCaptureClaimCreationId],
    ]
]` — A list of Claim Creation IDs to filter by.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of billing provider NPIs to filter by. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_name:** `typing.Optional[str]` — A string to filter by. This will return all charge captures with this service facility name.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer IDs to filter by. This will return all charge captures with one of the primary payer IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider NPIs to filter by. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider names to filter by. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider NPIs to filter by. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider names to filter by. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_category:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of claim creation categories to filter by. This will return all charge capture claim_creations which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of tags to filter by. This will return all charge captures with one of the tags.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer names to filter by. This will return all charge captures with one of the names.
    
</dd>
</dl>

<dl>
<dd>

**patient_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of patient names to filter by. This will return all charge captures with one of the names.
    
</dd>
</dl>

<dl>
<dd>

**exclude_charges_linked_to_claims:** `typing.Optional[bool]` — Whether to exclude charge captures which are part of a claim creation.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id_ranked_sort:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status_ranked_sort:** `typing.Optional[ChargeCaptureStatus]` — The charge capture status to show first
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id_ranked_sort:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min_ranked_sort:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max_ranked_sort:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 

Filter by any of the following fields: charge_id, claim_id, patient external_id,
patient date of birth, patient first name, patient last name,
or charge external id.
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `typing.Optional[BillableStatusType]` — Defines if the Encounter is to be billed by Candid to the responsible_party. Examples for when this should be set to NOT_BILLABLE include if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    
</dd>
</dl>

<dl>
<dd>

**responsible_party:** `typing.Optional[ResponsiblePartyType]` — Defines the party to be billed with the initial balance owed on the claim. Use SELF_PAY if you intend to bill self pay/cash pay.
    
</dd>
</dl>

<dl>
<dd>

**claim_ids_ranked_sort:** `typing.Optional[typing.Union[EncounterId, typing.Sequence[EncounterId]]]` — A list of claim IDs to show first. This will return all charge captures that have a resulting claim with one of the IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_ids_ranked_sort:** `typing.Optional[
    typing.Union[
        ChargeCaptureClaimCreationId,
        typing.Sequence[ChargeCaptureClaimCreationId],
    ]
]` — A list of Claim Creation IDs to show first.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npis_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of billing provider NPIs to show first. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_name_ranked_sort:** `typing.Optional[str]` — A string to show first. This will return all charge captures with this service facility name.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_ids_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer IDs to show first. This will return all charge captures with one of the primary payer IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npis_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider NPIs to show first. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_names_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider names to show first. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_npis_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider NPIs to show first. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_names_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider names to show first. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**claim_status:** `typing.Optional[ClaimStatus]` — the status of the claim to filter by created from charge capture bundle.
    
</dd>
</dl>

<dl>
<dd>

**claim_creation_category_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of claim creation categories to sort by. This will return all charge capture claim_creations which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**tags_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of tags. This will return all charge captures with one of the tags.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_names_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer names to sort by. This will return all charge captures with one of the names.
    
</dd>
</dl>

<dl>
<dd>

**patient_names_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of patient names to sort by. This will return all charge captures with one of the names.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">update_post_billed_changes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.update_post_billed_changes(
    charge_capture_change_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ],
    resolved=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_change_ids:** `typing.Sequence[ChargeCapturePostBilledChangeId]` 

A list of UUIDs corresponding to ChargeCapturePostBilledChanges.
All of the charges sent will be marked as resolved
    
</dd>
</dl>

<dl>
<dd>

**resolved:** `bool` 

Whether the change has been resolved. If true, the change will be marked as resolved.
If false, the change will be marked as unresolved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contracts V2
<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.get(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of contracts returned. Defaults to 1000. Max is 1000.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[ContractingProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Optional[
    typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter to contracts that include any of the included payer names.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` — The status of the contract. Defaults to `pending`
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ContractSortField]` — Potentially sort by a contract related attribute.  Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Direction of sort, defaulting to desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new contract within the user's current organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import Regions_States, State
from candid.resources.contracts.resources.v_2 import InsuranceTypes

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.create(
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ],
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    effective_date="effective_date",
    regions=Regions_States(
        states=[State.AA, State.AA],
    ),
    commercial_insurance_types=InsuranceTypes(),
    medicare_insurance_types=InsuranceTypes(),
    medicaid_insurance_types=InsuranceTypes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contracting_provider_id:** `ContractingProviderId` — The UUID of the provider under agreement to the contract
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Set[RenderingProviderid]` 

A rendering provider isn't contracted directly with the payer but can render
services under the contract held by the contracting provider.
Max items is 4000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The UUID of the insurance company under agreement to the contract
    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `Date` — The starting day upon which the contract is effective
    
</dd>
</dl>

<dl>
<dd>

**regions:** `Regions` 

The state(s) to which the contract's coverage extends.
It may also be set to "national" for the entirety of the US.
    
</dd>
</dl>

<dl>
<dd>

**commercial_insurance_types:** `InsuranceTypes` — The commercial plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**medicare_insurance_types:** `InsuranceTypes` — The Medicare plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**medicaid_insurance_types:** `InsuranceTypes` — The Medicaid plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[Date]` — An optional end day upon which the contract expires
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**authorized_signatory:** `typing.Optional[AuthorizedSignatory]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.delete(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.update(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Optional[typing.Set[RenderingProviderid]]` 

A rendering provider isn't contracted directly with the payer but can render
services under the contract held by the contracting provider.
Max items is 4000.
    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `typing.Optional[Date]` — The starting day upon which the contract is effective
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[DateUpdate]` — An optional end day upon which the contract expires
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[RegionsUpdate]` 

If present, the contract's rendering providers will be patched to this exact
value, overriding what was set before.
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**authorized_signatory:** `typing.Optional[AuthorizedSignatoryUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**commercial_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**medicare_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**medicaid_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credentialing V2
<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">create_facility</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.create_facility(
    service_facility_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_facility_id:** `uuid.UUID` — The ID of the service facility covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `uuid.UUID` — The ID of the billing provider for which the service facility is covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The ID of the payer covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get_facility</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get_facility(
    facility_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**facility_credentialing_id:** `FacilityCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get_all_facilities</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get_all_facilities()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — Filter by payer.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[uuid.UUID]` — Filter to a particular contracting provider.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_id:** `typing.Optional[uuid.UUID]` — Filter to a particular service facility.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">delete_facility</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a credentialing span rate from the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.delete_facility(
    facility_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**facility_credentialing_id:** `FacilityCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">update_facility</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.update_facility(
    facility_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**facility_credentialing_id:** `FacilityCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `uuid.UUID` — The ID of the billing provider for which the service facility is covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — The ID of the payer doing the credentialing.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[Regions]` — The states covered by the credentialing span. A span may be national and cover all states.
    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import Regions_States, State

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.create(
    rendering_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    regions=Regions_States(
        states=[State.AA, State.AA],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rendering_provider_id:** `uuid.UUID` — The ID of the rendering provider covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `uuid.UUID` — The ID of the billing provider for which the service facility is covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The ID of the payer covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `Regions` — The states covered by the credentialing span. A span may be national and cover all states.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — Filter by payer.
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `typing.Optional[uuid.UUID]` — Filter to a particular provider. Use in conjunction as_rendering_provider and as_contracting_provider.
    
</dd>
</dl>

<dl>
<dd>

**as_rendering_provider:** `typing.Optional[bool]` — Filter to credentialing spans where the provider is a rendering provider. To use this filter provider_id is required.
    
</dd>
</dl>

<dl>
<dd>

**as_contracting_provider:** `typing.Optional[bool]` — Filter to credentialing spans where the provider is a contracting provider. To use this filter provider_id is required.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a credentialing span rate from the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.delete(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.update(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[uuid.UUID]` — The ID of the billing provider for which the service facility is covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — The ID of the payer doing the credentialing.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[Regions]` — The states covered by the credentialing span. A span may be national and cover all states.
    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomSchemas V1
<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">get_multi</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom schemas.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a custom schema with a given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.get(
    schema_id=uuid.UUID(
        "ec096b13-f80a-471d-aaeb-54b021c9d582",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `SchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom schema with a set of typed keys. Schema keys can be referenced as inputs in user-configurable rules in the Rules
Engine, and key-value pairs can be attached to claims via the Encounters API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.commons import Primitive
from candid.resources.custom_schemas.resources.v_1 import SchemaField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.create(
    name="General Medicine",
    description="Values associated with a generic visit",
    fields=[
        SchemaField(
            key="provider_category",
            type=Primitive.STRING,
        ),
        SchemaField(
            key="is_urgent_care",
            type=Primitive.BOOLEAN,
        ),
        SchemaField(
            key="bmi",
            type=Primitive.DOUBLE,
        ),
        SchemaField(
            key="age",
            type=Primitive.INTEGER,
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Sequence[SchemaField]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name, description, or keys on a preexisting schema.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import Primitive
from candid.resources.custom_schemas.resources.v_1 import SchemaField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.update(
    schema_id=uuid.UUID(
        "ec096b13-f80a-471d-aaeb-54b021c9d582",
    ),
    name="General Medicine and Health",
    description="Values collected during all visits",
    fields_to_add=[
        SchemaField(
            key="visit_type",
            type=Primitive.STRING,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `SchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fields_to_add:** `typing.Optional[typing.Sequence[SchemaField]]` — A list of typed entries to add to schema. Only additive modifications are permitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Eligibility V2
<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Tip>Candid is deprecating support for this endpoint. It is instead recommended to use [Candid's Stedi passthrough endpoint](https://docs.joincandidhealth.com/api-reference/pre-encounter/eligibility-checks/v-1/post).
For assistance with the transition, please reference the [Transitioning to Candid's New Eligibility Endpoint](https://support.joincandidhealth.com/hc/en-us/articles/34918552872980) document in the Candid Support Center.</Tip>

This API is a wrapper around Change Healthcare's eligibility API. Below are some helpful documentation links:

- [Change Healthcare - Guides: Contents of the Eligibility Request Body](https://developers.changehealthcare.com/eligibilityandclaims/docs/contents-of-the-eligibility-request-body)
- [Change Healthcare - Guides: Use "Bare Minimum" Eligibility Requests](https://developers.changehealthcare.com/eligibilityandclaims/docs/use-bare-minimum-eligibility-requests)
- [Change Healthcare - Guides: Contents of the Eligibility Response](https://developers.changehealthcare.com/eligibilityandclaims/docs/contents-of-the-eligibility-response)
- [Change Healthcare - Guides: Eligibility JSON-to-EDI API Contents](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-json-to-edi-api-contents)
- [Change Healthcare - Guides: Eligibility Error Messages](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-error-messages)
- [Change Healthcare - Guides: FAQ](https://developers.changehealthcare.com/eligibilityandclaims/docs/frequently-asked-questions)
- [Change Healthcare - Guides: Eligibility FAQs](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-api-requests)
- [Change Healthcare - Guides: Sandbox API Values and Test Responses](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-sandbox-api-values-and-test-responses)
- [Change Healthcare - Guides: Sandbox Predefined Fields and Values](https://developers.changehealthcare.com/eligibilityandclaims/docs/sandbox-predefined-fields-and-values)
- [Change Healthcare - Guides: Using Test Payers in the Sandbox](https://developers.changehealthcare.com/eligibilityandclaims/docs/use-the-test-payers-in-the-sandbox-api)

A schema of the response object can be found here: [Change Healthcare Docs](https://developers.changehealthcare.com/eligibilityandclaims/reference/medicaleligibility)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check_availity</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Tip>Candid is deprecating support for this endpoint. It is instead recommended to use [Candid's Stedi passthrough endpoint](https://docs.joincandidhealth.com/api-reference/pre-encounter/eligibility-checks/v-1/post).
For assistance with the transition, please reference the [Transitioning to Candid's New Eligibility Endpoint](https://support.joincandidhealth.com/hc/en-us/articles/34918552872980) document in the Candid Support Center.</Tip>

**Availity has transitioned their GET endpoint to a POST endpoint. Candid has updated their pass-through integration to enable backwards compatibility for the GET endpoint so that customers do not have to immediately update their integrations.**

**Candid recommends integrations with the [POST endpoint](https://docs.joincandidhealth.com/api-reference/eligibility/v-2/submit-eligibility-check-availity-post) to ensure the best possible integration experience. Given the transition, Availity’s documentation will be out of sync with this endpoint.**

If you'd like access to this endpoint, please reach out to support@joincandidhealth.com with the subject line "Action: Activate Availity Eligibility API Endpoint

This API is a wrapper around Availity's coverages API. Below are some helpful documentation links:

- [Availity - Coverages 1.0.0 API](https://developer.availity.com/partner/documentation#c_coverages_references)
- [Candid Availity Eligibility Integration Guide](https://support.joincandidhealth.com/hc/en-us/articles/24218441631892--Availity-Eligibility-Integration-Guide)

A schema of the response object can be found here: [Availity Docs](https://developer.availity.com/partner/product/191210/api/190898#/Coverages_100/operation/%2Fcoverages%2F{id}/get)
* Note Availity requires a free developer account to access this documentation.

Check connection status of Availity API and partners here:
- [Availity Trading Partner Connection Status](https://www.availity.com/status/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check_availity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check_availity_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Tip>Candid is deprecating support for this endpoint. It is instead recommended to use [Candid's Stedi passthrough endpoint](https://docs.joincandidhealth.com/api-reference/pre-encounter/eligibility-checks/v-1/post).
For assistance with the transition, please reference the [Transitioning to Candid's New Eligibility Endpoint](https://support.joincandidhealth.com/hc/en-us/articles/34918552872980) document in the Candid Support Center.</Tip>

If you'd like access to this endpoint, please reach out to support@joincandidhealth.com with the subject line "Action: Activate Availity Eligibility API Endpoint

This API is a wrapper around Availity's coverages API. Below are some helpful documentation links:

- [Availity - Coverages 1.0.0 API](https://developer.availity.com/partner/documentation#c_coverages_references)
- [Candid Availity Eligibility Integration Guide](https://support.joincandidhealth.com/hc/en-us/articles/24218441631892--Availity-Eligibility-Integration-Guide)

A schema of the response object can be found here: [Availity Docs](https://developer.availity.com/partner/product/191210/api/190898#/Coverages_100/operation/%2Fcoverages%2F{id}/get)
* Note Availity requires a free developer account to access this documentation.

Check connection status of Availity API and partners here:
- [Availity Trading Partner Connection Status](https://www.availity.com/status/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check_availity_post(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EncounterAttachments V1
<details><summary><code>client.encounter_attachments.v_1.<a href="src/candid/resources/encounter_attachments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_attachments.v_1.get(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_attachments.v_1.<a href="src/candid/resources/encounter_attachments/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_attachments.v_1.delete(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    attachment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `AttachmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EncounterProviders V2
<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import (
    ReferringProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ReferringProviderUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReferringProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import (
    InitialReferringProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=InitialReferringProviderUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `InitialReferringProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import (
    SupervisingProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=SupervisingProviderUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SupervisingProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import (
    OrderingProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrderingProviderUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrderingProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import ReferringProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ReferringProvider(
        npi="npi",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReferringProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import (
    InitialReferringProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=InitialReferringProvider(
        npi="npi",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `InitialReferringProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import (
    SupervisingProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=SupervisingProvider(
        npi="npi",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SupervisingProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_providers.resources.v_2 import OrderingProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrderingProvider(
        npi="npi",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrderingProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EncounterSupplementalInformation V1
<details><summary><code>client.encounter_supplemental_information.v_1.<a href="src/candid/resources/encounter_supplemental_information/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_supplemental_information.v_1.get(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_supplemental_information.v_1.<a href="src/candid/resources/encounter_supplemental_information/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import ReportTransmissionCode, ReportTypeCode
from candid.resources.encounter_supplemental_information.resources.v_1 import (
    AttachmentInclusion,
    CreateSupplementalInformationRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_supplemental_information.v_1.create(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=CreateSupplementalInformationRequest(
        attachment_report_type_code=ReportTypeCode.C_03,
        attachment_transmission_code=ReportTransmissionCode.CBM,
        attachment_inclusion=AttachmentInclusion.NOT_INCLUDED,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateSupplementalInformationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_supplemental_information.v_1.<a href="src/candid/resources/encounter_supplemental_information/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounter_supplemental_information.resources.v_1 import (
    UpdateSupplementalInformationRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_supplemental_information.v_1.update(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    supplemental_information_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=UpdateSupplementalInformationRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**supplemental_information_id:** `SupplementalInformationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSupplementalInformationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_supplemental_information.v_1.<a href="src/candid/resources/encounter_supplemental_information/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_supplemental_information.v_1.delete(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    supplemental_information_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**supplemental_information_id:** `SupplementalInformationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Encounters V4
<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient
from candid.resources.claims import ClaimStatus
from candid.resources.encounters.resources.v_4 import EncounterSortOptions

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.get_all(
    limit=100,
    claim_status=ClaimStatus.BILLER_RECEIVED,
    sort=EncounterSortOptions.CREATED_AT_ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    date_of_service_min=datetime.date.fromisoformat(
        "2019-08-24",
    ),
    date_of_service_max=datetime.date.fromisoformat(
        "2019-08-25",
    ),
    primary_payer_names="Medicare,Medicaid",
    search_term="doe",
    external_id="123456",
    diagnoses_updated_since=datetime.datetime.fromisoformat(
        "2019-08-24 14:15:22+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**claim_status:** `typing.Optional[ClaimStatus]` — Indicates the current status of an insurance claim within the billing process.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EncounterSortOptions]` — Defaults to created_at:desc.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_names:** `typing.Optional[str]` — Comma delimited string.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 

Filter by any of the following fields: encounter_id, claim_id, patient external_id,
patient date of birth, patient first name, patient last name,
or encounter external id.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[EncounterExternalId]` — Filter to an exact match on encounter external_id, if one exists.
    
</dd>
</dl>

<dl>
<dd>

**diagnoses_updated_since:** `typing.Optional[dt.datetime]` — ISO 8601 timestamp; ideally in UTC (although not required): 2019-08-24T14:15:22Z.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[TagId, typing.Sequence[TagId]]]` — Filter by name of tags on encounters.
    
</dd>
</dl>

<dl>
<dd>

**work_queue_id:** `typing.Optional[WorkQueueId]` 
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `typing.Optional[BillableStatusType]` — Defines if the Encounter is to be billed by Candid to the responsible_party. Examples for when this should be set to NOT_BILLABLE include if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    
</dd>
</dl>

<dl>
<dd>

**responsible_party:** `typing.Optional[ResponsiblePartyType]` — Defines the party to be billed with the initial balance owed on the claim. Use SELF_PAY if you intend to bill self pay/cash pay.
    
</dd>
</dl>

<dl>
<dd>

**owner_of_next_action:** `typing.Optional[EncounterOwnerOfNextActionType]` — The party who is responsible for taking the next action on an Encounter, as defined by ownership of open Tasks.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.get(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient
from candid.resources.commons import (
    FacilityTypeCode,
    State,
    StreetAddressLongZip,
    StreetAddressShortZip,
)
from candid.resources.diagnoses import DiagnosisCreate, DiagnosisTypeCode
from candid.resources.encounter_providers.resources.v_2 import (
    BillingProvider,
    RenderingProvider,
)
from candid.resources.encounters.resources.v_4 import (
    BillableStatusType,
    EncounterCreate,
    ResponsiblePartyType,
)
from candid.resources.individual import Gender, PatientCreate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.create(
    request=EncounterCreate(
        billing_provider=BillingProvider(
            address=StreetAddressLongZip(
                zip_plus_four_code="zip_plus_four_code",
                address_1="address1",
                city="city",
                state=State.AA,
                zip_code="zip_code",
            ),
            tax_id="tax_id",
            npi="npi",
        ),
        diagnoses=[
            DiagnosisCreate(
                code_type=DiagnosisTypeCode.ABF,
                code="code",
            ),
            DiagnosisCreate(
                code_type=DiagnosisTypeCode.ABF,
                code="code",
            ),
        ],
        place_of_service_code=FacilityTypeCode.PHARMACY,
        rendering_provider=RenderingProvider(
            npi="npi",
        ),
        patient=PatientCreate(
            external_id="external_id",
            date_of_birth=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            address=StreetAddressShortZip(
                address_1="address1",
                city="city",
                state=State.AA,
                zip_code="zip_code",
            ),
            first_name="first_name",
            last_name="last_name",
            gender=Gender.MALE,
        ),
        responsible_party=ResponsiblePartyType.INSURANCE_PAY,
        external_id="external_id",
        patient_authorized_release=True,
        benefits_assigned_to_provider=True,
        provider_accepts_assignment=True,
        billable_status=BillableStatusType.BILLABLE,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EncounterCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">create_from_pre_encounter_patient</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an encounter from a pre-encounter patient and appointment. This endpoint is intended to be used by consumers who are managing
patients and appointments in the pre-encounter service and is currently under development. Consumers who are not taking advantage
of the pre-encounter service should use the standard create endpoint.

The endpoint will create an encounter from the provided fields, pulling information from the provided patient and appointment objects
where applicable. In particular, the following fields are populated from the patient and appointment objects:
  - Patient
  - Referring Provider
  - Subscriber Primary
  - Subscriber Secondary
  - Referral Number
  - Responsible Party
  - Guarantor

Utilizing this endpoint opts you into automatic updating of the encounter when the patient or appointment is updated, assuming the
encounter has not already been submitted or adjudicated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import (
    FacilityTypeCode,
    State,
    StreetAddressLongZip,
)
from candid.resources.diagnoses import DiagnosisCreate, DiagnosisTypeCode
from candid.resources.encounter_providers.resources.v_2 import (
    BillingProvider,
    RenderingProvider,
)
from candid.resources.encounters.resources.v_4 import (
    BillableStatusType,
    EncounterCreateFromPreEncounter,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.create_from_pre_encounter_patient(
    request=EncounterCreateFromPreEncounter(
        rendering_provider=RenderingProvider(
            npi="npi",
        ),
        place_of_service_code=FacilityTypeCode.PHARMACY,
        diagnoses=[
            DiagnosisCreate(
                code_type=DiagnosisTypeCode.ABF,
                code="code",
            ),
            DiagnosisCreate(
                code_type=DiagnosisTypeCode.ABF,
                code="code",
            ),
        ],
        pre_encounter_patient_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        pre_encounter_appointment_ids=[
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        ],
        billing_provider=BillingProvider(
            address=StreetAddressLongZip(
                zip_plus_four_code="zip_plus_four_code",
                address_1="address1",
                city="city",
                state=State.AA,
                zip_code="zip_code",
            ),
            tax_id="tax_id",
            npi="npi",
        ),
        external_id="external_id",
        patient_authorized_release=True,
        benefits_assigned_to_provider=True,
        provider_accepts_assignment=True,
        billable_status=BillableStatusType.BILLABLE,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EncounterCreateFromPreEncounter` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.encounters.resources.v_4 import EncounterUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.update(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=EncounterUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EncounterUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExpectedNetworkStatus V1
<details><summary><code>client.expected_network_status.v_1.<a href="src/candid/resources/expected_network_status/resources/v_1/client.py">compute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes the expected network status given the provided information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.commons import State

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.expected_network_status.v_1.compute(
    subscriber_payer_id="subscriber_payer_id",
    subscriber_payer_name="subscriber_payer_name",
    billing_provider_npi="billing_provider_npi",
    billing_provider_tin="billing_provider_tin",
    rendering_provider_npi="rendering_provider_npi",
    contracted_state=State.AA,
    date_of_service="date_of_service",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscriber_payer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_payer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npi:** `str` — The National Provider Identifier (NPI) of the healthcare provider responsible for billing. A unique 10-digit identification number.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_tin:** `str` — Follow the 9-digit format of the Taxpayer Identification Number (TIN).
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npi:** `str` — The National Provider Identifier (NPI) of the healthcare provider who delivered the services. A unique 10-digit identification number.
    
</dd>
</dl>

<dl>
<dd>

**contracted_state:** `State` — The state in which the healthcare provider has a contractual agreement with the insurance payer.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `Date` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**external_patient_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_insurance_type:** `typing.Optional[InsuranceTypeCode]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_plan_name:** `typing.Optional[str]` — The descriptive name of the insurance plan selected by the subscriber, often indicating coverage specifics or tier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExpectedNetworkStatus V2
<details><summary><code>client.expected_network_status.v_2.<a href="src/candid/resources/expected_network_status/resources/v_2/client.py">compute_for_rendering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes the expected network status for a given rendering provider.
This endpoint is not available to all customers. Reach out to the Candid sales team
to discuss enabling this endpoint if it is not available for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.commons import (
    FacilityTypeCode,
    InsuranceTypeCode,
    State,
    StreetAddressShortZip,
)
from candid.resources.expected_network_status.resources.v_2 import (
    ExpectedNetworkStatusRequestV2,
    ExpectedNetworkStatusSubscriberInformation,
    InsuranceType,
    InsuranceTypeCodes_InsuranceTypeCode,
    LineOfBusiness,
    ServiceType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.expected_network_status.v_2.compute_for_rendering_provider(
    rendering_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ExpectedNetworkStatusRequestV2(
        service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
        place_of_service_code=FacilityTypeCode.PHARMACY,
        subscriber_information=ExpectedNetworkStatusSubscriberInformation(
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            member_id="member_id",
            insurance_type=InsuranceType(
                line_of_business=LineOfBusiness.MEDICARE,
                insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                    value=InsuranceTypeCode.C_01
                ),
            ),
        ),
        patient_address=StreetAddressShortZip(
            address_1="address1",
            city="city",
            state=State.AA,
            zip_code="zip_code",
        ),
        billing_provider_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        organization_service_facility_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rendering_provider_id:** `OrganizationProviderId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExpectedNetworkStatusRequestV2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.expected_network_status.v_2.<a href="src/candid/resources/expected_network_status/resources/v_2/client.py">compute_all_in_network_providers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes all the in network providers for a given set of inputs.
This endpoint is not available to all customers. Reach out to the Candid sales team
to discuss enabling this endpoint if it is not available for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.commons import (
    FacilityTypeCode,
    InsuranceTypeCode,
    State,
    StreetAddressShortZip,
)
from candid.resources.expected_network_status.resources.v_2 import (
    ComputeAllInNetworkProvidersRequest,
    ExpectedNetworkStatusSubscriberInformation,
    InsuranceType,
    InsuranceTypeCodes_InsuranceTypeCode,
    LineOfBusiness,
    ServiceType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.expected_network_status.v_2.compute_all_in_network_providers(
    request=ComputeAllInNetworkProvidersRequest(
        service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
        place_of_service_code=FacilityTypeCode.PHARMACY,
        subscriber_information=ExpectedNetworkStatusSubscriberInformation(
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            member_id="member_id",
            insurance_type=InsuranceType(
                line_of_business=LineOfBusiness.MEDICARE,
                insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                    value=InsuranceTypeCode.C_01
                ),
            ),
        ),
        patient_address=StreetAddressShortZip(
            address_1="address1",
            city="city",
            state=State.AA,
            zip_code="zip_code",
        ),
        billing_provider_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        organization_service_facility_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ComputeAllInNetworkProvidersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Exports V3
<details><summary><code>client.exports.v_3.<a href="src/candid/resources/exports/resources/v_3/client.py">get_exports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>
API-based exports are in the process of being deprecated in favor of Candid Data Share and are not being offered to new customers.
Please see the [Candid Data Share docs](https://docs.joincandidhealth.com/introduction/candid-data-share) for more information.
</Warning>

Retrieve CSV-formatted reports on claim submissions and outcomes. This endpoint returns Export objects that contain an
authenticated URL to a customer's reports with a 2min TTL. The schema for the CSV export can be found [here](https://app.joincandidhealth.com/files/exports_schema.csv).

**Schema changes:** Changing column order, removing columns, or changing the name of a column is considered a
[Breaking Change](../../../api-principles/breaking-changes). Adding new columns to the end of the Exports file is not considered a
Breaking Change and happens periodically. For this reason, it is important that any downstream automation or processes built on top
of Candid Health's export files be resilient to the addition of new columns at the end of the file.

**SLA guarantees:** Files for a given date are guaranteed to be available after 3 business days. For example, Friday's file will be
available by Wednesday at the latest. If file generation is still in progress upon request before 3 business days have passed, the
caller will receive a 422 response. If the file has already been generated, it will be served. Historic files should be available
up to 90 days in the past by default. Please email our [Support team](mailto:support@joincandidhealth.com) with any data requests
outside of these stated guarantees.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.exports.v_3.get_exports(
    start_date=datetime.date.fromisoformat(
        "2023-10-01",
    ),
    end_date=datetime.date.fromisoformat(
        "2023-10-02",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `dt.date` 

Beginning date of claim versions returned in the export, ISO 8601 date e.g. 2019-08-24.
Must be at least 1 calendar day in the past. Cannot be earlier than 2022-10-07.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `dt.date` 

Ending date of claim versions returned in the export, ISO 8601 date; e.g. 2019-08-24.
Must be within 30 days of start_date.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExternalPaymentAccountConfig V1
<details><summary><code>client.external_payment_account_config.v_1.<a href="src/candid/resources/external_payment_account_config/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.external_payment_account_config.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FeeSchedules V3
<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_match</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the rate that matches a service line.  No result means no rate exists matching the service line's dimensions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_match(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">test_match</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tests a service line against a rate to see if it matches.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.test_match(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rate_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**rate_id:** `RateId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of dimensions with their rates. The rates returned will always be the most recent versions of those rates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of dimensions returned. Defaults to 100. Max is 100.
    
</dd>
</dl>

<dl>
<dd>

**active_date:** `typing.Optional[dt.date]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_billing_provider_id:** `typing.Optional[OrganizationProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**zip_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**license_types:** `typing.Optional[typing.Union[LicenseType, typing.Sequence[LicenseType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**facility_type_codes:** `typing.Optional[
    typing.Union[FacilityTypeCode, typing.Sequence[FacilityTypeCode]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**network_types:** `typing.Optional[typing.Union[NetworkType, typing.Sequence[NetworkType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_plan_group_ids:** `typing.Optional[
    typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**cpt_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[
    typing.Union[ProcedureModifier, typing.Sequence[ProcedureModifier]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_unique_values_for_dimension</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets unique values for a dimension based on other selection criteria. The response is a list of dimensions with your criteria and the unique values populated. This API is useful for driving pivots on dimension values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.fee_schedules.resources.v_3 import DimensionName

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_unique_values_for_dimension(
    pivot_dimension=DimensionName.PAYER_UUID,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pivot_dimension:** `DimensionName` — The name of the dimension to fetch unique values for.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of values returned. Defaults to 1000. Max is 1000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_billing_provider_id:** `typing.Optional[OrganizationProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**zip_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**license_types:** `typing.Optional[typing.Union[LicenseType, typing.Sequence[LicenseType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**facility_type_codes:** `typing.Optional[
    typing.Union[FacilityTypeCode, typing.Sequence[FacilityTypeCode]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**network_types:** `typing.Optional[typing.Union[NetworkType, typing.Sequence[NetworkType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_plan_group_ids:** `typing.Optional[
    typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**cpt_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[
    typing.Union[ProcedureModifier, typing.Sequence[ProcedureModifier]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_rate_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets every version of a rate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_rate_history(
    rate_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rate_id:** `RateId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">upload_fee_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a new fee schedule.\n Each rate may either be totally new as qualified by it's dimensions or a new version for an existing rate.\n If adding a new version to an existing rate, the rate must be posted with the next version number (previous version + 1) or a EntityConflictError will be returned.\n Use the dry run flag to discover already existing rates and to run validations.  If validations for any rate fail, no rates will be saved to the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.commons import (
    FacilityTypeCode,
    NetworkType,
    ProcedureModifier,
    State,
)
from candid.resources.fee_schedules.resources.v_3 import (
    Dimensions,
    RateEntry,
    RateUpload_NewRate,
)
from candid.resources.organization_providers.resources.v_2 import LicenseType

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.upload_fee_schedule(
    dry_run=True,
    rates=[
        RateUpload_NewRate(
            dimensions=Dimensions(
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                organization_billing_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                states=[State.AA],
                zip_codes={"zip_codes"},
                license_types=[LicenseType.MD],
                facility_type_codes=[FacilityTypeCode.PHARMACY],
                network_types=[NetworkType.PPO],
                payer_plan_group_ids=[
                    uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ],
                cpt_code="cpt_code",
                modifiers=[ProcedureModifier.AV],
            ),
            entries=[
                RateEntry(
                    start_date=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    rate_cents=1,
                    is_deactivated=True,
                ),
                RateEntry(
                    start_date=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    rate_cents=1,
                    is_deactivated=True,
                ),
            ],
        ),
        RateUpload_NewRate(
            dimensions=Dimensions(
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                organization_billing_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                states=[State.AA],
                zip_codes={"zip_codes"},
                license_types=[LicenseType.MD],
                facility_type_codes=[FacilityTypeCode.PHARMACY],
                network_types=[NetworkType.PPO],
                payer_plan_group_ids=[
                    uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ],
                cpt_code="cpt_code",
                modifiers=[ProcedureModifier.AV],
            ),
            entries=[
                RateEntry(
                    start_date=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    rate_cents=1,
                    is_deactivated=True,
                ),
                RateEntry(
                    start_date=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    rate_cents=1,
                    is_deactivated=True,
                ),
            ],
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dry_run:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**rates:** `typing.Sequence[RateUpload]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">delete_rate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a rate from the system.  Only the most recent version of a rate can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.delete_rate(
    rate_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rate_id:** `RateId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_payer_thresholds_default</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the default payer threshold
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_payer_thresholds_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_payer_thresholds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of payers and thresholds by their uuids
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_payer_thresholds(
    payer_uuids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuids:** `typing.Union[PayerUuid, typing.Sequence[PayerUuid]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">set_payer_threshold</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the threshold information for a payer
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.fee_schedules.resources.v_3 import PayerThreshold

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.set_payer_threshold(
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=PayerThreshold(
        disable_paid_incorrectly=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuid:** `PayerUuid` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PayerThreshold` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">hard_delete_rates</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hard deletes rates from the system that match the provided dimensions.  This is a destructive operation and cannot be undone.  If an empty dimensions object is provided, all rates will be hard deleted.  The maximum number of rates this API will delete at a time is 10000.  Returns the number of rates deleted and if that number is the maximum, the caller should call this API again to continue deleting rates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import (
    FacilityTypeCode,
    NetworkType,
    ProcedureModifier,
    State,
)
from candid.resources.fee_schedules.resources.v_3 import OptionalDimensions
from candid.resources.organization_providers.resources.v_2 import LicenseType

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.hard_delete_rates(
    request=OptionalDimensions(
        states=[State.AA],
        zip_codes={"zip_codes"},
        license_types=[LicenseType.MD],
        facility_type_codes=[FacilityTypeCode.PHARMACY],
        network_types=[NetworkType.PPO],
        payer_plan_group_ids=[
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            )
        ],
        modifiers=[ProcedureModifier.AV],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OptionalDimensions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">hard_delete_rates_by_ids</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hard deletes specific rates from the system by their IDs. This is a destructive operation and cannot be undone. Limited to 100 rate IDs maximum per request. For bulk deletion of more than 100 rates, use the hard_delete_rates endpoint with dimension filters. Returns the number of rates deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.hard_delete_rates_by_ids(
    rate_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rate_ids:** `typing.Sequence[RateId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guarantor V1
<details><summary><code>client.guarantor.v_1.<a href="src/candid/resources/guarantor/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new guarantor and returns the newly created Guarantor object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressShortZip
from candid.resources.guarantor.resources.v_1 import GuarantorCreate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.guarantor.v_1.create(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=GuarantorCreate(
        first_name="first_name",
        last_name="last_name",
        external_id="external_id",
        address=StreetAddressShortZip(
            address_1="address1",
            city="city",
            state=State.AA,
            zip_code="zip_code",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GuarantorCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guarantor.v_1.<a href="src/candid/resources/guarantor/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a guarantor by its `guarantor_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.guarantor.v_1.get(
    guarantor_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guarantor_id:** `GuarantorId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guarantor.v_1.<a href="src/candid/resources/guarantor/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a guarantor by its `guarantor_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.guarantor.resources.v_1 import GuarantorUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.guarantor.v_1.update(
    guarantor_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=GuarantorUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guarantor_id:** `GuarantorId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GuarantorUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## HealthCareCodeInformation V1
<details><summary><code>client.health_care_code_information.v_1.<a href="src/candid/resources/health_care_code_information/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.health_care_code_information.resources.v_1 import (
    HealthCareCodeInformationUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.health_care_code_information.v_1.update(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=HealthCareCodeInformationUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `HealthCareCodeInformationUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_care_code_information.v_1.<a href="src/candid/resources/health_care_code_information/resources/v_1/client.py">get_all_for_encounter</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.health_care_code_information.v_1.get_all_for_encounter(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ImportInvoice V1
<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">import_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import an existing invoice from a third party service to reflect state in Candid.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.import_invoice.resources.v_1 import (
    CreateImportInvoiceRequest,
)
from candid.resources.invoices.resources.v_2 import (
    InvoiceItemAttributionCreate_ServiceLineId,
    InvoiceItemCreate,
    InvoiceStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.import_invoice(
    request=CreateImportInvoiceRequest(
        external_payment_account_config_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        patient_external_id="patient_external_id",
        external_customer_identifier="external_customer_identifier",
        items=[
            InvoiceItemCreate(
                attribution=InvoiceItemAttributionCreate_ServiceLineId(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
                amount_cents=1,
            ),
            InvoiceItemCreate(
                attribution=InvoiceItemAttributionCreate_ServiceLineId(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
                amount_cents=1,
            ),
        ],
        status=InvoiceStatus.DRAFT,
        external_identifier="external_identifier",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateImportInvoiceRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Invoices for the authenticated user's organziation with all filters applied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**encounter_external_id:** `typing.Optional[EncounterExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — partial match supported
    
</dd>
</dl>

<dl>
<dd>

**due_date_before:** `typing.Optional[dt.date]` — all invoices whose due date is before this due date, not inclusive
    
</dd>
</dl>

<dl>
<dd>

**due_date_after:** `typing.Optional[dt.date]` — all invoices whose due date is after this due date, not inclusive
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — all invoices that match any of the provided statuses
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InvoiceSortField]` — Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve and view an import invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.get(
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — InvoiceId to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the information on the imported invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.import_invoice.resources.v_1 import (
    ImportInvoiceUpdateRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.update(
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ImportInvoiceUpdateRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ImportInvoiceUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InsuranceAdjudications V1
<details><summary><code>client.insurance_adjudications.v_1.<a href="src/candid/resources/insurance_adjudications/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created insurance adjudication by its `insurance_adjudication_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_adjudications.v_1.get(
    insurance_adjudication_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_adjudication_id:** `InsuranceAdjudicationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_adjudications.v_1.<a href="src/candid/resources/insurance_adjudications/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new insurance adjudication record and returns the newly created InsuranceAdjudication object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.commons import ClaimAdjustmentGroupCodes
from candid.resources.era_commons import ClaimStatusCodeCreate
from candid.resources.insurance_adjudications.resources.v_1 import (
    ClaimAdjudicationCreate,
    InsuranceAdjudicationCreate,
    ServiceLineAdjudicationCreate,
)
from candid.resources.payers.resources.v_3 import PayerIdentifier_PayerInfo
from candid.resources.remits.resources.v_1 import Payee, PayeeIdentifier_Npi
from candid.resources.x_12.resources.v_1 import (
    Carc,
    ClaimAdjustmentReasonCode,
    Rarc,
    RemittanceAdviceRemarkCode,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_adjudications.v_1.create(
    request=InsuranceAdjudicationCreate(
        payer_identifier=PayerIdentifier_PayerInfo(
            payer_id="payer_id",
            payer_name="payer_name",
        ),
        payee=Payee(
            payee_name="payee_name",
            payee_identifier=PayeeIdentifier_Npi(value="payee_identifier"),
        ),
        check_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        claims={
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ): [
                ClaimAdjudicationCreate(
                    claim_status_code=ClaimStatusCodeCreate.PROCESSED_AS_PRIMARY,
                    service_lines={
                        uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        ): [
                            ServiceLineAdjudicationCreate(
                                carcs=[
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                ],
                                rarcs=[
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                ],
                            ),
                            ServiceLineAdjudicationCreate(
                                carcs=[
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                ],
                                rarcs=[
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                ],
                            ),
                        ]
                    },
                    carcs=[
                        ClaimAdjustmentReasonCode(
                            group_code=ClaimAdjustmentGroupCodes.CO,
                            reason_code=Carc.CARC_1,
                            amount_cents=1,
                        ),
                        ClaimAdjustmentReasonCode(
                            group_code=ClaimAdjustmentGroupCodes.CO,
                            reason_code=Carc.CARC_1,
                            amount_cents=1,
                        ),
                    ],
                ),
                ClaimAdjudicationCreate(
                    claim_status_code=ClaimStatusCodeCreate.PROCESSED_AS_PRIMARY,
                    service_lines={
                        uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        ): [
                            ServiceLineAdjudicationCreate(
                                carcs=[
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                ],
                                rarcs=[
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                ],
                            ),
                            ServiceLineAdjudicationCreate(
                                carcs=[
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                    ClaimAdjustmentReasonCode(
                                        group_code=ClaimAdjustmentGroupCodes.CO,
                                        reason_code=Carc.CARC_1,
                                        amount_cents=1,
                                    ),
                                ],
                                rarcs=[
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                    RemittanceAdviceRemarkCode(
                                        reason_code=Rarc.M_1,
                                    ),
                                ],
                            ),
                        ]
                    },
                    carcs=[
                        ClaimAdjustmentReasonCode(
                            group_code=ClaimAdjustmentGroupCodes.CO,
                            reason_code=Carc.CARC_1,
                            amount_cents=1,
                        ),
                        ClaimAdjustmentReasonCode(
                            group_code=ClaimAdjustmentGroupCodes.CO,
                            reason_code=Carc.CARC_1,
                            amount_cents=1,
                        ),
                    ],
                ),
            ]
        },
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InsuranceAdjudicationCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_adjudications.v_1.<a href="src/candid/resources/insurance_adjudications/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the insurance adjudication record matching the provided insurance_adjudication_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_adjudications.v_1.delete(
    insurance_adjudication_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_adjudication_id:** `InsuranceAdjudicationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InsurancePayments V1
<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-ERA originated insurance payments satisfying the search criteria
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InsurancePaymentSortField]` — Defaults to payment_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created insurance payment by its `insurance_payment_id`.
If the payment does not exist, a `403` will be thrown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.get(
    insurance_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_payment_id:** `InsurancePaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InsuranceRefunds V1
<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all insurance refunds satisfying the search criteria AND whose organization_id matches
the current organization_id of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InsuranceRefundSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created insurance refund by its `insurance_refund_id`.
If the refund does not exist, a `403` will be thrown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.get(
    insurance_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_refund_id:** `InsuranceRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new insurance refund record and returns the newly created `InsuranceRefund` object.
The allocations can describe whether the refund is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.financials import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
)
from candid.resources.insurance_refunds.resources.v_1 import (
    InsuranceRefundCreate,
)
from candid.resources.payers.resources.v_3 import PayerIdentifier_PayerInfo

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.create(
    request=InsuranceRefundCreate(
        payer_identifier=PayerIdentifier_PayerInfo(
            payer_id="payer_id",
            payer_name="payer_name",
        ),
        amount_cents=1,
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            ),
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InsuranceRefundCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient refund record matching the provided insurance_refund_id. If updating the refund amount,
then the allocations must be appropriately updated as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.update(
    insurance_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_refund_id:** `InsuranceRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReasonUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the insurance refund record matching the provided `insurance_refund_id`.
If the matching record's organization_id does not match the authenticated user's
current organization_id, then a response code of `403` will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.delete(
    insurance_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_refund_id:** `InsuranceRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MedicationDispense V1
<details><summary><code>client.medication_dispense.v_1.<a href="src/candid/resources/medication_dispense/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient
from candid.resources.commons import ServiceLineUnits
from candid.resources.medication_dispense.resources.v_1 import (
    MedicationDispenseCreate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.medication_dispense.v_1.create(
    request=MedicationDispenseCreate(
        medication_dispense_external_id="medication_dispense_external_id",
        patient_external_id="patient_external_id",
        procedure_code="procedure_code",
        quantity="quantity",
        units=ServiceLineUnits.MJ,
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MedicationDispenseCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NonInsurancePayerPayments V1
<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-insurance payer payments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**non_insurance_payer_id:** `typing.Optional[NonInsurancePayerId]` 
    
</dd>
</dl>

<dl>
<dd>

**check_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NonInsurancePayerPaymentSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created non-insurance payer payment by its `non_insurance_payer_payment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.get(
    non_insurance_payer_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_payment_id:** `NonInsurancePayerPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.financials import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
)
from candid.resources.non_insurance_payer_payments.resources.v_1 import (
    NonInsurancePayerPaymentCreate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.create(
    request=NonInsurancePayerPaymentCreate(
        non_insurance_payer_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        amount_cents=1,
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            ),
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `NonInsurancePayerPaymentCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.update(
    non_insurance_payer_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_payment_id:** `NonInsurancePayerPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the non-insurance payer payment record matching the provided `non_insurance_payer_payment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.delete(
    non_insurance_payer_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_payment_id:** `NonInsurancePayerPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NonInsurancePayerRefunds V1
<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-insurance payer refunds satisfying the search criteria
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**non_insurance_payer_id:** `typing.Optional[NonInsurancePayerId]` 
    
</dd>
</dl>

<dl>
<dd>

**check_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NonInsurancePayerRefundSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created non-insurance payer refund by its `non_insurance_payer_refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.get(
    non_insurance_payer_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_refund_id:** `NonInsurancePayerRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new non-insurance payer refund record and returns the newly created `NonInsurancePayerRefund` object.
The allocations can describe whether the refund is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.financials import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
)
from candid.resources.non_insurance_payer_refunds.resources.v_1 import (
    NonInsurancePayerRefundCreate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.create(
    request=NonInsurancePayerRefundCreate(
        non_insurance_payer_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        amount_cents=1,
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            ),
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `NonInsurancePayerRefundCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the non-insurance payer refund record matching the provided non_insurance_payer_refund_id. If updating the refund amount,
then the allocations must be appropriately updated as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.update(
    non_insurance_payer_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_refund_id:** `NonInsurancePayerRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReasonUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the non-insurance payer refund record matching the provided `non_insurance_payer_refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.delete(
    non_insurance_payer_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_refund_id:** `NonInsurancePayerRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NonInsurancePayers V1
<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.non_insurance_payers.resources.v_1 import (
    CreateNonInsurancePayerRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.create(
    request=CreateNonInsurancePayerRequest(
        name="name",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateNonInsurancePayerRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">toggle_enablement</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.non_insurance_payers.resources.v_1 import (
    ToggleNonInsurancePayerEnablementRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.toggle_enablement(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ToggleNonInsurancePayerEnablementRequest(
        enabled=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ToggleNonInsurancePayerEnablementRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Fuzzy-match category names of non-insurance payers.
    
</dd>
</dl>

<dl>
<dd>

**categories_exact:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter by one or more categories by name.
When multiple are present, non-insurance payers with any of the specified
categories will be matched.
    
</dd>
</dl>

<dl>
<dd>

**clinical_trial_ids:** `typing.Optional[typing.Union[ClinicalTrialId, typing.Sequence[ClinicalTrialId]]]` 

Filter by one or more clinical trials by their `clinical_trial_id`.
When multiple are present, non-insurance payers with any of the specified
clinical trials will be matched.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NonInsurancePayerSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">get_categories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of all non-insurance payer categories.

Non-insurance payer categories are simply strings and are not stored as a
separate object in Candid. They are created when added to at least one
non-insurance payer's `category` field and are deleted when there are no
longer any non-insurance payers that contain them.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.get_categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_term:** `typing.Optional[str]` — Filters categories by fuzzy matching on name.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the maximum number of categories that will be returned. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — The page token to continue paging through a previous request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.get(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.non_insurance_payers.resources.v_1 import (
    NonInsurancePayerUpdateRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.update(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=NonInsurancePayerUpdateRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NonInsurancePayerUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.delete(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrganizationProviders V3
<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.get(
    organization_provider_id=uuid.UUID(
        "965a563a-0285-4910-9569-e3739c0f6eab",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_provider_id:** `OrganizationProviderId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.organization_providers.resources.v_2 import (
    OrganizationProviderSortOptions,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.get_multi(
    limit=100,
    search_term="john",
    npi="1234567890",
    is_rendering=True,
    is_billing=True,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    sort=OrganizationProviderSortOptions.PROVIDER_NAME_ASC,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of results returned. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` — Filter to a name or a part of a name.
    
</dd>
</dl>

<dl>
<dd>

**npi:** `typing.Optional[str]` — Filter to a specific NPI.
    
</dd>
</dl>

<dl>
<dd>

**is_rendering:** `typing.Optional[bool]` — Filter to only rendering providers.
    
</dd>
</dl>

<dl>
<dd>

**is_billing:** `typing.Optional[bool]` — Filter to only billing providers.
    
</dd>
</dl>

<dl>
<dd>

**organization_provider_ids:** `typing.Optional[
    typing.Union[
        OrganizationProviderId, typing.Sequence[OrganizationProviderId]
    ]
]` — Filter to the provided organization provider IDs.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — The page token to continue paging through a previous request.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[OrganizationProviderSortOptions]` — Defaults to PROVIDER_NAME_ASC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.commons import State
from candid.resources.identifiers import (
    IdentifierCode,
    IdentifierCreate,
    IdentifierValue_MedicareProviderIdentifier,
)
from candid.resources.organization_providers.resources.v_2 import (
    LicenseType,
    ProviderType,
)
from candid.resources.organization_providers.resources.v_3 import (
    OrganizationProviderCreateV2,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.create(
    request=OrganizationProviderCreateV2(
        npi="npi",
        is_rendering=True,
        is_billing=True,
        provider_type=ProviderType.INDIVIDUAL,
        license_type=LicenseType.MD,
        qualifications=[
            IdentifierCreate(
                identifier_code=IdentifierCode.MCR,
                identifier_value=IdentifierValue_MedicareProviderIdentifier(
                    state=State.AA,
                    provider_number="provider_number",
                ),
            ),
            IdentifierCreate(
                identifier_code=IdentifierCode.MCR,
                identifier_value=IdentifierValue_MedicareProviderIdentifier(
                    state=State.AA,
                    provider_number="provider_number",
                ),
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrganizationProviderCreateV2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.organization_providers.resources.v_3 import (
    OrganizationProviderUpdateV2,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.update(
    organization_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrganizationProviderUpdateV2(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_provider_id:** `OrganizationProviderId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationProviderUpdateV2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrganizationServiceFacilities V2
<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.get(
    organization_service_facility_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_service_facility_id:** `OrganizationServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.get_multi(
    limit=100,
    name="Test Service Facility",
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of results returned. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter to a name or a part of a name.
    
</dd>
</dl>

<dl>
<dd>

**organization_service_facility_ids:** `typing.Optional[
    typing.Union[
        OrganizationServiceFacilityId,
        typing.Sequence[OrganizationServiceFacilityId],
    ]
]` — Filter to the provided organization service facility IDs.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by one or more external_ids.
    
</dd>
</dl>

<dl>
<dd>

**place_of_service_code:** `typing.Optional[FacilityTypeCode]` — Filter by Place of Service (POS) code.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — The page token to continue paging through a previous request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">get_by_external_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Looks up a single organization service facility by its `external_id` field. This can be useful
for finding service facilities within Candid which are associated with service facilities in
an external system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.get_by_external_id(
    external_id="external_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.organization_service_facilities.resources.v_2 import (
    OrganizationServiceFacilityCreate,
    ServiceFacilityMode,
    ServiceFacilityOperationalStatus,
    ServiceFacilityPhysicalType,
    ServiceFacilityStatus,
    ServiceFacilityType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.create(
    request=OrganizationServiceFacilityCreate(
        name="Test Service Facility",
        aliases=["Test Service Facility Alias"],
        description="Test Service Facility Description",
        status=ServiceFacilityStatus.ACTIVE,
        operational_status=ServiceFacilityOperationalStatus.CLOSED,
        mode=ServiceFacilityMode.INSTANCE,
        type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
        physical_type=ServiceFacilityPhysicalType.SITE,
        telecoms=["555-555-5555"],
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrganizationServiceFacilityCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.organization_service_facilities.resources.v_2 import (
    OrganizationServiceFacilityUpdate,
    ServiceFacilityMode,
    ServiceFacilityOperationalStatus,
    ServiceFacilityPhysicalType,
    ServiceFacilityStatus,
    ServiceFacilityType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.update(
    organization_service_facility_id=uuid.UUID(
        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
    ),
    request=OrganizationServiceFacilityUpdate(
        name="Test Service Facility",
        aliases=["Test Service Facility Alias"],
        description="Test Service Facility Description",
        status=ServiceFacilityStatus.ACTIVE,
        operational_status=ServiceFacilityOperationalStatus.CLOSED,
        mode=ServiceFacilityMode.INSTANCE,
        type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
        physical_type=ServiceFacilityPhysicalType.SITE,
        telecoms=["555-555-5555"],
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_service_facility_id:** `OrganizationServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationServiceFacilityUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.delete(
    organization_service_facility_id=uuid.UUID(
        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_service_facility_id:** `OrganizationServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PatientAr V1
<details><summary><code>client.patient_ar.v_1.<a href="src/candid/resources/patient_ar/resources/v_1/client.py">list_inventory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

NOTE: This service is in-development and can only be used by select partners. Please contact Candid Health to request access.

Retrieve a list of inventory records based on the provided filters. Each inventory record provides the latest invoiceable status of the associated claim.
The response is paginated, and the `page_token` can be used to retrieve subsequent pages. Initial requests should not include `page_token`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_ar.v_1.list_inventory()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `typing.Optional[dt.datetime]` — Timestamp to filter records since, inclusive
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of records to return, default is 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_ar.v_1.<a href="src/candid/resources/patient_ar/resources/v_1/client.py">itemize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

NOTE: This service is in-development and can only be used by select partners. Please contact Candid Health to request access.

Provides detailed itemization of invoice data for a specific claim.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_ar.v_1.itemize(
    claim_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**claim_id:** `ClaimId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PatientPayments V4
<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all patient payments satisfying the search criteria AND whose organization_id matches
the current organization_id of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**unattributed:** `typing.Optional[bool]` — returns payments with unattributed allocations if set to true
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[
    typing.Union[
        PatientTransactionSource, typing.Sequence[PatientTransactionSource]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PatientPaymentSortField]` — Defaults to payment_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created patient payment by its `patient_payment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.get(
    patient_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_payment_id:** `PatientPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new patient payment record and returns the newly created PatientPayment object.
The allocations can describe whether the payment is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.financials import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.create(
    amount_cents=1,
    patient_external_id="patient_external_id",
    allocations=[
        AllocationCreate(
            amount_cents=1,
            target=AllocationTargetCreate_ServiceLineById(
                value=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ),
        ),
        AllocationCreate(
            amount_cents=1,
            target=AllocationTargetCreate_ServiceLineById(
                value=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount_cents:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `PatientExternalId` 
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Sequence[AllocationCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient payment record matching the provided patient_payment_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.update(
    patient_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_payment_id:** `PatientPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the patient payment record matching the provided patient_payment_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.delete(
    patient_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_payment_id:** `PatientPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PatientRefunds V1
<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all patient refunds satisfying the search criteria AND whose organization_id matches
the current organization_id of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**unattributed:** `typing.Optional[bool]` — returns payments with unattributed allocations if set to true
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[
    typing.Union[
        PatientTransactionSource, typing.Sequence[PatientTransactionSource]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PatientRefundSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created patient refund by its `patient_refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.get(
    patient_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_refund_id:** `PatientRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new patient refund record and returns the newly created PatientRefund object.
The allocations can describe whether the refund is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.financials import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.create(
    amount_cents=1,
    patient_external_id="patient_external_id",
    allocations=[
        AllocationCreate(
            amount_cents=1,
            target=AllocationTargetCreate_ServiceLineById(
                value=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ),
        ),
        AllocationCreate(
            amount_cents=1,
            target=AllocationTargetCreate_ServiceLineById(
                value=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount_cents:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `PatientExternalId` 
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Sequence[AllocationCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReason]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient refund record matching the provided patient_refund_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.update(
    patient_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_refund_id:** `PatientRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReasonUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the patient refund record matching the provided patient_refund_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.delete(
    patient_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_refund_id:** `PatientRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PayerPlanGroups V1
<details><summary><code>client.payer_plan_groups.v_1.<a href="src/candid/resources/payer_plan_groups/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all payer plan groups matching filter criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payer_plan_groups.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_group_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[typing.Union[PayerUuid, typing.Sequence[PayerUuid]]]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[PayerId, typing.Sequence[PayerId]]]` 
    
</dd>
</dl>

<dl>
<dd>

**plan_type:** `typing.Optional[
    typing.Union[SourceOfPaymentCode, typing.Sequence[SourceOfPaymentCode]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_plan_group_id:** `typing.Optional[
    typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. Cannot exc
    
</dd>
</dl>

<dl>
<dd>

**sort_by_similarity:** `typing.Optional[str]` 

If this property is passed, the results will be ordered by those that contain a payer_id, payer_name, plan_group_name, or
payer_address most similar to the value passed. This will take precedence over the sort and sort_direction properties. This
will always sort in order of most similar to least similar.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PayerPlanGroupSortField]` — Defaults to plan_group_name. If sort_by_similarity is passed, that sort will takes precedence over this property.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to ascending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payer_plan_groups.v_1.<a href="src/candid/resources/payer_plan_groups/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a plan group with a given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payer_plan_groups.v_1.get(
    payer_plan_group_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_plan_group_id:** `PayerPlanGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payer_plan_groups.v_1.<a href="src/candid/resources/payer_plan_groups/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a payer plan group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import SourceOfPaymentCode
from candid.resources.payer_plan_groups.resources.v_1 import (
    MutablePayerPlanGroup,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payer_plan_groups.v_1.create(
    request=MutablePayerPlanGroup(
        plan_group_name="plan_group_name",
        payer_uuid=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        plan_type=SourceOfPaymentCode.SELF_PAY,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutablePayerPlanGroup` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payer_plan_groups.v_1.<a href="src/candid/resources/payer_plan_groups/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update any of the fields on a payer plan group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import SourceOfPaymentCode
from candid.resources.payer_plan_groups.resources.v_1 import (
    MutablePayerPlanGroup,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payer_plan_groups.v_1.update(
    payer_plan_group_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=MutablePayerPlanGroup(
        plan_group_name="plan_group_name",
        payer_uuid=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        plan_type=SourceOfPaymentCode.SELF_PAY,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_plan_group_id:** `PayerPlanGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutablePayerPlanGroup` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payer_plan_groups.v_1.<a href="src/candid/resources/payer_plan_groups/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks the payer plan group as deactivated
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payer_plan_groups.v_1.deactivate(
    payer_plan_group_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_plan_group_id:** `PayerPlanGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payers V3
<details><summary><code>client.payers.v_3.<a href="src/candid/resources/payers/resources/v_3/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payers.v_3.get(
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuid:** `PayerUuid` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payers.v_3.<a href="src/candid/resources/payers/resources/v_3/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payers.v_3.get_all(
    limit=100,
    search_term="john",
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payers V4
<details><summary><code>client.payers.v_4.<a href="src/candid/resources/payers/resources/v_4/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payers.v_4.get(
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuid:** `PayerUuid` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payers.v_4.<a href="src/candid/resources/payers/resources/v_4/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payers.v_4.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ServiceLines V2
<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import ServiceLineUnits
from candid.resources.service_lines.resources.v_2 import (
    ServiceLineCreateStandalone,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.create(
    request=ServiceLineCreateStandalone(
        procedure_code="procedure_code",
        quantity="quantity",
        units=ServiceLineUnits.MJ,
        claim_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ServiceLineCreateStandalone` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">create_universal</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import ServiceLineUnits
from candid.resources.service_lines.resources.v_2 import (
    UniversalServiceLineCreateStandalone,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.create_universal(
    request=UniversalServiceLineCreateStandalone(
        quantity="quantity",
        units=ServiceLineUnits.MJ,
        claim_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UniversalServiceLineCreateStandalone` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">update_universal</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.service_lines.resources.v_2 import (
    UniversalServiceLineUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.update_universal(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=UniversalServiceLineUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UniversalServiceLineUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.service_lines.resources.v_2 import ServiceLineUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.update(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ServiceLineUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ServiceLineUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.delete(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Superbills V1
<details><summary><code>client.superbills.v_1.<a href="src/candid/resources/superbills/resources/v_1/client.py">create_superbill</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.superbills.v_1.create_superbill(
    patient_external_id="patient_external_id",
    date_range_min=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    date_range_max=datetime.date.fromisoformat(
        "2023-01-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_external_id:** `PatientExternalId` — Empty string not allowed
    
</dd>
</dl>

<dl>
<dd>

**date_range_min:** `dt.date` — Minimum (inclusive) date selected for the superbill
    
</dd>
</dl>

<dl>
<dd>

**date_range_max:** `dt.date` — Maximum (inclusive) date selected for the superbill
    
</dd>
</dl>

<dl>
<dd>

**pay_to_address:** `typing.Optional[StreetAddressShortZip]` — Address that will be displayed on the superbill as the 'Pay to' Address. If not provided this value will be set from available encounter data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks V3
<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">get_actions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.get_actions(
    task_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `TaskId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[str]` — Only return tasks with categories that match one in this comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**updated_since:** `typing.Optional[dt.datetime]` — Only return tasks updated on or after this date-time
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `typing.Optional[EncounterId]` — Only return tasks associated with this encounter
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` — Query tasks by encounter_id, claim_id, task_id, or external_id
    
</dd>
</dl>

<dl>
<dd>

**assigned_to_id:** `typing.Optional[UserId]` — Only return tasks assigned to this user
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` — The minimum date of service for the linked encounter
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` — The maximum date of service for the linked encounter
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npi:** `typing.Optional[str]` — The NPI of the billing provider associated with the task's claim
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[TaskSortOptions]` — Defaults to updated_at:desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.get(
    task_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `TaskId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.tasks.resources.commons import TaskType
from candid.resources.tasks.resources.v_3 import TaskCreateV3

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.create(
    request=TaskCreateV3(
        encounter_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        task_type=TaskType.CUSTOMER_DATA_REQUEST,
        description="description",
        work_queue_id="work_queue_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TaskCreateV3` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.tasks.resources.v_3 import TaskUpdateV3

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.update(
    task_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=TaskUpdateV3(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `TaskId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TaskUpdateV3` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WriteOffs V1
<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all write-offs satisfying the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[WriteOffSortField]` — Defaults to write_off_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**account_types:** `typing.Optional[typing.Union[AccountType, typing.Sequence[AccountType]]]` — Filters the returned values to include only the provided account types.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created write off by its `write_off_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.get(
    write_off_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**write_off_id:** `WriteOffId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one or many write-offs applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.write_offs.resources.v_1 import (
    PatientWriteOffReason,
    WriteOffCreate_Patient,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.create(
    write_offs=[
        WriteOffCreate_Patient(
            write_off_timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            write_off_reason=PatientWriteOffReason.SMALL_BALANCE,
            service_line_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            amount_cents=1,
        ),
        WriteOffCreate_Patient(
            write_off_timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            write_off_reason=PatientWriteOffReason.SMALL_BALANCE,
            service_line_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            amount_cents=1,
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**write_offs:** `typing.Sequence[WriteOffCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">revert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reverts a write off given a `write_off_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.revert(
    write_off_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**write_off_id:** `WriteOffId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">revert_insurance_balance_adjustment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reverts an Insurance Balance Adjustment given an `adjustment_id`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.revert_insurance_balance_adjustment(
    adjustment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**adjustment_id:** `AdjustmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">revert_era_originated_insurance_balance_adjustment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reverts an ERA-originated Insurance Balance Adjustment given an `adjustment_id`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.revert_era_originated_insurance_balance_adjustment(
    adjustment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**adjustment_id:** `AdjustmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Appointments V1
<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an appointment.  VersionConflictError is returned when the placer_appointment_id is already in use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.appointments.resources.v_1 import (
    MutableAppointment,
    Service,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.create(
    request=MutableAppointment(
        patient_id="patient_id",
        start_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        service_duration=1,
        services=[Service(), Service()],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableAppointment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">get_visits</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all Visits within a given time range. The return list is ordered by start_time ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.get_visits()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[SortFieldString]` — Defaults to appointment.start_time.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to ascending.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[FilterQueryString]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an appointment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an appointment along with it's full history.  The return list is ordered by version ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.get_history(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an appointment. The path must contain the next version number to prevent race conditions. For example, if the current version of the appointment is n, you will need to send a request to this endpoint with `/{id}/n+1` to update the appointment. Updating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.appointments.resources.v_1 import (
    MutableAppointment,
    Service,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.update(
    id="id",
    version="version",
    request=MutableAppointment(
        patient_id="patient_id",
        start_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        service_duration=1,
        services=[Service(), Service()],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableAppointment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans up to 100 appointment updates.  The since query parameter is inclusive, and the result list is ordered by updatedAt ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.scan(
    since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets an appointment as deactivated.  The path must contain the most recent version to prevent race conditions.  Deactivating historic versions is not supported. Subsequent updates via PUT to the appointment will "reactivate" the appointment and set the deactivated flag to false.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.deactivate(
    id="id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Coverages V1
<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new Coverage. A Coverage provides the high-level identifiers and descriptors of a specific insurance plan for a specific individual - typically the information you can find on an insurance card. Additionally a coverage will include detailed benefits information covered by the specific plan for the individual.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.common import (
    HumanName,
    NameUse,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    CoverageStatus,
    InsurancePlan,
    MutableCoverage,
    Subscriber,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.create(
    request=MutableCoverage(
        status=CoverageStatus.ACTIVE,
        subscriber=Subscriber(
            name=HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
            biological_sex=Sex.FEMALE,
        ),
        relationship=Relationship.SELF,
        patient="patient",
        insurance_plan=InsurancePlan(
            member_id="member_id",
            payer_id="payer_id",
            payer_name="payer_name",
        ),
        verified=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableCoverage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Coverage. The path must contain the next version number to prevent race conditions. For example, if the current version of the coverage is n, you will need to send a request to this endpoint with `/{id}/n+1` to update the coverage. Updating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.common import (
    HumanName,
    NameUse,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    CoverageStatus,
    InsurancePlan,
    MutableCoverage,
    Subscriber,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.update(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    version="version",
    request=MutableCoverage(
        status=CoverageStatus.ACTIVE,
        subscriber=Subscriber(
            name=HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
            biological_sex=Sex.FEMALE,
        ),
        relationship=Relationship.SELF,
        patient="patient",
        insurance_plan=InsurancePlan(
            member_id="member_id",
            payer_id="payer_id",
            payer_name="payer_name",
        ),
        verified=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableCoverage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_multi_paginated</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a page of Coverages based on the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_multi_paginated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_plan_group_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Must be between 0 and 1000. Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

gets a specific Coverage
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a coverage along with it's full history.  The return list is ordered by version ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_history(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Coverages based on the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans up to 100 coverage updates. The since query parameter is inclusive, and the result list is ordered by updatedAt ascending.

**Polling Pattern:**
To continuously poll for updates without gaps:
1. Make your initial request with a `since` timestamp (e.g., `since=2020-01-01T13:00:00.000Z`)
2. The API returns up to 100 coverage records, sorted by `updated_at` ascending
3. Find the `updated_at` value from the last record in the response
4. Use that `updated_at` value as the `since` parameter in your next request
5. Repeat steps 2-4 to ingest updates until you receive an empty list

**Important Notes:**
- The `since` parameter is inclusive, so you may receive the last record from the previous batch again (you can deduplicate by ID and version)
- All coverage records include `updated_at`, `id`, `version`, `deactivated`, and `updating_user` fields for tracking changes
- Timestamps have millisecond resolution for precise ordering
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.scan(
    since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">batch_update_ppg</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finds all coverages associated with the given ppg_id and updates the ppg_fields for each coverage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    NetworkType,
    PayerPlanGroupFields,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.batch_update_ppg(
    ppg_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=PayerPlanGroupFields(
        payer_plan_group_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        payer_id="payer_id",
        payer_name="payer_name",
        plan_type=NetworkType.SELF_PAY,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ppg_id:** `PayerPlanGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PayerPlanGroupFields` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">check_eligibility</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an eligibility check. Returns the metadata of the check if successfully initiated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    ServiceTypeCode,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.check_eligibility(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_code=ServiceTypeCode.MEDICAL_CARE,
    date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    npi="npi",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**service_code:** `ServiceTypeCode` 
    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `dt.date` 
    
</dd>
</dl>

<dl>
<dd>

**npi:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_eligibility</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the eligibility of a patient for a specific coverage if successful.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_eligibility(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    check_id="check_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**check_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter EligibilityChecks V1
<details><summary><code>client.pre_encounter.eligibility_checks.v_1.<a href="src/candid/resources/pre_encounter/resources/eligibility_checks/resources/v_1/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends real-time eligibility checks to payers through Stedi.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    MemberInfo,
)
from candid.resources.pre_encounter.resources.eligibility_checks.resources.v_1 import (
    EligibilityRequest,
    IndividualProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.post(
    request=EligibilityRequest(
        payer_id="payer_id",
        provider=IndividualProvider(
            npi="npi",
        ),
        subscriber=MemberInfo(
            first_name="first_name",
            last_name="last_name",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EligibilityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.eligibility_checks.v_1.<a href="src/candid/resources/pre_encounter/resources/eligibility_checks/resources/v_1/client.py">batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a batch of eligibility checks to payers through Stedi.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    MemberInfo,
)
from candid.resources.pre_encounter.resources.eligibility_checks.resources.v_1 import (
    EligibilityRequest,
    IndividualProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.batch(
    request=[
        EligibilityRequest(
            payer_id="payer_id",
            provider=IndividualProvider(
                npi="npi",
            ),
            subscriber=MemberInfo(
                first_name="first_name",
                last_name="last_name",
            ),
        ),
        EligibilityRequest(
            payer_id="payer_id",
            provider=IndividualProvider(
                npi="npi",
            ),
            subscriber=MemberInfo(
                first_name="first_name",
                last_name="last_name",
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Sequence[EligibilityRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.eligibility_checks.v_1.<a href="src/candid/resources/pre_encounter/resources/eligibility_checks/resources/v_1/client.py">poll_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Polls the status of a batch eligibility check.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.poll_batch(
    batch_id="batch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.eligibility_checks.v_1.<a href="src/candid/resources/pre_encounter/resources/eligibility_checks/resources/v_1/client.py">payer_search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for payers that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.payer_search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.eligibility_checks.v_1.<a href="src/candid/resources/pre_encounter/resources/eligibility_checks/resources/v_1/client.py">recommendation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets recommendation for eligibility checks based on the request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.recommendation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filters:** `typing.Optional[FilterQueryString]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.eligibility_checks.v_1.<a href="src/candid/resources/pre_encounter/resources/eligibility_checks/resources/v_1/client.py">create_recommendation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an eligibiilty recommendation based on the request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.eligibility_checks.resources.v_1 import (
    EligibilityRecommendationPatientInfo,
    EligibilityRecommendationPayload_MedicareAdvantage,
    MedicareAdvantageRecommendationPayload,
    PostEligibilityRecommendationRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.create_recommendation(
    request=PostEligibilityRecommendationRequest(
        eligibility_check_id="eligibility_check_id",
        patient=EligibilityRecommendationPatientInfo(),
        recommendation=EligibilityRecommendationPayload_MedicareAdvantage(
            payload=MedicareAdvantageRecommendationPayload(),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostEligibilityRecommendationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Images V1
<details><summary><code>client.pre_encounter.images.v_1.<a href="src/candid/resources/pre_encounter/resources/images/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an image.  VersionConflictError is returned if a front or back of this coverage already exists.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.images.resources.v_1 import (
    ImageStatus,
    MutableImage,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.images.v_1.create(
    request=MutableImage(
        file_name="file_name",
        display_name="display_name",
        file_type="file_type",
        status=ImageStatus.PENDING,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableImage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.images.v_1.<a href="src/candid/resources/pre_encounter/resources/images/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an image by imageId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.images.v_1.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `ImageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.images.v_1.<a href="src/candid/resources/pre_encounter/resources/images/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an Image.  The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.images.resources.v_1 import (
    ImageStatus,
    MutableImage,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.images.v_1.update(
    id="id",
    version="version",
    request=MutableImage(
        file_name="file_name",
        display_name="display_name",
        file_type="file_type",
        status=ImageStatus.PENDING,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `ImageId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableImage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.images.v_1.<a href="src/candid/resources/pre_encounter/resources/images/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets an Image as deactivated.  The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.images.v_1.deactivate(
    id="id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `ImageId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.images.v_1.<a href="src/candid/resources/pre_encounter/resources/images/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for images that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.images.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**coverage_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Lists V1
<details><summary><code>client.pre_encounter.lists.v_1.<a href="src/candid/resources/pre_encounter/resources/lists/resources/v_1/client.py">get_patient_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets patients with dependent objects for patients that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.lists.v_1.get_patient_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[SortFieldString]` — Defaults to patient.updatedAt.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to ascending.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[FilterQueryString]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.lists.v_1.<a href="src/candid/resources/pre_encounter/resources/lists/resources/v_1/client.py">get_appointment_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for appointments that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.lists.v_1.get_appointment_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sort_field:** `typing.Optional[SortFieldString]` — Defaults to appointment.startTimestamp.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[FilterQueryString]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Notes V1
<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a note by NoteId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new note.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.notes.resources.v_1 import (
    MutableNote,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.create(
    request=MutableNote(
        value="value",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableNote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a note. The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.notes.resources.v_1 import (
    MutableNote,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.update(
    id="id",
    version="version",
    request=MutableNote(
        value="value",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableNote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a note as deactivated.  The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.deactivate(
    id="id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Patients V1
<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient.  VersionConflictError is returned when the patient's external ID is already in use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.common import (
    Address,
    AddressUse,
    ContactPoint,
    ContactPointUse,
    ExternalProvider,
    HumanName,
    NameUse,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.resources.patients.resources.v_1 import (
    Contact,
    FilingOrder,
    MutablePatient,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.create(
    request=MutablePatient(
        name=HumanName(
            family="family",
            given=["given", "given"],
            use=NameUse.USUAL,
        ),
        other_names=[
            HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
            HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
        ],
        birth_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        biological_sex=Sex.FEMALE,
        primary_address=Address(
            use=AddressUse.HOME,
            line=["line", "line"],
            city="city",
            state="state",
            postal_code="postal_code",
            country="country",
        ),
        other_addresses=[
            Address(
                use=AddressUse.HOME,
                line=["line", "line"],
                city="city",
                state="state",
                postal_code="postal_code",
                country="country",
            ),
            Address(
                use=AddressUse.HOME,
                line=["line", "line"],
                city="city",
                state="state",
                postal_code="postal_code",
                country="country",
            ),
        ],
        other_telecoms=[
            ContactPoint(
                value="value",
                use=ContactPointUse.HOME,
            ),
            ContactPoint(
                value="value",
                use=ContactPointUse.HOME,
            ),
        ],
        contacts=[
            Contact(
                relationship=[Relationship.SELF, Relationship.SELF],
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                ],
            ),
            Contact(
                relationship=[Relationship.SELF, Relationship.SELF],
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                ],
            ),
        ],
        general_practitioners=[
            ExternalProvider(
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
            ),
            ExternalProvider(
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
            ),
        ],
        filing_order=FilingOrder(
            coverages=[
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutablePatient` 
    
</dd>
</dl>

<dl>
<dd>

**skip_duplicate_check:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">create_with_mrn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient and hydrates their MRN with a pre-existing MRN.  Once this patient is created their MRN will not be editable. BadRequestError is returned when the MRN is greater than 20 characters. VersionConflictError is returned when the patient's external ID is already in use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.common import (
    Address,
    AddressUse,
    ContactPoint,
    ContactPointUse,
    ExternalProvider,
    HumanName,
    NameUse,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.resources.patients.resources.v_1 import (
    Contact,
    FilingOrder,
    MutablePatientWithMrn,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.create_with_mrn(
    request=MutablePatientWithMrn(
        mrn="mrn",
        name=HumanName(
            family="family",
            given=["given", "given"],
            use=NameUse.USUAL,
        ),
        other_names=[
            HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
            HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
        ],
        birth_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        biological_sex=Sex.FEMALE,
        primary_address=Address(
            use=AddressUse.HOME,
            line=["line", "line"],
            city="city",
            state="state",
            postal_code="postal_code",
            country="country",
        ),
        other_addresses=[
            Address(
                use=AddressUse.HOME,
                line=["line", "line"],
                city="city",
                state="state",
                postal_code="postal_code",
                country="country",
            ),
            Address(
                use=AddressUse.HOME,
                line=["line", "line"],
                city="city",
                state="state",
                postal_code="postal_code",
                country="country",
            ),
        ],
        other_telecoms=[
            ContactPoint(
                value="value",
                use=ContactPointUse.HOME,
            ),
            ContactPoint(
                value="value",
                use=ContactPointUse.HOME,
            ),
        ],
        contacts=[
            Contact(
                relationship=[Relationship.SELF, Relationship.SELF],
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                ],
            ),
            Contact(
                relationship=[Relationship.SELF, Relationship.SELF],
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                ],
            ),
        ],
        general_practitioners=[
            ExternalProvider(
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
            ),
            ExternalProvider(
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
            ),
        ],
        filing_order=FilingOrder(
            coverages=[
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutablePatientWithMrn` 
    
</dd>
</dl>

<dl>
<dd>

**skip_duplicate_check:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for patients that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mrn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[PatientSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to ascending.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">search_providers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for referring providers that match the query parameters.  The search is case-insensitive, supports fuzzy matching, and matches against provider name and NPI. The search criteria must be an alphanumeric string, and the search is limited to the first 20 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.search_providers(
    search_criteria="search_criteria",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_criteria:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get_by_mrn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient by mrn.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get_by_mrn(
    mrn="mrn",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mrn:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient along with it's full history.  The return list is ordered by version ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get_history(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient. The path must contain the next version number to prevent race conditions. For example, if the current version of the patient is n, you will need to send a request to this endpoint with `/{id}/n+1` to update the patient. Updating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.common import (
    Address,
    AddressUse,
    ContactPoint,
    ContactPointUse,
    ExternalProvider,
    HumanName,
    NameUse,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.resources.patients.resources.v_1 import (
    Contact,
    FilingOrder,
    MutablePatient,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.update(
    id="id",
    version="version",
    request=MutablePatient(
        name=HumanName(
            family="family",
            given=["given", "given"],
            use=NameUse.USUAL,
        ),
        other_names=[
            HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
            HumanName(
                family="family",
                given=["given", "given"],
                use=NameUse.USUAL,
            ),
        ],
        birth_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        biological_sex=Sex.FEMALE,
        primary_address=Address(
            use=AddressUse.HOME,
            line=["line", "line"],
            city="city",
            state="state",
            postal_code="postal_code",
            country="country",
        ),
        other_addresses=[
            Address(
                use=AddressUse.HOME,
                line=["line", "line"],
                city="city",
                state="state",
                postal_code="postal_code",
                country="country",
            ),
            Address(
                use=AddressUse.HOME,
                line=["line", "line"],
                city="city",
                state="state",
                postal_code="postal_code",
                country="country",
            ),
        ],
        other_telecoms=[
            ContactPoint(
                value="value",
                use=ContactPointUse.HOME,
            ),
            ContactPoint(
                value="value",
                use=ContactPointUse.HOME,
            ),
        ],
        contacts=[
            Contact(
                relationship=[Relationship.SELF, Relationship.SELF],
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                ],
            ),
            Contact(
                relationship=[Relationship.SELF, Relationship.SELF],
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                    Address(
                        use=AddressUse.HOME,
                        line=["line", "line"],
                        city="city",
                        state="state",
                        postal_code="postal_code",
                        country="country",
                    ),
                ],
            ),
        ],
        general_practitioners=[
            ExternalProvider(
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
            ),
            ExternalProvider(
                name=HumanName(
                    family="family",
                    given=["given", "given"],
                    use=NameUse.USUAL,
                ),
                telecoms=[
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                    ContactPoint(
                        value="value",
                        use=ContactPointUse.HOME,
                    ),
                ],
            ),
        ],
        filing_order=FilingOrder(
            coverages=[
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutablePatient` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a patient as deactivated.  The path must contain the most recent version plus 1 to prevent race conditions.  Deactivating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.deactivate(
    id="id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">reactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the deactivated flag for a patient.  The path must contain the most recent version plus 1 to prevent race conditions.  Reactivating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.reactivate(
    id="id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Patients based on the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mrn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_name_ordering:** `typing.Optional[str]` — A string that is used to order similar names in search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans up to 1000 patient updates. The since query parameter is inclusive, and the result list is ordered by updatedAt ascending.

**Polling Pattern:**
To continuously poll for updates without gaps:
1. Make your initial request with a `since` timestamp (e.g., `since=2020-01-01T13:00:00.000Z`)
2. The API returns 100 by default and up to 1000 patient records, sorted by `updated_at` ascending
3. Find the `updated_at` value from the last record in the response
4. Use that `updated_at` value as the `since` parameter in your next request
5. Repeat steps 2-4 to ingest updates until you receive an empty list

**Important Notes:**
- The `since` parameter is inclusive, so you may receive the last record from the previous batch again (you can deduplicate by ID and version)
- All patient records include `updated_at`, `id`, `version`, `deactivated`, and `updating_user` fields for tracking changes
- Timestamps have millisecond resolution for precise ordering
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.scan(
    since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Tags V1
<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a tag by TagId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `TagId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all tags. Defaults to page size of 1000.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new tag if it does not already exist, otherwise, returns the existing tag.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.tags.resources.v_1 import (
    MutableTag,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.create(
    request=MutableTag(
        value="value",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableTag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a tag. The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.tags.resources.v_1 import (
    MutableTag,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.update(
    id="id",
    version="version",
    request=MutableTag(
        value="value",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `TagId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableTag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a tag as deactivated.  The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.deactivate(
    id="id",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `TagId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Diagnoses
<details><summary><code>client.diagnoses.<a href="src/candid/resources/diagnoses/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new diagnosis for an encounter
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.diagnoses import (
    DiagnosisTypeCode,
    StandaloneDiagnosisCreate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.diagnoses.create(
    request=StandaloneDiagnosisCreate(
        encounter_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        code_type=DiagnosisTypeCode.ABF,
        code="code",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `StandaloneDiagnosisCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.diagnoses.<a href="src/candid/resources/diagnoses/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the diagnosis record matching the provided `diagnosis_id`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.diagnoses.update(
    diagnosis_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**diagnosis_id:** `DiagnosisId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**code_type:** `typing.Optional[DiagnosisTypeCode]` — Typically, providers submitting claims to Candid are using ICD-10 diagnosis codes. If you are using ICD-10 codes, the primary diagnosis code listed on the claim should use the ABK code_type. If more than one diagnosis is being submitted on a claim, please use ABF for the rest of the listed diagnoses. If you are using ICD-9 diagnosis codes, use BK and BF for the principal and following diagnosis code(s) respectively.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 

Empty string not allowed.
Should be of the appropriate format for the provided `code_type`.
Must obey the ICD-10 format if an ICD-10 code_type is provided, specifically:
  - Letter
  - Digit
  - Digit or the letter `A` or `B`
  - (Optional) Period `.`
  - Up to 4 (or as few as 0) letters and digits
    
</dd>
</dl>

<dl>
<dd>

**present_on_admission_indicator:** `typing.Optional[YesNoIndicator]` 

For Institutional claims only.
A "Y" indicates that the onset occurred prior to admission to the hospital.
An "N" indicates that the onset did NOT occur prior to admission to the hospital.
A "U" indicates that it is unknown whether the onset occurred prior to admission to the hospital or not.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.diagnoses.<a href="src/candid/resources/diagnoses/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the diagnosis record associated with the provided `diagnosis_id`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.diagnoses.delete(
    diagnosis_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**diagnosis_id:** `DiagnosisId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ServiceFacility
<details><summary><code>client.service_facility.<a href="src/candid/resources/service_facility/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.service_facility import EncounterServiceFacilityUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_facility.update(
    service_facility_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=EncounterServiceFacilityUpdate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_facility_id:** `ServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EncounterServiceFacilityUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

