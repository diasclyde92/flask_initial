import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'T#1nKpractice^')
    DEBUG = False


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {'DB': 'test_pro'}
    SECRET_KEY = 'flask+mongoengine=<3'


class TestingConfig(Config):
    DEBUG = False
    TESTING = True

    MONGODB_SETTINGS = {'DB': 'test', 'USERNAME': 'test', 'PASSWORD': 'test'}
    SECRET_KEY = 'flask+mongoengine=<3'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {'DB': 'test', 'USERNAME': 'test_prod', 'PASSWORD': '7014e2e7'}
    SECRET_KEY = 'T#1nKtest^-9800-'


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY