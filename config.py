import os

class Config:
    '''
    parent class for configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:dan15done@localhost/blog'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Lets Blog!'
    SENDER_EMAIL = 'dmndan124@gmail.com'


    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    child class for production configurations
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# class TestConfig(Config):
#     # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:dan15done@localhost/blog'

class DevConfig(Config):
    '''
    child class for development configurations
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:dan15done@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
}