import os
import sqlite3
from typing import Optional

from aiosqlite import Connection, Error, connect


class SqliteConnectionFactory():
    _connection: Optional[Connection]

    def __init__(self):
        self._connection = None

    async def get_connection(self, use_cached: bool=False) -> Connection:
        if self._connection is not None and use_cached:
            return self._connection
        try:
            file_path = os.path.dirname(os.path.realpath(__file__))
            self._connection = await connect(f"{file_path}/test.db")
            self._connection.row_factory = sqlite3.Row
            return self._connection
        except Error as e:
            raise e
