from __future__ import annotations

from typing import List

from aiosqlite import Connection
from src.database.sqlite_connection_factory import SqliteConnectionFactory
from src.models.person import Person
from src.util.sqlite_person_adapter import SqlitePersonAdapter

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
    def __init__(self, connectionFactory: SqliteConnectionFactory) -> None:
        self.connectionFactory = connectionFactory

    async def _get_connection(self) -> Connection:
        return await self.connectionFactory.get_connection(use_cached=True)

    async def get_all_people(self) -> List[Person]:
        conn = await self._get_connection()
        cursor = await conn.execute("SELECT * FROM person")
        rows = await cursor.fetchall()
        await cursor.close()
        return [
            SqlitePersonAdapter.person_from_sqlite_row(row)
            for row in rows
        ]

    async def get_person_by_id(self, id: int) -> Person:
        conn = await self._get_connection()
        cursor = await conn.execute("SELECT * FROM person WHERE id = ?", [id])
        row = await cursor.fetchone()
        await cursor.close()
        if not row or len(tuple(row)) == 0:
            raise UnknownPersonException(f"Unable to find person with ID '{id}'")
        return SqlitePersonAdapter.person_from_sqlite_row(row)

    async def create_person(self, person: Person) -> None:
        conn = await self._get_connection()
        await conn.execute("INSERT INTO person (name, age, address) VALUES (?, ?, ?)", [person.name, person.age, person.address])
        await conn.commit()

    async def delete_person_by_id(self, id: int) -> None:
        conn = await self._get_connection()
        await conn.execute("DELETE FROM person WHERE id = ?", [id])
        await conn.commit()
