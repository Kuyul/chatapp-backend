from chatapp.chat.dao.chat import ChatDAO
from chatapp.chat.model.chat import SendChatRequest


class ChatService:
    def __init__(self):
        self.dao = ChatDAO()

    def send_chat(self, req: SendChatRequest):
        session_id = req.session_id
        if session_id is None:
            session_id = self.dao.check_session_exist(req)

        # If there is no chat session between two users, create a new session
        if session_id is None:
            session_id = self.dao.create_chat_session(req)

        # send chat to the created session
        self.dao.send_chat_message(session_id, req)
