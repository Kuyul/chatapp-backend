from flask import Blueprint
from flask_restful import Api
from chatapp.users.controller.user import CreateUserController, UserSignInController, GetUserInfoController,\
    SearchUserController
from chatapp.users.controller.friends import GetFriendsController, AddFriendController, RemoveFriendController

user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')
user_api = Api(user_blueprint)

user_api.add_resource(CreateUserController, "/create")
user_api.add_resource(UserSignInController, "/login")
user_api.add_resource(GetFriendsController, "/friends")
user_api.add_resource(AddFriendController, "/add_friend")
user_api.add_resource(RemoveFriendController, "/remove_friend")
user_api.add_resource(GetUserInfoController, "/user_info")
user_api.add_resource(SearchUserController, "/search")

