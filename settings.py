import os
import warnings

SESSION_CONFIGS = [
    dict(
        name='tourism_survey',
        display_name='Tourism Perceptions Survey',
        app_sequence=['tourism_survey'],
        num_demo_participants=3,
    ),
]

ROOMS = [
    dict(
        name='TourismSurvey',
        display_name='Tourism Survey',
    )
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'fr'

REAL_WORLD_CURRENCY_CODE = 'XPF'
USE_POINTS = False

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = os.environ.get("OTREE_ADMIN_PASSWORD")

OTREE_AUTH_LEVEL = os.environ.get('OTREE_AUTH_LEVEL', None)


match os.environ.get("OTREE_REST_KEY"):
    case "" | None:
        SECRET_KEY = "5903222485487"
        warnings.warn(
            "Environmental variable for REST key not set. Using default.",
            stacklevel=1,
        )
    case _:
        SECRET_KEY = os.environ.get("OTREE_REST_KEY")

# Database credentials
if (
    os.environ.get("POSTGRES_PASSWORD")
    and os.environ.get("POSTGRES_USER")
    and os.environ.get("POSTGRES_DB")
):
    os.environ["DATABASE_URL"] = (
        "postgres://"
        + os.environ.get("POSTGRES_USER")
        + ":"
        + os.environ.get("POSTGRES_PASSWORD")
        + "@db/"
        + os.environ.get("POSTGRES_DB")
    )
elif (
    os.environ.get("POSTGRES_PASSWORD")
    or os.environ.get("POSTGRES_USER")
    or os.environ.get("POSTGRES_DB")
):
    warnings.warn(
        """To use Postgres, the environmental variables DATABASE_URL,
        POSTGRES_USER, and POSTGRES_DB must all be set""",
        stacklevel=1,
    )
elif os.environ.get("DATABASE_URL"):
    pass
else:
    warnings.warn(
        """Using SQLite, because no Postgres credentials are specified. This is
        fine for local use, but can lead to performance degradation in
        production.""",
        stacklevel=1,
    )
