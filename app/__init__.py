from flask import Flask
import pymongo
from celery import Celery
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager
from config import config

db = pymongo.MongoClient('mongo', 27017)
db = db.messages_database
collection = db.messages_collection
limiter = Limiter(key_func=get_remote_address)
jwt = JWTManager()
celery = Celery(__name__, broker=config['development'].CELERY_BROKER_URL)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    celery.conf.update(app.config)
    limiter.init_app(app)
    jwt.init_app(app)
    
    from .views import api_bp
    app.register_blueprint(api_bp)

    return app
