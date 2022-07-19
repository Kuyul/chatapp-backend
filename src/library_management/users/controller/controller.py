from flask.views import MethodView
from flask import request

from src.library_management.users.service.service import UserService
from src.library_management.users.model.user import UserInfo


class UserController(MethodView):
    def __init__(self):
        self.service = UserService()

    def get(self):
        resp_schema = UserInfo.Schema()
        res = self.service.get_users()
        return {
            "data": resp_schema.dump(res)
        }
