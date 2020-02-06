import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Development(object):
    # DATABASE_URL -> Variable de entorno del sistema
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test(object):
    # DATABASE_URL -> Variable de entorno del sistema
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(object):
    # DATABASE_URL -> Variable de entorno del sistema
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_mode(mode):
    if mode == "prod":
        return Production
    elif mode == "test":
        return Test
    else:
        return Development
