from chatapp.users.dao.dao import UserDAO


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def get_users(self):
        return self.dao.get_all_users()
