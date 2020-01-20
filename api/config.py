import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # DATABASE_URL -> Variable de entorno del sistema
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False