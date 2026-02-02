import pytest
from app import app
from models import db
from test_config import TestConfig

@pytest.fixture
def client():
    app.config.from_object(TestConfig)
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        
    with app.app_context():
        db.drop_all()

@pytest.fixture
def runner():
    return app.test_cli_runner()
