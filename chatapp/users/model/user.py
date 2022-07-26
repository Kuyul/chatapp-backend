from typing import ClassVar, Type, Optional, List
from dataclasses import field
from marshmallow import Schema as MSchema
from dataclasses import dataclass
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class SignupRequest:
    email: str
    first_name: str
    last_name: str
    password: str
    password_confirm: str


@dataclass_with_schema
class SigninRequest:
    email: str
    password: str


@dataclass_with_schema
class SigninRepsonse:
    user_id: str


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


@dataclass_with_schema
class GetUserInfoRequest:
    user_id: str


@dataclass_with_schema
class GetUserInfoResponse:
    email: str
    first_name: str
    last_name: str
    prof_pic_url: str
