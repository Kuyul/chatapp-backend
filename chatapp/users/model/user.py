from typing import ClassVar, Type, Optional
from dataclasses import field
from marshmallow import Schema as MSchema
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class UserInfo:
    id: str
    email: str
    username: str
    first_name: str
    last_name: str
    created_date: Optional[str]


@dataclass_with_schema
class TemplateResponse:
    status: str = field(default='ok')
    Schema: ClassVar[Type[MSchema]] = MSchema
