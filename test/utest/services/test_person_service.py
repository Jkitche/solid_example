from datetime import datetime
from src.models.person import Person
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, Mock

from src.services.person_service import PersonService


class TestPersonService(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock_person_repository = Mock()
        self.mock_date_service = Mock()
        self.mock_date_service.get_now.return_value = datetime.now()
        self.person_service = PersonService(person_repository=self.mock_person_repository, date_service=self.mock_date_service)

    async def test_get_all_people_success(self):
        person_list = [
            Person(id=1, name="Foo", age=42, address="")
        ]
        self.mock_person_repository.get_all_people = AsyncMock()
        self.mock_person_repository.get_all_people.return_value = person_list

        actual = await self.person_service.get_all_people()
        self.assertEqual(actual, person_list)

    async def test_get_person_by_id_success(self):
        id = 1
        person = Person(id=id, name="Foo", age=42, address="")
        self.mock_person_repository.get_person_by_id = AsyncMock()
        self.mock_person_repository.get_person_by_id.return_value = person

        actual = await self.person_service.get_person_by_id(id)
        self.assertEqual(actual, person)

    async def test_create_person_success(self):
        person = Person(id=1, name="Foo", age=42, address="")
        self.mock_person_repository.create_person = AsyncMock()

        await self.person_service.create_person(person)
    
    async def test_delete_person_by_id_success(self):
        id = 1
        person = Person(id=id, name="Foo", age=42, address="")
        self.mock_person_repository.get_person_by_id = AsyncMock()
        self.mock_person_repository.get_person_by_id.return_value = person

        self.mock_person_repository.delete_person_by_id = AsyncMock()

        await self.person_service.delete_person_by_id(id)

    async def test_delete_person_by_id_raises(self):
        id = 1
        self.mock_person_repository.get_person_by_id = AsyncMock()
        self.mock_person_repository.get_person_by_id.return_value = None

        self.mock_person_repository.delete_person_by_id = AsyncMock()

        with self.assertRaises(Exception):
            await self.person_service.delete_person_by_id(id)