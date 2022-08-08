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
class GetUserInfoRequest:
    user_id: str


@dataclass_with_schema
class UserInfo:
    user_id: str
    email: str
    first_name: str
    last_name: str
    prof_pic_url: str


@dataclass_with_schema
class SearchUserRequest:
    keyword: str


@dataclass_with_schema
class SearchUserResponse:
    user_list: List[UserInfo]


@dataclass_with_schema
class UpdateUserInfoRequest:
    user_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    prof_pic_url: Optional[str] = None
