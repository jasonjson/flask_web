import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '267299877045537',
        'secret': '52f80ebf78a4a34498bb7f392d4fb9a9'
    }
}

# administrator list
ADMINS = ['jason.yyliu@gmail.com']

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
