from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.users.service.user import UserService
from chatapp.users.model.user import SignupRequest


class CreateUserController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        validate = SignupRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.signup(validate)

        return make_output(data={}, status="ok", error=None)
