## -*- coding: utf-8 -*-
# project/config.py

import os
import vars
path = os.path.join('.', os.path.dirname(__file__), 'app/static/js/sijax/')

class BaseConfig(object):
    MAIL_USERNAME                       = os.environ['mail']
    MAIL_PASSWORD                       = os.environ['mailPass'].replace("'","")
    MAIL_DEFAULT_SENDER                 = os.environ['mailSender']
    MAIL_SERVER                         = os.environ['mailServer']
    MAIL_PORT                           = int(os.environ['mailPort'])
    MAIL_USE_SSL                        = bool(os.environ['mailSSL'])
    SECRET_KEY                          = os.environ['secretKey']
    SIJAX_STATIC_PATH                   = path
    SIJAX_JSON_URI                      = 'app/static/js/sijax/json2.js'
    JSON_AS_ASCII                       = False
    TEMPLATES_AUTO_RELOAD               = True

    # Flask security
    SECURITY_TRACKABLE                  = True
    SECURITY_REGISTERABLE               = True
    SECURITY_RECOVERABLE                = True
    SECURITY_CHANGEABLE                 = True
    SECURITY_FLASH_MESSAGES             = True
    SECURITY_CONFIRMABLE                = True
    SECURITY_PASSWORD_HASH              = 'bcrypt'
    SECURITY_PASSWORD_SALT              = 'RANDOM_SALT_VALUE'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI             = os.environ['dev-db']
    SQLALCHEMY_TRACK_MODIFICATIONS      = True
    MINIFY_PAGE                         = False

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI             = os.environ['prod-db']
    SQLALCHEMY_TRACK_MODIFICATIONS      = False
    MINIFY_PAGE                         = True
