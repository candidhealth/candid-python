# This file was auto-generated by Fern from our API Definition.

import typing

PatientPaymentSource = typing.Union[
    typing.Literal[
        "MANUAL_ENTRY",
        "CHARGEBEE_PAYMENTS",
        "CHARGEBEE MANUALLY VOIDED BY CANDID",
        "CHARGEBEE_REFUNDS",
        "SQUARE_REFUNDS",
        "SQUARE_PAYMENTS",
        "STRIPE_CHARGES",
        "STRIPE_REFUNDS",
        "ELATION_PAYMENTS",
    ],
    typing.Any,
]
