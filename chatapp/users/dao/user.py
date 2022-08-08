from typing import List
from uuid import uuid4
from common_lib.infra.mysql import DB
from chatapp.users.model.user import SignupRequest, UserInfo, UpdateUserInfoRequest


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

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                'user_id': str(uuid4()),
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

    def get_password(self, user_id: str):
        query = """
        SELECT PWD
        FROM CHAT_USER
        WHERE USER_ID = %(user_id)s
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                'user_id': user_id
            })
            row = cursor.fetchone()

            return row['PWD']

    def get_user_information(self, user_id: str):
        query = """
        SELECT USER_ID
        , FIRST_NAME
        , LAST_NAME
        , PROF_PIC_URL
        , EMAIL
        FROM CHAT_USER
        WHERE USER_ID = %(user_id)s;
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                'user_id': user_id
            })
            row = cursor.fetchone()

            user_info = UserInfo(
                user_id=row['USER_ID'],
                first_name=row['FIRST_NAME'],
                last_name=row['LAST_NAME'],
                prof_pic_url=row['PROF_PIC_URL'],
                email=row['EMAIL']
            )

            return user_info

    def search_user_list(self, keyword: str) -> List[UserInfo]:

        # Adjust for LIKE statement query
        keyword_query = '%' + keyword + '%'

        query = f"""
        SELECT USER_ID
        , FIRST_NAME
        , LAST_NAME
        , PROF_PIC_URL
        , EMAIL
        FROM CHAT_USER
        WHERE FIRST_NAME LIKE %(keyword)s
        OR LAST_NAME LIKE %(keyword)s
        OR EMAIL LIKE %(keyword)s;
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                'keyword': keyword_query
            })

            rows = cursor.fetchall()

            user_list = []
            for row in rows:
                user = UserInfo(
                    user_id=row['USER_ID'],
                    last_name=row['LAST_NAME'],
                    first_name=row['FIRST_NAME'],
                    prof_pic_url=row['PROF_PIC_URL'],
                    email=row['EMAIL']
                )
                user_list.append(user)

            return user_list

    def update_user_info(self, req: UpdateUserInfoRequest):

        sub_query_list = []
        if req.last_name is not None:
            sub_query = "LAST_NAME = %(last_name)s"
            sub_query_list.append(sub_query)

        if req.first_name is not None:
            sub_query = "FIRST_NAME = %(first_name)s"
            sub_query_list.append(sub_query)

        if req.prof_pic_url is not None:
            sub_query = "PROF_PIC_URL = %(prof_pic_url)s"
            sub_query_list.append(sub_query)

        if len(sub_query_list) > 0:
            sub_query_str = ",".join(sub_query_list)

            query = f"""
            UPDATE CHAT_USER
            SET
            {sub_query_str}
            WHERE USER_ID = %(user_id)s
            """

            with self.db.cursor(dictionary= True) as cursor:
                cursor.execute(query, {
                    "user_id": req.user_id,
                    "last_name": req.last_name,
                    "first_name": req.first_name,
                    "prof_pic_url": req.prof_pic_url
                })
