# Test configuration for the Flask application
import os
import tempfile
from datetime import timedelta

class TestConfig:
    TESTING = True
    SECRET_KEY = "testsecretkey"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    WTF_CSRF_ENABLED = False
