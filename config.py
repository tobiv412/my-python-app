import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLACHEMY_DATABASE_URI = 'mysql://root:' + SECRET_KEY + '@127.0.0.1/movie_db'
    DEBUG = True
    CSRF_ENABLED = True