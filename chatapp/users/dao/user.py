from typing import Optional
from uuid import uuid4
from common_lib.infra.mysql import DB
from chatapp.users.model.user import SignupRequest


class UserDAO:
    def __init__(self):
        self.db = DB()

    def user_exists(self, email:str) -> bool:
        query = f"""
        SELECT USER_ID
        FROM CHAT_USER
        WHERE EMAIL = "{email}"
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            if row is not None:
                return True
            else:
                return False

    def create_new_user(self, req: SignupRequest):
        query = """
        INSERT INTO CHAT_USER (
            USER_ID, FIRST_NAME, LAST_NAME, EMAIL, PWD
        )
        VALUES (
            %(user_id)s, %(first_name)s, %(last_name)s, %(email)s, %(pwd)s
        );
        """

        uuid = str(uuid4())

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                'user_id': uuid,
                'first_name': req.first_name,
                'last_name': req.last_name,
                'email': req.email,
                'pwd': req.password
            })

    def get_user_by_email(self, email: str):
        query = f"""
        SELECT USER_ID
        FROM CHAT_USER
        WHERE EMAIL = "{email}"
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

            return row['USER_ID']
