import os
import logging
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask


# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class BaseConfig(object):

    def __init__(self, app: Flask):
        self.init_app(app)

    @classmethod
    def init_app(cls, app: Flask):
        app.config.from_object(cls)

    # # LOGGER
    # DEBUG = True
    # TESTING = True
    # APP_NAME = os.environ.get('APP_NAME', 'stuio-trend-subscriber')
    # APP_NAME_EXPORT = os.environ.get('APP_NAME_EXPORT', 'studio-trend-export')
    # LOGGING_FORMAT = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
    # ACCESS_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(message)s"
    # LOGGING_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"  # iso8601
    # LOGGING_PATH = '../logs'
    # EXPORT_LOGGING_PATH = 'logs'
    # LOGGING_LEVEL = logging.INFO

    # MYSQL
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db host')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'db user')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'db password')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'db database')
    MYSQL_POOL_SIZE = int(os.environ.get('MYSQL_POOL_SIZE', 5))
