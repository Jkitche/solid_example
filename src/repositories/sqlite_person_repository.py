import os
import sqlite3
from src.util.sqlite_person_adapter import SqlitePersonAdapter
from typing import List, Optional

from aiosqlite import Connection, Error, connect
from src.models.person import Person

from .base_person_repository import BasePersonRepository


class UnknownPersonException(Exception):
    pass


class SqlitePersonRepository(BasePersonRepository):
    """
    Sqlite based implementation for storing and handling Person objects

    Args:
        BasePersonRepository: Base Person Repository

    Raises:
        e: Unknown errors
        UnknownPersonException: When a Person cannot be found by ID
    """
    _connection: Optional[Connection]

    def __init__(self) -> None:
        self._connection = None

    async def get_connection(self) -> Connection:
        try:
            file_path = os.path.dirname(os.path.realpath(__file__))
            self._connection = await connect(f"{file_path}/test.db")
            self._connection.row_factory = sqlite3.Row
            return self._connection
        except Error as e:
            raise e

    async def get_all_people(self) -> List[Person]:
        conn = await self.get_connection()
        cursor = await conn.execute("SELECT * FROM person")
        rows = await cursor.fetchall()
        await cursor.close()
        return [
            SqlitePersonAdapter.person_from_sqlite_row(row)
            for row in rows
        ]

    async def get_person_by_id(self, id: int) -> Person:
        conn = await self.get_connection()
        cursor = await conn.execute("SELECT * FROM person WHERE id = ?", [id])
        row = await cursor.fetchone()
        await cursor.close()
        if not row or len(tuple(row)) == 0:
            raise UnknownPersonException(f"Unable to find person with ID '{id}'")
        return SqlitePersonAdapter.person_from_sqlite_row(row)

    async def create_person(self, person: Person) -> None:
        conn = await self.get_connection()
        await conn.execute("INSERT INTO person (name, age, address) VALUES (?, ?, ?)", [person.name, person.age, person.address])
        await conn.commit()

    async def delete_person_by_id(self, id: int) -> None:
        conn = await self.get_connection()
        await conn.execute("DELETE FROM person WHERE id = ?", [id])
        await conn.commit()
