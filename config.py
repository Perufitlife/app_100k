import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_fuerte'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
