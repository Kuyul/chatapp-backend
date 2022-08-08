from chatapp.users.dao.user import UserDAO
from chatapp.users.model.user import SignupRequest, SigninRequest, GetUserInfoRequest, SearchUserRequest,\
    UpdateUserInfoRequest


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def signup(self, req: SignupRequest):
        if self.dao.user_exists(req.email):
            return None
        elif req.password != req.password_confirm:
            return None

        self.dao.create_new_user(req)

    def signin(self, req: SigninRequest):
        user_id = self.dao.get_user_by_email(req.email)
        if user_id is None:
            raise Exception("No User Found")

        pwd = self.dao.get_password(user_id)

        if pwd != req.password:
            raise Exception("Incorrect Password")

        return user_id

    def get_user_info(self, req: GetUserInfoRequest):
        user_id = req.user_id
        user_info = self.dao.get_user_information(user_id)
        return user_info

    def search_user_list(self, req: SearchUserRequest):
        keyword = req.keyword
        user_list = self.dao.search_user_list(keyword)
        return user_list

    def update_user_info(self, req: UpdateUserInfoRequest):
        self.dao.update_user_info(req)
