from flask import jsonify, Blueprint, request
from ..commands.signup_specialist import SignupSpecialist
from ..commands.login_specialist import LoginSpecialist

specialist_routes = Blueprint('specialist_routes', __name__)

@specialist_routes.route('/specialist', methods = ['POST'])
def create():
    specialist = SignupSpecialist(request.get_json()).execute()
    return jsonify(specialist), 201

@specialist_routes.route('/auth/login', methods = ['POST'])
def login():
    specialist = LoginSpecialist(request.get_json()).execute()
    return jsonify(specialist), 201