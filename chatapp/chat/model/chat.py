from typing import ClassVar, Type, Optional, List
from dataclasses import field
from marshmallow import Schema as MSchema
from datetime import datetime
from dataclasses import dataclass
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class GetChatSessionsRequest:
    user_id: str


@dataclass
class ChatSessionDetails:
    session_id: str
    session_other_user: str
    prof_pic_url: str
    last_sent_user_name: str
    last_message: str
    last_message_time: datetime


@dataclass_with_schema
class GetChatSessionsResponse:
    chat_list: List[ChatSessionDetails]


@dataclass_with_schema
class SendChatRequest:
    from_user_id: str
    to_user_id: str
    message: str
    session_id: Optional[str] = None
