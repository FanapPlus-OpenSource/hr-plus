from flask import Flask, request
from app.db import initialize_db
from app.api import blueprint as api_blueprint
from users.commands.create_superuser import bp as superuser_command_bp

# Import extensions
from app.extensions import cors, jwt, ma

from app.settings import config_by_name


def create_app(config_name='default'):
    """
    Create a Flask application using the app factory pattern.

    :param config_name: Config name
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_by_name[config_name])

    app.config['MONGODB_SETTINGS'] = {
        'host': app.config['MONGO_URI'],
    }

    app.config['JWT_ERROR_MESSAGE_KEY'] = 'message'

    register_extensions(app)

    middleware(app)

    # Blueprints
    app.register_blueprint(superuser_command_bp)
    app.register_blueprint(api_blueprint)

    return app


def register_extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    initialize_db(app)
    ma.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    return None


def middleware(app):
    """
    Register 0 or more middleware (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # Swap request.remote_addr with the real IP address even if behind a proxy.

    return None
