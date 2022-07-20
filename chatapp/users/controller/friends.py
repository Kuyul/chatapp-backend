from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.users.service.friends import FriendsService
from chatapp.users.model.friends import GetFriendsRequest, GetFriendsResponse


class GetFriendsController(MethodView):
    def __init__(self):
        self.service = FriendsService()

    def get(self):
        req = GetFriendsRequest.Schema().load(request.get_json(force=True, silent=True))
        friends = self.service.get_friends(req)

        resp_schema = GetFriendsResponse.Schema()
        resp = GetFriendsResponse(friends)

        return make_output(data=resp_schema.dump(resp), status="ok", error=None)

