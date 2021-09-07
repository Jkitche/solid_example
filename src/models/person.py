from __future__ import annotations

from typing import Optional, Tuple

from pydantic import BaseModel


class Person(BaseModel):
    id: Optional[int]
    name: str
    age: int
    address: str

    @staticmethod
    def from_tuple(tuple: Tuple) -> Person:
        (id, name, age, address) = tuple
        return Person(id=id, name=name, age=age, address=address)
