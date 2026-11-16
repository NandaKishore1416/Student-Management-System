import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-only-change-me')
