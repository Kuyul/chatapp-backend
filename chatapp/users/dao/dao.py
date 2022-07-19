from typing import Optional

from common_lib.infra.mysql import DB
from chatapp.users.model.user import UserInfo


class UserDAO:
    def __init__(self):
        self.db = DB()

    def get_all_users(self) -> Optional[UserInfo]:
        query = """
                SELECT USER_ID
                , EMAIL
                , USERNAME
                , FIRST_NAME
                , LAST_NAME
                , CREA_DT
                FROM LIB_USER
                LIMIT 1
                """
        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            user = UserInfo(
                id=row['USER_ID'],
                email=row['EMAIL'],
                username=row['USERNAME'],
                first_name=row['FIRST_NAME'],
                last_name=row['LAST_NAME'],
                created_date=row['CREA_DT']
            )

            return user
