from typing import Optional, List
from uuid import uuid4
from common_lib.infra.mysql import DB
from chatapp.users.model.friends import GetFriendsRequest, FriendUser, AddFriendRequest, RemoveFriendRequest


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
        WHERE CUF.USER_ID = %(user_id)s;
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

    def add_friend(self, req: AddFriendRequest):
        query = """
        INSERT INTO CHAT_USER_FRND
        (USER_ID, FRND_ID)
        VALUES
        (%(user_id)s, %(friend_id)s),
        (%(friend_id)s, %(user_id)s)
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "user_id": req.user_id,
                "friend_id": req.friend_id
            })

    def remove_friend(self, req: RemoveFriendRequest):
        # Remove friend from both users
        query1 = """
        DELETE FROM CHAT_USER_FRND
        WHERE USER_ID = %(user_id)s
        AND FRND_ID = %(friend_id)s
        """

        query2 = """
        DELETE FROM CHAT_USER_FRND
        WHERE USER_ID = %(friend_id)s
        AND FRND_ID = %(user_id)s
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query1, {
                "user_id": req.user_id,
                "friend_id": req.friend_id
            })

            cursor.execute(query2, {
                "user_id": req.user_id,
                "friend_id": req.friend_id
            })
