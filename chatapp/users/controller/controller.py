from flask.views import MethodView

from chatapp.users.service.service import UserService
from chatapp.users.model.user import UserInfo


class UserController(MethodView):
    def __init__(self):
        self.service = UserService()

    def get(self):
        resp_schema = UserInfo.Schema()
        res = self.service.get_users()
        return {
            "data": resp_schema.dump(res)
        }
