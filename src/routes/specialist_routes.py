from flask import jsonify, Blueprint, request
from ..commands.signup_specialist import SignupSpecialist

specialist_routes = Blueprint('specialist_routes', __name__)

@specialist_routes.route('/specialist', methods = ['POST'])
def create():
    specialist = SignupSpecialist(request.get_json()).execute()
    return jsonify(specialist), 201