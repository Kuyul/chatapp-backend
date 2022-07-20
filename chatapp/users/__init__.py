from flask import Blueprint
from flask_restful import Api
from chatapp.users.controller.user import CreateUserController, UserSignInController
from chatapp.users.controller.friends import GetFriendsController

user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')
user_api = Api(user_blueprint)

user_api.add_resource(CreateUserController, "/create")
user_api.add_resource(UserSignInController, "/login")
user_api.add_resource(GetFriendsController, "/friends")
