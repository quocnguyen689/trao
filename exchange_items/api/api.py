from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api")

@api.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})