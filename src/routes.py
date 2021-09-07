from src.dependencies import Dependencies
from tornado.web import StaticFileHandler

from src.handlers import person_handler, people_handler
from src.repositories.person_repository import PersonRepository
from src.services.person_service import PersonService
from src.settings import STATIC_PATH

container = Dependencies()
container.register_resource("person_repository", lambda x: PersonRepository())
container.register_resource("person_service", lambda x: PersonService(personRepository=container.get_dependency("person_repository")))


routes = [
    (r'/api/people/(\d+)', person_handler.PersonHandler, {"personService": container.get_dependency("person_service")}),
    (r'/api/people', people_handler.PeopleHandler, {"personService": container.get_dependency("person_service")}),
    (r"/(.*)", StaticFileHandler, {"path": STATIC_PATH, "default_filename": "index.html"})
]
