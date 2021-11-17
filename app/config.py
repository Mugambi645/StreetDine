import os
class Config:
    '''General configuration class'''
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
        '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pato:flower2@localhost/streetdine'
    DEBUG = True
    

config_options = {
    'development':DevConfig,
    'production':ProdConfig,

}
