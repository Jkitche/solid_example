
from src.models.person import Person
from src.repositories.base_person_repository import BasePersonRepository
from src.services.base_person_service import BasePersonService


class PersonService(BasePersonService):
    def __init__(self, personRepository: BasePersonRepository):
        self.personRepository = personRepository

    def get_all_people(self):
        return self.personRepository.get_all_people()

    def get_person_by_id(self, id: int) -> Person:
        return self.personRepository.get_person_by_id(id)

    def create_person(self, person: Person) -> None:
        return self.personRepository.create_person(person)

    def delete_person_by_id(self, id: int) -> None:
        person = self.get_person_by_id(id)
        if person is None:
            raise Exception(f"Could not find person to delete with id '{id}'")
        return self.personRepository.delete_person_by_id(id)
