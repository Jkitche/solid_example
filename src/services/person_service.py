
from typing import List

from src.models.person import Person
from src.repositories.base_person_repository import BasePersonRepository
from src.services.base_person_service import BasePersonService


class PersonService(BasePersonService):
    def __init__(self, personRepository: BasePersonRepository):
        """
        Business logic for Person based operations

        Args:
            personRepository (BasePersonRepository): Data Handler for Person objects
        """
        self.personRepository = personRepository

    async def get_all_people(self) -> List[Person]:
        return await self.personRepository.get_all_people()

    async def get_person_by_id(self, id: int) -> Person:
        return await self.personRepository.get_person_by_id(id)

    async def create_person(self, person: Person) -> None:
        await self.personRepository.create_person(person)

    async def delete_person_by_id(self, id: int) -> None:
        person = await self.get_person_by_id(id)
        if person is None:
            raise Exception(f"Could not find person to delete with id '{id}'")
        await self.personRepository.delete_person_by_id(id)
