from src.repositories.sqlite_person_repository import UnknownPersonException
from src.services.person_service import BasePersonService
from tornado.web import RequestHandler
from http import HTTPStatus


class PersonHandler(RequestHandler):
    """
    Handlers are responsible for parsing HTTP requests,
    calling into business logic, and adapting the response to and HTTP spec appropriate response
    """
    def initialize(self, personService: BasePersonService) -> None:
        """
        Initialize is a method called by tornado/cyclone to inject dependencies

        Args:
            personService (BasePersonService): Person business logic
        """
        self.personService = personService

    async def get(self, id: int) -> None:
        """
        The HTTP GET method for this handler
        """
        try:
            person = await self.personService.get_person_by_id(id)
            self.write(person.dict())
        except UnknownPersonException as e:
            self.set_status(HTTPStatus.BAD_REQUEST)

    async def delete(self, id: int) -> None:
        """
        The HTTP DELETE method for this handler
        """
        try:
            await self.personService.delete_person_by_id(id)
        except UnknownPersonException as e:
            self.set_status(HTTPStatus.BAD_REQUEST)