from chatapp.users.dao.user import UserDAO
from chatapp.users.model.user import SignupRequest


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def signup(self, req: SignupRequest):
        if self.dao.user_exists(req.email):
            return None
        elif req.password != req.password_confirm:
            return None

        self.dao.create_new_user(req)
