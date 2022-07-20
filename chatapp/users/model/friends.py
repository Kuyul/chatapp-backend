from typing import ClassVar, Type, Optional, List
from dataclasses import field
from marshmallow import Schema as MSchema
from dataclasses import dataclass
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class GetFriendsRequest:
    user_id: str


@dataclass
class FriendUser:
    user_id: str
    first_name: str
    last_name: str


@dataclass_with_schema
class GetFriendsResponse:
    friends: List[FriendUser]