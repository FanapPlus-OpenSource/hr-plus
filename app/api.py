from flask import Blueprint
from flask_restx import Api
from users import auth_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='HR Plus APIs',
          version='1.0',
          description='APIs for handling HR Plus tasks',
          doc='/docs'
          )

# API namespaces
api.add_namespace(auth_ns, '/auth')
