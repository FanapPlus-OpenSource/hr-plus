from pytz import timezone
import dateutil.parser
from flask import current_app
from app.utils import validation_error

from app.utils import message, internal_err_resp
from users.models.user import User
from users.schemas.user import UserSchema

user_schema = UserSchema()


class UserService:

    @staticmethod
    def create_superuser(data):
        return UserService.__add_user(data, True)

    @staticmethod
    def create(data):
        return UserService.__add_user(data, False)

    @staticmethod
    def __add_user(data, is_superuser=False):
        # Required values
        email = data["email"]
        password = data["password"]
        date_joined = data["date_joined"]

        if type(date_joined) is str:
            date_joined = dateutil.parser.parse(date_joined)
            date_joined = date_joined.astimezone(timezone('UTC'))

        # Optional
        data_first_name = data.get("first_name")
        data_last_name = data.get("last_name")
        data_is_active = data.get("is_active")
        data_is_staff = data.get("is_staff")

        # Check if the email is taken
        if User.objects(email=email).first() is not None:
            return validation_error(False, {"email": ["این ایمیل قبلا ثبت شده است."]}), 422

        try:
            new_user = User(
                first_name=data_first_name,
                last_name=data_last_name,
                date_joined=date_joined,
                email=email,
                is_active=data_is_active,
                is_staff=data_is_staff,
                is_superuser=is_superuser,
            )

            new_user.set_password_hash(password)

            new_user.save()

            # Load the new user's info
            user_info = user_schema.dump(new_user)

            resp = message(True, "کاربر با موفقیت ایجاد شد.")
            resp["user"] = user_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
