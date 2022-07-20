from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.chat.service.chat import ChatService
from chatapp.chat.model.chat import SendChatRequest


class SendChatController(MethodView):
    def __init__(self):
        self.service = ChatService()

    def post(self):
        req = SendChatRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.send_chat(req)

        return make_output(data={}, status="ok", error=None)
