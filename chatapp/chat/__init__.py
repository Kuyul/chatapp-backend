from flask import Blueprint
from flask_restful import Api

from chatapp.chat.controller.chat import SendChatController, GetChatSessionsController

chat_blueprint = Blueprint('chat', __name__, url_prefix='/api/chat')
chat_api = Api(chat_blueprint)

chat_api.add_resource(SendChatController, "/send_chat")
chat_api.add_resource(GetChatSessionsController, "/chat_list")
