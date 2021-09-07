from tornado.web import StaticFileHandler

from src.database.sqlite_connection_factory import SqliteConnectionFactory
from src.dependencies import Dependencies
from src.handlers import people_handler, person_handler
from src.repositories.sqlite_person_repository import SqlitePersonRepository
from src.services.person_service import PersonService
from src.settings import STATIC_PATH

container = Dependencies()
container.register_resource("sqlite_connection_factory", lambda x: SqliteConnectionFactory())
container.register_resource("sqlite_person_repository", lambda x: SqlitePersonRepository(connectionFactory=container.get_dependency("sqlite_connection_factory")))
container.register_resource("person_service", lambda x: PersonService(personRepository=container.get_dependency("sqlite_person_repository")))


routes = [
    (r'/api/people/(\d+)', person_handler.PersonHandler, {"personService": container.get_dependency("person_service")}),
    (r'/api/people', people_handler.PeopleHandler, {"personService": container.get_dependency("person_service")}),
    (r"/(.*)", StaticFileHandler, {"path": STATIC_PATH, "default_filename": "index.html"})
]
