from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.users.service.user import UserService
from chatapp.users.model.user import SignupRequest, SigninRequest, SigninRepsonse, GetUserInfoRequest, \
    GetUserInfoResponse



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

        resp_schema = GetUserInfoResponse.Schema()

        return make_output(data=resp_schema.dump(user_info), status="ok", error=None)

