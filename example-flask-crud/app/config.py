import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Example DATABASE_URL: mysql+pymysql://username:password@host:3306/dbname
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False