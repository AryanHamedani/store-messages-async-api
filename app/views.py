from flask import Blueprint, request, jsonify
from .tasks import process_message
from . import db, limiter, collection
from flask_jwt_extended import jwt_required, create_access_token

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/token',methods=['GET'])
def generate_token():
    token = create_access_token(identity='test')
    return jsonify(token), 200


@api_bp.route('/messages', methods=['POST'])
@limiter.limit("10 per 60 second")
@jwt_required()
def add_message():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    process_message.delay(message)
    return jsonify({'message': 'Message received and will be processed asynchronously'}), 202

@api_bp.route('/messages', methods=['GET'])
@limiter.limit("10 per 60 second")
@jwt_required()
def get_messages():
    messages = []
    for doc in collection.find():
        messages.append({'id': str(doc['_id']), 'message': doc['message'], 'timestamp': doc['timestamp']})
    return jsonify(messages)



