from flask import Blueprint
from flask_restful import Api
from chatapp.users.controller import UserController

user_blueprint = Blueprint('user', __name__, url_prefix='/api/users')
user_api = Api(user_blueprint)

user_api.add_resource(UserController, "/getusers")
