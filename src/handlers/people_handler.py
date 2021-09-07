import json

from src.models.person import Person
from src.services.person_service import BasePersonRepository
from tornado.web import RequestHandler


class PeopleHandler(RequestHandler):
    """
    Handlers are responsible for parsing HTTP requests,
    calling into business logic, and adapting the response to and HTTP spec appropriate response
    """
    def initialize(self, personService: BasePersonRepository) -> None:
        """
        Initialize is a method called by tornado/cyclone to inject dependencies

        Args:
            data_service (DataService): The Data business logic service
        """
        self.personService = personService

    def get(self) -> None:
        """
        The HTTP GET method for this handler
        """
        people = self.personService.get_all_people()
        people_list = [person.dict() for person in people]
        self.write(json.dumps(people_list))

    def post(self) -> None:
        """
        The HTTP POST method for this handler
        """
        data = json.loads(self.request.body)
        self.personService.create_person(Person(name=data.get("name"), age=data.get("age"), address=data.get("address")))
