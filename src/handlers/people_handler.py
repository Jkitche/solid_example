import json

from src.models.person import Person
from src.services.base_person_service import BasePersonService
from tornado.web import RequestHandler


class PeopleHandler(RequestHandler):
    """
    Handlers are responsible for parsing HTTP requests,
    calling into business logic, and adapting the response to and HTTP spec appropriate response
    """
    def initialize(self, person_service: BasePersonService) -> None:
        """
        Initialize is a method called by tornado/cyclone to inject dependencies

        Args:
            personService (BasePersonService): Person business logic
        """
        self.person_service = person_service

    async def get(self) -> None:
        """
        The HTTP GET method for this handler
        """
        people = await self.person_service.get_all_people()
        people_list = [person.dict() for person in people]
        self.write(json.dumps(people_list, default=str))

    async def post(self) -> None:
        """
        The HTTP POST method for this handler
        """
        data = json.loads(self.request.body)
        person = Person(name=data.get("name"), age=data.get("age"), address=data.get("address"))
        await self.person_service.create_person(person)
