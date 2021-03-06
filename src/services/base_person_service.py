from abc import ABC, abstractmethod
from typing import Iterable

from src.models.person import Person


class BasePersonService(ABC):
    @abstractmethod
    # I principle
    async def get_all_people(self) -> Iterable[Person]:
        raise NotImplementedError("Not Implemented!")

    @abstractmethod
    async def get_person_by_id(self, id: int) -> Person:
        raise NotImplementedError("Not Implemented!")

    @abstractmethod
    async def create_person(self, person: Person) -> None:
        raise NotImplementedError("Not Implemented!")

    @abstractmethod
    async def delete_person_by_id(self, id: int) -> None:
        raise NotImplementedError("Not Implemented!")
