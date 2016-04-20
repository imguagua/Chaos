##-*- coding: utf-8 -*-
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'harry harry is guagua'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:sasa@localhost/chaos-dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:sasa@localhost:3306/chaos-test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:sasa@localhost:3306/chaos-test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

 

config = {
     'development': DevelopmentConfig,
     'testing': TestingConfig,
     'production': ProductionConfig,
     'default': DevelopmentConfig
}
