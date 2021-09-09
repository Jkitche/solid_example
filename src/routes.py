from tornado.web import StaticFileHandler

from src.database.sqlite_connection_factory import SqliteConnectionFactory
from src.handlers import people_handler, person_handler
from src.repositories.sqlite_person_repository import SqlitePersonRepository
from src.services.date_service import DateService
from src.services.person_service import PersonService
from src.settings import STATIC_PATH

date_service = DateService()
sql_connection_factory = SqliteConnectionFactory()
sqlite_person_repository = SqlitePersonRepository(connection_factory=sql_connection_factory)
person_service = PersonService(person_repository=sqlite_person_repository, date_service=date_service)

routes = [
    (r'/api/people/(\d+)', person_handler.PersonHandler, {"person_service": person_service}),
    (r'/api/people', people_handler.PeopleHandler, {"person_service": person_service}),
    (r"/(.*)", StaticFileHandler, {"path": STATIC_PATH, "default_filename": "index.html"})
]
