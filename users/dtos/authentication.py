from flask_restx import Namespace, fields


class AuthDto:
    api = Namespace("Authentication", description="Authenticate and receive tokens.")

    user_obj = api.model(
        "User object",
        {
            "id": fields.String,
            "first_name": fields.String,
            "last_name": fields.String,
            "full_name": fields.String,
            "date_joined": fields.DateTime,
            "email": fields.String,
            "is_superuser": fields.Boolean,
            "is_active": fields.Boolean,
            "is_staff": fields.Boolean,
        },
    )

    auth_login = api.model(
        "Login data",
        {
            "email": fields.String(required=True),
            "password": fields.String(required=True),
        },
    )

    auth_refresh = api.parser()
    auth_refresh.add_argument('Authorization', type=str, location='headers')

    auth_success = api.model(
        "Auth success response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "access_token": fields.String,
            "refresh_token": fields.String,
            "user": fields.Nested(user_obj),
        },
    )

    refresh_success = api.model(
        "Refresh success response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "access_token": fields.String,
        },
    )
