from typing import Optional

from pydantic import BaseModel


class Person(BaseModel):
    id: Optional[int]
    name: str
    age: int
    address: str

