import os
from dotenv import load_dotenv

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


class Config:
    DEBUG = os.getenv('DEBUG_VALUE') == 'TRUE'
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')  # refers to application_top
    LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

    MONGO_URI = os.getenv('MONGO_URI')

    SERVER_NAME = os.getenv('SERVER_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_TOKEN_EXPIRE_SECONDS'))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRE_SECONDS'))

    SESSION_COOKIE_NAME = 'hr_plus'
    SESSION_COOKIE_DOMAIN = False if os.getenv('SESSION_COOKIE_DOMAIN') == 'FALSE' else os.getenv(
        'SESSION_COOKIE_DOMAIN')
    SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_HTTPONLY') == 'TRUE'
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE') == 'TRUE'
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SECURE')


class TestConfig(Config):
    DEBUG = True
    TESTING = True


config_by_name = dict(
    testing=TestConfig,
    default=Config,
)
