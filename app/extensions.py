"""
Extensions module

Each extension is initialized when app is created.
"""

from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_marshmallow import Marshmallow

cors = CORS()

jwt = JWTManager()
ma = Marshmallow()
