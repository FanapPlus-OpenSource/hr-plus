from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token

from app.utils import message, err_resp, internal_err_resp
from users.models.user import User
from users.schemas.user import UserSchema

user_schema = UserSchema()


class AuthService:
    @staticmethod
    def login(data):
        # Assign vars
        email = data["email"]
        password = data["password"]

        try:
            # Fetch user data
            if not (user := User.objects(email=email).get_not_trashed().first()):
                return err_resp(
                    "ایمیل یا رمزعبور صحیح نمی‌باشد.",
                    "credentials_mismatch",
                    401,
                )

            elif user and user.check_password(password):
                user_info = user_schema.dump(user)

                access_token = create_access_token(identity=str(user.id))
                refresh_token = create_refresh_token(identity=str(user.id))

                resp = message(True, "ورود موفقیت آمیز.")
                resp["access_token"] = access_token
                resp["refresh_token"] = refresh_token
                resp["user"] = user_info

                return resp, 200

            return err_resp(
                "ایمیل یا رمزعبور صحیح نمی‌باشد.", "credentials_mismatch", 401
            )

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
