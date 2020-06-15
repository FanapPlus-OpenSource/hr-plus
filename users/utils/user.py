# Validations with Marshmallow
from marshmallow import Schema, fields
from marshmallow.validate import Length
from app.custom_validators import Unique
from users.models.user import User


class CreateSchema(Schema):
    """ /auth/register [POST]

    Parameters:
    - First Name (Str)
    - Last Name (Str)
    - Email (Str)
    - Is Active (Bool)
    - Is Staff (Bool)
    - Date Joined (Datetime)
    - Password (Str)
    """

    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email(
        required=True,
        error_messages={"required": "ایمیل نمی‌تواند خالی باشد.", "invalid": "آدرس ایمیل صحیح نمی‌باشد."},
        validate=[
            Length(max=64, error='باید حداکثر {max} کاراکتر داشته باشد.'),
            Unique(User, 'email', error='آدرس ایمیل قبلا گرفته شده.')
        ]
    )
    is_active = fields.Boolean(
        default=False,
        error_messages={"invalid": "مقدار صحیح نمی‌باشد."}
    )
    is_staff = fields.Boolean(
        default=False,
        error_messages={"invalid": "مقدار صحیح نمی‌باشد."}
    )
    date_joined = fields.DateTime(
        required=True,
        error_messages={"required": "ایمیل نمی‌تواند خالی باشد.", "invalid": "مقدار صحیح نمی‌باشد.",
                        "format": "فرمت تاریخ صحیح نمی‌باشد."},
    )
    password = fields.Str(
        required=True,
        error_messages={"required": "رمز عبور نمی‌تواند خالی باشد."},
        validate=[
            Length(min=8, max=128, error='باید حداقل {min} کاراکتر و حداکثر {max} کاراکتر داشته باشد.')
        ]
    )
