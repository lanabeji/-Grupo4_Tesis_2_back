from flask import jsonify, Blueprint

health_routes = Blueprint('health_routes', __name__)

@health_routes.route('/health', methods = ['GET'])
def health():
    return jsonify({ 'status': 'ok'})