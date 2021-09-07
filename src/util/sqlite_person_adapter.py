
from src.models.person import Person
from sqlite3 import Row


class SqlitePersonAdapter:
    @staticmethod
    def person_from_sqlite_row(row: Row) -> Person:
        (id, name, age, address) = tuple(row)
        return Person(id=id, name=name, age=age, address=address)