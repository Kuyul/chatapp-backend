from typing import Optional
from uuid import uuid4
from common_lib.infra.mysql import DB

from chatapp.chat.model.chat import SendChatRequest


class ChatDAO:
    def __init__(self):
        self.db = DB()

    def check_session_exist(self, req: SendChatRequest):
        # Check if there is a same chat session for both users (that means chat is already activated)

        query = """
        SELECT CSU1.SESS_ID FROM CHAT_SESS_USER CSU1
        INNER JOIN CHAT_SESS_USER CSU2
        ON CSU1.SESS_ID = CSU2.SESS_ID
        WHERE CSU1.USER_ID = %(from_user_id)s
        AND CSU2.USER_ID = %(to_user_id)s;
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "from_user_id": req.from_user_id,
                "to_user_id": req.to_user_id
            })

            row = cursor.fetchone()
            if row is None:
                return None
            else:
                session_id = row['SESS_ID']
                return session_id

    def create_chat_session(self, req: SendChatRequest):
        session_id = str(uuid4())

        query1 = """
        INSERT INTO CHAT_SESS
        (SESS_ID, CREA_ID)
        VALUES
        (%(session_id)s, %(from_user_id)s)
        """

        query2 = """
        INSERT INTO CHAT_SESS_USER
        (SESS_ID, USER_ID)
        VALUES
        (%(session_id)s, %(from_user_id)s),
        (%(session_id)s, %(to_user_id)s)
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query1, {
                "session_id": session_id,
                "from_user_id": req.from_user_id,
            })

            cursor.execute(query2, {
                "session_id": session_id,
                "from_user_id": req.from_user_id,
                "to_user_id": req.to_user_id,
            })

        return session_id

    def send_chat_message(self, session_id: str, req: SendChatRequest):
        query = """
        INSERT INTO CHAT_SESS_MSG
        (SESS_ID, MSG, USER_ID)
        VALUES(
        %(session_id)s, %(message)s, %(from_user_id)s
        )
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "session_id": session_id,
                "message": req.message,
                "from_user_id": req.from_user_id
            })
