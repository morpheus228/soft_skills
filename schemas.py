from enum import Enum

from pydantic import BaseModel


class RequestBody(BaseModel):
    color: str
    relax: str
    happy: str
    angry: str
    bad_people: str
    can_not_forgive: str
    music: str
    weak_skill: str
    sphere: str
    result: str

