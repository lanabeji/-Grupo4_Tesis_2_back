from flask import jsonify, Blueprint
from ..commands.reset import Reset

base_routes = Blueprint('base_routes', __name__)

@base_routes.route('/health', methods = ['GET'])
def health():
    return jsonify({ 'status': 'ok'})

@base_routes.route('/reset', methods = ['POST'])
def reset():
    Reset().execute()
    return jsonify({'status': 'OK'})