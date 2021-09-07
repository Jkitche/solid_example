

from sqlite3 import Connection, Error, connect
from typing import List, Optional
import os

from src.models.person import Person

from .base_person_repository import BasePersonRepository


class UnknownPersonException(Exception):
    pass


class PersonRepository(BasePersonRepository):
    _connection: Optional[Connection]

    def __init__(self) -> None:
        self._connection = None

    def get_connection(self) -> Connection:
        try:
            file_path = os.path.dirname(os.path.realpath(__file__))
            self._connection = connect(f"{file_path}/test.db")
            return self._connection
        except Error as e:
            raise e

    def get_all_people(self) -> List[Person]:
        conn = self.get_connection()
        results = conn.execute("SELECT * FROM person")
        return [
            Person.from_tuple(row)
            for row in results.fetchall()
        ]

    def get_person_by_id(self, id: int) -> Person:
        conn = self.get_connection()
        results = conn.execute("SELECT * FROM person WHERE id = ?", [id])
        if len(results.fetchall()) == 0:
            raise UnknownPersonException(f"Unable to find person with ID '{id}'")
        return Person.from_tuple(results.fetchone())

    def create_person(self, person: Person) -> None:
        conn = self.get_connection()
        conn.execute("INSERT INTO person (name, age, address) VALUES (?, ?, ?)", [person.name, person.age, person.address])
        conn.commit()

    def delete_person_by_id(self, id: int) -> None:
        conn = self.get_connection()
        conn.execute("DELETE FROM person WHERE id = ?", [id])
        conn.commit()
