"""Application configuration classes."""
import os


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
