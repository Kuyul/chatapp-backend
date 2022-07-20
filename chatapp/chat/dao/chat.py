from typing import Optional, List
from uuid import uuid4
from common_lib.infra.mysql import DB

from chatapp.chat.model.chat import SendChatRequest, GetChatSessionsRequest, ChatSessionDetails


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

    def get_chat_sessions(self, req: GetChatSessionsRequest) -> List[ChatSessionDetails]:
        query = """
        SELECT CSU.SESS_ID          AS SESS_ID
        , CU.FIRST_NAME             AS USER_FIRST_NAME
        , CSM.MSG                   AS MSG
        , TBL1.MAX_SENT_DT          AS MAX_SENT_DT
        , (SELECT CU2.FIRST_NAME 
            FROM CHAT_SESS_USER CSU2
            INNER JOIN CHAT_USER CU2
            ON CU2.USER_ID = CSU2.USER_ID
            WHERE CSU2.SESS_ID = CSU.SESS_ID  
            AND CSU2.USER_ID != CSU.USER_ID
        LIMIT 1) SESS_OTHER_USER -- finding the name of the other end of the user
        
        , (SELECT CU2.PROF_PIC_URL 
            FROM CHAT_SESS_USER CSU2
            INNER JOIN CHAT_USER CU2
            ON CU2.USER_ID = CSU2.USER_ID
            WHERE CSU2.SESS_ID = CSU.SESS_ID  
            AND CSU2.USER_ID != CSU.USER_ID
        LIMIT 1) SESS_OTHER_USER_PROF -- finding the profile pic of the other end of the user
        
        FROM CHAT_SESS_USER CSU
        INNER JOIN CHAT_SESS_MSG CSM
        ON CSU.SESS_ID = CSM.SESS_ID
        INNER JOIN CHAT_USER CU
        ON CSM.USER_ID = CU.USER_ID
        INNER JOIN (
            SELECT MAX(SENT_DT) AS MAX_SENT_DT
            FROM CHAT_SESS_MSG
            GROUP BY SESS_ID
        ) TBL1
        ON TBL1.MAX_SENT_DT = CSM.SENT_DT
        WHERE CSU.USER_ID = %(user_id)s
        GROUP BY CSU.SESS_ID;
        """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "user_id": req.user_id
            })
            rows = cursor.fetchall()

            return_list = []
            for row in rows:
                return_list.append(
                    ChatSessionDetails(
                        session_id=row['SESS_ID'],
                        session_other_user=row['SESS_OTHER_USER'],
                        prof_pic_url=row['SESS_OTHER_USER_PROF'],
                        last_message=row['MSG'],
                        last_message_time=row['MAX_SENT_DT'],
                        last_sent_user_name=row['USER_FIRST_NAME']
                    )
                )

            return return_list
