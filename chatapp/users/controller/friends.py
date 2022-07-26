from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.users.service.friends import FriendsService
from chatapp.users.model.friends import GetFriendsRequest, GetFriendsResponse, AddFriendRequest, RemoveFriendRequest


class GetFriendsController(MethodView):
    def __init__(self):
        self.service = FriendsService()

    def post(self):
        req = GetFriendsRequest.Schema().load(request.get_json(force=True, silent=True))
        friends = self.service.get_friends(req)

        resp_schema = GetFriendsResponse.Schema()
        resp = GetFriendsResponse(friends)

        return make_output(data=resp_schema.dump(resp), status="ok", error=None)


class AddFriendController(MethodView):
    def __init__(self):
        self.service = FriendsService()

    def post(self):
        req = AddFriendRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.add_friend(req)

        return make_output(data={}, status="ok", error=None)


class RemoveFriendController(MethodView):
    def __init__(self):
        self.service = FriendsService()

    def delete(self):
        req = RemoveFriendRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.remove_friend(req)

        return make_output(data={}, status="ok", error=None)
