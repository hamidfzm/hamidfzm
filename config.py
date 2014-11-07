# -*- coding: utf-8 -*-

# python import
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = '+%2@@xc65t4re5bg4l$egx1e55b(*_oexmre@674^em!phgd8d'
    WTF_CSRF_SECRET_KEY = 'ldfzbn$5+(hrt0h843(qu=n8x11x&f4a0hwh=2ircc)@p4jhup'


    FLASKY_MAIL_SUBJECT_PREFIX = '[Hamid FzM]'
    FLASKY_MAIL_SENDER = 'Hamid FzM <mail@hamidfzm.ir>'
    FLASKY_ADMIN = 'Hamid FzM'

    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'UTC+03:30'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MINIFY_PAGE = False


class ProductionConfig(Config):
    DEBUG = False
    MINIFY_PAGE = True


config = {'development': DevelopmentConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}