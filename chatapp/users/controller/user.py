from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.users.service.user import UserService
from chatapp.users.model.user import SignupRequest, SigninRequest, SigninRepsonse, GetUserInfoRequest, \
    UserInfo, SearchUserResponse, SearchUserRequest, UpdateUserInfoRequest


class CreateUserController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        validate = SignupRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.signup(validate)

        return make_output(data={}, status="ok", error=None)


class UserSignInController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        resp_schema = SigninRepsonse.Schema()
        validate = SigninRequest.Schema().load(request.get_json(force=True, silent=True))
        user_id = self.service.signin(validate)
        resp = SigninRepsonse(user_id)

        return make_output(data=resp_schema.dump(resp), status="ok", error=None)


class GetUserInfoController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        validate = GetUserInfoRequest.Schema().load(request.get_json(force=True, silent=True))
        user_info = self.service.get_user_info(validate)

        resp_schema = UserInfo.Schema()

        return make_output(data=resp_schema.dump(user_info), status="ok", error=None)


class SearchUserController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        validate = SearchUserRequest.Schema().load(request.get_json(force=True, silent=True))
        user_list = self.service.search_user_list(validate)

        resp_schema = SearchUserResponse.Schema()
        resp = SearchUserResponse(user_list)

        return make_output(data=resp_schema.dump(resp), status="ok", error=None)


class UpdateUserInfoController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        validate = UpdateUserInfoRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.update_user_info(validate)

        return make_output(data={}, status="ok", error=None)
