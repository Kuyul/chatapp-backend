from typing import ClassVar, Type, Optional
from dataclasses import field
from marshmallow import Schema as MSchema
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class SignupRequest:
    email: str
    first_name: str
    last_name: str
    password: str
    password_confirm: str

