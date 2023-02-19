from . import Config


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'test-database',
        'host': 'mongo',
        'port': 27017
    }
    CELERY_BROKER_URL = 'redis://redis:6379/1'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/1'