
from datetime import datetime
from app import celery, collection

@celery.task
def process_message(message, *args, **kwargs):
    doc = {'message': message, 'timestamp': datetime.now()}
    collection.insert_one(doc)

