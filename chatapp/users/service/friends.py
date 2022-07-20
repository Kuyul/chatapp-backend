from chatapp.users.dao.friends import FriendsDAO
from chatapp.users.model.friends import GetFriendsRequest, AddFriendRequest, RemoveFriendRequest


class FriendsService:
    def __init__(self):
        self.dao = FriendsDAO()

    def get_friends(self, req: GetFriendsRequest):
        friends = self.dao.get_friends(req)
        return friends

    def add_friend(self, req: AddFriendRequest):
        # Todo add check to see if they're already friends
        self.dao.add_friend(req)

    def remove_friend(self, req: RemoveFriendRequest):
        self.dao.remove_friend(req)
