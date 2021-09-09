
from typing import Any, Dict
from src.models.person import Person


class SqlitePersonAdapter:
    @staticmethod
    def person_from_dict(dict: Dict[str, Any]) -> Person:
        return Person(
            id=dict.get("id"),
            name=dict.get("name", ""), 
            age=dict.get("age", 0),
            address=dict.get("address", "")
        )