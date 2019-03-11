import os

DEBUG = True

SECRET_KEY = os.urandom(24)


# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
USERNAME = 'wangpb'
PASSWORD = 'xiaobobo'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlkt_demo'

DB_URI = "{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS=False


