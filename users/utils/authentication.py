# Validations with Marshmallow
from marshmallow import Schema, fields
from marshmallow.validate import Length


class LoginSchema(Schema):
    """ /auth/login [POST]

    Parameters:
    - Email
    - Password (Str)
    """

    email = fields.Email(
        required=True,
        error_messages={"required": "ایمیل نمی‌تواند خالی باشد.", "invalid": "آدرس ایمیل صحیح نمی‌باشد."},
        validate=[
            Length(max=64, error='باید حداکثر {max} کاراکتر داشته باشد.')
        ]
    )
    password = fields.Str(
        required=True,
        error_messages={"required": "رمز عبور نمی‌تواند خالی باشد."},
        validate=[
            Length(min=8, max=128,  error='باید حداقل {min} کاراکتر و حداکثر {max} کاراکتر داشته باشد.')
        ]
    )