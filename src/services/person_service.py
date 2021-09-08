
from typing import List

from src.models.person import Person
from src.repositories.base_person_repository import BasePersonRepository
from src.services.base_date_service import BaseDateService
from src.services.base_person_service import BasePersonService


class PersonService(BasePersonService):
    def __init__(self, person_repository: BasePersonRepository, date_service: BaseDateService):
        """
        Business logic for Person based operations

        Args:
            personRepository (BasePersonRepository): Data Handler for Person objects
        """
        self.person_repository = person_repository
        self.date_service = date_service

    async def get_all_people(self) -> List[Person]:
        people = await self.person_repository.get_all_people()
        for person in people:
            person.last_accessed = self.date_service.get_now()
        return people

    async def get_person_by_id(self, id: int) -> Person:
        person = await self.person_repository.get_person_by_id(id)
        person.last_accessed = self.date_service.get_now()
        return person

    async def create_person(self, person: Person) -> None:
        await self.person_repository.create_person(person)

    async def delete_person_by_id(self, id: int) -> None:
        person = await self.get_person_by_id(id)
        if person is None:
            raise Exception(f"Could not find person to delete with id '{id}'")
        await self.person_repository.delete_person_by_id(id)
