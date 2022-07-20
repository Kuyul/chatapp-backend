from chatapp.users.dao.friends import FriendsDAO
from chatapp.users.model.friends import GetFriendsRequest


class FriendsService:
    def __init__(self):
        self.dao = FriendsDAO()

    def get_friends(self, req: GetFriendsRequest):
        friends = self.dao.get_friends(req)
        return friends

