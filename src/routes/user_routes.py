from flask import jsonify, Blueprint, request
from ..commands.signup_user import SignupUser

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods = ['POST'])
def create():
    user = SignupUser(request.get_json()).execute()
    return jsonify(user), 201