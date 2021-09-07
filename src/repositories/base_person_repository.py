from abc import ABCMeta, abstractmethod
from typing import List

from src.models.person import Person


class BasePersonRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_all_people(self) -> List[Person]:
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
