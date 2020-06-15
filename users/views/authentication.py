from flask import request
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token
from flask_restx import Resource

from app.utils import validation_error

# Auth modules
from users.services.authentication import AuthService
from users.dtos.authentication import AuthDto
from users.utils.authentication import LoginSchema

api = AuthDto.api
auth_success = AuthDto.auth_success
refresh_success = AuthDto.refresh_success

login_schema = LoginSchema()


@api.route("/login")
class AuthLogin(Resource):
    """ User login endpoint
    User registers then receives the user's information and access_token
    """

    auth_login = AuthDto.auth_login

    @api.doc(
        "Auth login",
        responses={
            200: ("Logged in", auth_success),
            422: "Validations failed.",
            401: "Incorrect password or incomplete credentials.",
        },
    )
    @api.expect(auth_login)
    def post(self):
        """ Login using email and password """
        # Grab the json data
        login_data = request.get_json()

        # Validate data
        if (errors := login_schema.validate(login_data)):
            return validation_error(False, errors), 422

        return AuthService.login(login_data)


@api.route("/refresh")
class AuthRefresh(Resource):
    """ User login endpoint
    User registers then receives the user's information and access_token
    """

    auth_refresh = AuthDto.auth_refresh

    @api.doc(
        "Auth Refresh Token",
        responses={
            200: ("Refresh", refresh_success),
            401: "Invalid Token.",
        },
    )
    @api.expect(auth_refresh)
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        res = {
            'status': True,
            'message': 'توکن با موفقیت بروزرسانی شد.',
            'access_token': create_access_token(identity=current_user),
        }
        return res, 200
