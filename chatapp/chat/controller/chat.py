from flask.views import MethodView
from flask import request
from chatapp.template import make_output

from chatapp.chat.service.chat import ChatService
from chatapp.chat.model.chat import SendChatRequest, GetChatSessionsRequest, GetChatSessionsResponse, \
    GetChatMessagesResponse, GetChatMessageRequest


class SendChatController(MethodView):
    def __init__(self):
        self.service = ChatService()

    def post(self):
        req = SendChatRequest.Schema().load(request.get_json(force=True, silent=True))
        self.service.send_chat(req)

        return make_output(data={}, status="ok", error=None)


class GetChatSessionsController(MethodView):
    def __init__(self):
        self.service = ChatService()

    def get(self):
        resp_schema = GetChatSessionsResponse.Schema()
        req = GetChatSessionsRequest.Schema().load(request.get_json(force=True, silent=True))
        session_list = self.service.get_session_list(req)
        resp = GetChatSessionsResponse(session_list)

        return make_output(data=resp_schema.dump(resp), status="ok", error=None)


class GetMessagesController(MethodView):
    def __init__(self):
        self.service = ChatService()

    def get(self):
        resp_schema = GetChatMessagesResponse.Schema()
        req = GetChatMessageRequest.Schema().load(request.get_json(force=True, silent=True))
        messages = self.service.get_messages(req)
        resp = GetChatMessagesResponse(messages)

        return make_output(data=resp_schema.dump(resp), status="ok", error=None)
