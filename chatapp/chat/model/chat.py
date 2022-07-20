from typing import ClassVar, Type, Optional
from dataclasses import field
from marshmallow import Schema as MSchema
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class GetChatSessionRequest:
    user_id: str


@dataclass_with_schema
class SendChatRequest:
    from_user_id: str
    to_user_id: str
    message: str
    session_id: Optional[str] = None
