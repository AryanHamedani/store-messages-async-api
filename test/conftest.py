import pytest
from app import create_app, db
from app.models import Message

@pytest.fixture(scope='module')
def test_app():
    app = create_app('testing')
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def test_client(test_app):
    with test_app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table

    # Insert user data
    message = Message(message='Test message')
    message.save()

    yield # This is where the testing happens!

    # Drop the database table after the tests run
    Message.drop_table()