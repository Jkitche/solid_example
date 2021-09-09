from src.models.person import Person
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.repositories.sqlite_person_repository import SqlitePersonRepository


class TestSqlitePersonRepository(IsolatedAsyncioTestCase):
    async def test_get_all_people_success(self):
        person_list = [
            Person(id=1, name="Foo", age=42, address="")
        ]

        self.mock_cursor = AsyncMock()
        self.mock_cursor.close = AsyncMock()
        self.mock_cursor.fetchall = AsyncMock()
        self.mock_cursor.fetchall.return_value = [
            {"id": 1, "name": "Foo", "age": 42, "address": ""}
        ]

        self.mock_connection = AsyncMock()
        self.mock_connection.execute = AsyncMock()
        self.mock_connection.execute.return_value = self.mock_cursor

        self.mock_connection_factory = AsyncMock()
        self.mock_connection_factory.get_connection = AsyncMock()
        self.mock_connection_factory.get_connection.return_value = self.mock_connection

        self.sqlite_person_repository = SqlitePersonRepository(connection_factory=self.mock_connection_factory)

        actual = await self.sqlite_person_repository.get_all_people()
        self.assertEqual(actual, person_list)
