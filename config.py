import os

class Config:
    '''
    parent class for configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:dan15done@localhost/blog'


class ProdConfig(Config):
    '''
    child class for production configurations
    '''
    pass

class DevConfig(Config):
    '''
    child class for development configurations
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}