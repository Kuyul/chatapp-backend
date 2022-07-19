from flask import Blueprint
from flask_restful import Api
from chatapp.users.controller.user import CreateUserController

user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')
user_api = Api(user_blueprint)

user_api.add_resource(CreateUserController, "/create_user")
