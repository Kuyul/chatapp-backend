from typing import Optional, List
from uuid import uuid4
from common_lib.infra.mysql import DB
from chatapp.users.model.friends import GetFriendsRequest, FriendUser


class FriendsDAO:
    def __init__(self):
        self.db = DB()

    def get_friends(self, req: GetFriendsRequest) -> List[FriendUser]:
        query = """
        SELECT CUF.FRND_ID          AS FRND_ID
        , CU.FIRST_NAME             AS FIRST_NAME
        , CU.LAST_NAME              AS LAST_NAME
        FROM CHAT_USER_FRND CUF
        INNER JOIN CHAT_USER CU
        ON CUF.FRND_ID = CU.USER_ID
        WHERE CU.USER_ID = %(user_id)s;
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "user_id": req.user_id
            })

            rows = cursor.fetchall()
            friends = []

            for row in rows:
                friend = FriendUser(
                    user_id=row['FRND_ID'],
                    first_name=row['FIRST_NAME'],
                    last_name=row['LAST_NAME']
                )

                friends.append(friend)

            return friends
